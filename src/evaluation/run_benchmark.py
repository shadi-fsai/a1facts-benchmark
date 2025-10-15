"""
A1Facts Benchmark Evaluation Pipeline with Comet Integration
"""

import json
import os
from typing import List, Dict
from datetime import datetime
from tqdm import tqdm
import comet_ml
from dotenv import load_dotenv

from ..models import GPT4Model, ClaudeModel, GeminiModel
from ..data_generation import TestCaseGenerator


class BenchmarkEvaluator:
    """Main evaluation pipeline with Comet experiment tracking"""
    
    def __init__(self, dataset_path: str = None):
        load_dotenv()
        
        # Load or generate dataset
        if dataset_path and os.path.exists(dataset_path):
            with open(dataset_path, 'r') as f:
                data = json.load(f)
            
            # Handle different dataset formats
            if isinstance(data, list):
                # Simple list format (triangulation datasets)
                self.dataset = data
            elif isinstance(data, dict) and 'test_cases' in data:
                # Structured format (manual datasets)
                self.dataset = data['test_cases']
            else:
                # Fallback to original data
                self.dataset = data
            
            print(f"📁 Loaded {len(self.dataset)} test cases from {dataset_path}")
            self.dataset_path = dataset_path
        else:
            print("📝 Generating new dataset...")
            generator = TestCaseGenerator()
            self.dataset = generator.generate_all()
            print(f"✅ Generated {len(self.dataset)} test cases")
            self.dataset_path = None
        
        # Initialize models
        self.models = {}
        self._init_models()
        
        # Metric level (will be set by command line args)
        self.metric_level = 'all'
        
        # Comet setup
        self.comet_api_key = os.getenv("COMET_API_KEY")
        self.comet_project = os.getenv("COMET_PROJECT_NAME", "a1facts-benchmark")
        self.comet_workspace = os.getenv("COMET_WORKSPACE")
        
    def _init_models(self):
        """Initialize available models"""
        print("\n🤖 Initializing models...")
        
        if os.getenv("OPENAI_API_KEY"):
            # GPT-4o family
            try:
                self.models['gpt-4o'] = GPT4Model("gpt-4o")
                print("  ✅ GPT-4o initialized")
            except Exception as e:
                print(f"  ⚠️  GPT-4o failed: {e}")
            
            try:
                self.models['gpt-4o-mini'] = GPT4Model("gpt-4o-mini")
                print("  ✅ GPT-4o-mini initialized")
            except Exception as e:
                print(f"  ⚠️  GPT-4o-mini failed: {e}")
            
            # GPT-4 Turbo
            try:
                self.models['gpt-4-turbo'] = GPT4Model("gpt-4-turbo")
                print("  ✅ GPT-4-turbo initialized")
            except Exception as e:
                print(f"  ⚠️  GPT-4-turbo failed: {e}")
            
            # GPT-4 removed due to high cost ($30-60 per 1M tokens)
            # try:
            #     self.models['gpt-4'] = GPT4Model("gpt-4")
            #     print("  ✅ GPT-4 initialized")
            # except Exception as e:
            #     print(f"  ⚠️  GPT-4 failed: {e}")
            
            # GPT-3.5 Turbo (for comparison)
            try:
                self.models['gpt-3.5-turbo'] = GPT4Model("gpt-3.5-turbo")
                print("  ✅ GPT-3.5-turbo initialized")
            except Exception as e:
                print(f"  ⚠️  GPT-3.5-turbo failed: {e}")
        
        # Anthropic models disabled - not using Claude for now
        # if os.getenv("ANTHROPIC_API_KEY"):
        #     try:
        #         self.models['claude-3.5-sonnet'] = ClaudeModel("claude-3-5-sonnet-20241022")
        #         print("  ✅ Claude 3.5 Sonnet initialized")
        #     except Exception as e:
        #         print(f"  ⚠️  Claude failed: {e}")
        
        # Google Gemini models enabled
        if os.getenv("GOOGLE_API_KEY"):
            # Gemini 2.5 models (latest - use correct model names)
            try:
                self.models['gemini-2.5-flash'] = GeminiModel("models/gemini-2.5-flash")
                print("  ✅ Gemini 2.5 Flash initialized")
            except Exception as e:
                print(f"  ⚠️  Gemini 2.5 Flash failed: {e}")
            
            try:
                self.models['gemini-2.5-pro'] = GeminiModel("models/gemini-2.5-pro")
                print("  ✅ Gemini 2.5 Pro initialized")
            except Exception as e:
                print(f"  ⚠️  Gemini 2.5 Pro failed: {e}")
            
            # Gemini 2.0 models  
            try:
                self.models['gemini-2.0-flash'] = GeminiModel("models/gemini-2.0-flash-exp")
                print("  ✅ Gemini 2.0 Flash initialized")
            except Exception as e:
                print(f"  ⚠️  Gemini 2.0 Flash failed: {e}")
            
            # Stable flash model
            try:
                self.models['gemini-flash'] = GeminiModel("models/gemini-flash-latest")
                print("  ✅ Gemini Flash Latest initialized")
            except Exception as e:
                print(f"  ⚠️  Gemini Flash Latest failed: {e}")
        
        if not self.models:
            raise ValueError("No models initialized. Please set OPENAI_API_KEY in .env file")
    
    def run_evaluation(self, model_names: List[str] = None, use_comet: bool = True, parallel: bool = True):
        """
        Run evaluation on specified models
        
        Args:
            model_names: List of model names to evaluate (None = all)
            use_comet: Whether to log to Comet
            parallel: Whether to run models in parallel (much faster)
        """
        if model_names is None:
            model_names = list(self.models.keys())
        
        if parallel and len(model_names) > 1:
            print(f"\n🚀 PARALLEL EVALUATION MODE: Running {len(model_names)} models simultaneously")
            print("⚡ Expected speedup: ~5x faster than sequential")
            return self._run_parallel_evaluation(model_names, use_comet)
        else:
            print(f"\n📝 SEQUENTIAL EVALUATION MODE: Running {len(model_names)} models one by one")
            return self._run_sequential_evaluation(model_names, use_comet)
    
    def _run_sequential_evaluation(self, model_names: List[str], use_comet: bool = True):
        """Original sequential evaluation method"""
        results = {}
        
        for model_name in model_names:
            if model_name not in self.models:
                print(f"⚠️  Model {model_name} not available, skipping...")
                continue
            
            print(f"\n{'='*60}")
            print(f"🎯 Evaluating {model_name}")
            print(f"{'='*60}")
            
            model = self.models[model_name]
            
            # Initialize Comet experiment
            experiment = None
            if use_comet and self.comet_api_key:
                try:
                    experiment = comet_ml.Experiment(
                        api_key=self.comet_api_key,
                        project_name=self.comet_project,
                        workspace=self.comet_workspace,
                    )
                    experiment.set_name(f"{model_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
                    experiment.add_tag("a1facts-triangulation")
                    experiment.log_parameter("model", model_name)
                    experiment.log_parameter("dataset_size", len(self.dataset))
                except Exception as e:
                    print(f"⚠️  Warning: Failed to initialize Comet experiment: {e}")
                    print(f"   Continuing without Comet tracking for {model_name}")
                    experiment = None
            
            # Run evaluation
            model_results = self._evaluate_model(model, experiment)
            results[model_name] = model_results
            
            # Calculate and log metrics
            all_metrics = self._calculate_metrics(model_results)
            filtered_metrics = self._filter_metrics_by_level(all_metrics)
            
            self._print_metrics(model_name, all_metrics)
            
            # Store both full and filtered metrics
            results[model_name] = {
                'raw_results': model_results,
                'all_metrics': all_metrics,
                'filtered_metrics': filtered_metrics
            }
            
            if experiment:
                try:
                    self._log_metrics_to_comet(experiment, all_metrics)
                    experiment.end()
                    print(f"✅ Logged {model_name} results to Comet successfully")
                except Exception as e:
                    print(f"⚠️  Warning: Failed to log {model_name} to Comet: {e}")
                    print(f"   Results are still saved locally in results/")
        
        return results
    
    def _run_parallel_evaluation(self, model_names: List[str], use_comet: bool = True):
        """Run models in parallel for 5x speedup"""
        import concurrent.futures
        import threading
        
        results = {}
        results_lock = threading.Lock()
        
        def evaluate_single_model(model_name):
            """Evaluate a single model in parallel thread"""
            if model_name not in self.models:
                print(f"⚠️  Model {model_name} not available, skipping...")
                return
            
            print(f"🎯 Starting {model_name} evaluation...")
            model = self.models[model_name]
            
            # Initialize Comet experiment
            experiment = None
            if use_comet and self.comet_api_key:
                try:
                    experiment = comet_ml.Experiment(
                        api_key=self.comet_api_key,
                        project_name=self.comet_project,
                        workspace=self.comet_workspace,
                    )
                    experiment.set_name(f"{model_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
                    experiment.add_tag("a1facts-parallel")
                    experiment.log_parameter("model", model_name)
                    experiment.log_parameter("dataset_size", len(self.dataset))
                    experiment.log_parameter("parallel_mode", True)
                except Exception as e:
                    print(f"⚠️  {model_name}: Failed Comet setup: {e}")
                    experiment = None
            
            # Run evaluation
            model_results = self._evaluate_model(model, experiment)
            
            # Calculate metrics
            all_metrics = self._calculate_metrics(model_results)
            filtered_metrics = self._filter_metrics_by_level(all_metrics)
            
            # Thread-safe results storage
            with results_lock:
                results[model_name] = {
                    'raw_results': model_results,
                    'all_metrics': all_metrics,
                    'filtered_metrics': filtered_metrics
                }
                print(f"✅ {model_name} completed: {all_metrics['strict_accuracy']:.1%} strict accuracy")
            
            if experiment:
                try:
                    self._log_metrics_to_comet(experiment, all_metrics)
                    experiment.end()
                except Exception as e:
                    print(f"⚠️  {model_name}: Comet logging failed: {e}")
        
        # Run models in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(model_names), 8)) as executor:
            futures = [executor.submit(evaluate_single_model, name) for name in model_names]
            
            # Wait for all to complete
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"❌ Model evaluation failed: {e}")
        
        print(f"\n🏆 PARALLEL EVALUATION COMPLETED: {len(results)} models finished")
        return results
    
    def _evaluate_model(self, model, experiment=None) -> List[Dict]:
        """Evaluate a single model on all test cases"""
        results = []
        
        for test_case in tqdm(self.dataset, desc=f"Evaluating {model.model_name}"):
            # Get model prediction
            prediction = model.assess_validity(test_case)
            
            # Compare with ground truth
            validity_correct = prediction['validity_rating'] == test_case['expected_validity']
            
            # Handle different reliability formats
            if 'expected_reliability_scores' in test_case:
                # Triangulation format: list of scores
                expected_reliability = test_case['expected_reliability_scores']
                reliability_correct = (
                    len(prediction['reliability_scores']) == len(expected_reliability) and
                    prediction['reliability_scores'] == expected_reliability
                )
            elif 'expected_reliability' in test_case:
                # Manual format: single score
                expected_reliability = [test_case['expected_reliability']]
                reliability_correct = (
                    len(prediction['reliability_scores']) == 1 and
                    prediction['reliability_scores'][0] == test_case['expected_reliability']
                )
            else:
                # No expected reliability data
                expected_reliability = []
                reliability_correct = False
            
            # Overall correctness: BOTH validity AND reliability must be correct
            both_correct = validity_correct and reliability_correct
            
            result = {
                'test_case_id': test_case['id'],
                'category': test_case['category'],
                'expected_validity': test_case['expected_validity'],
                'predicted_validity': prediction['validity_rating'],
                'expected_reliability': expected_reliability,
                'predicted_reliability': prediction['reliability_scores'],
                'validity_correct': validity_correct,
                'reliability_correct': reliability_correct,
                'correct': both_correct,  # Both must be correct
                'reasoning': prediction['reasoning'],
                'raw_response': prediction['raw_response']
            }
            
            results.append(result)
            
            # No per-test-case logging to Comet (reduces noise)
        
        return results
    
    def _calculate_metrics(self, results: List[Dict]) -> Dict:
        """Calculate evaluation metrics with proper classification metrics"""
        from sklearn.metrics import precision_recall_fscore_support, accuracy_score, confusion_matrix
        import numpy as np
        
        total = len(results)
        
        # Extract validity ratings (1-6)
        validity_true = [r['expected_validity'] for r in results if r['predicted_validity'] is not None]
        validity_pred = [r['predicted_validity'] for r in results if r['predicted_validity'] is not None]
        
        # Extract reliability ratings (A-F) - flatten lists
        reliability_true = []
        reliability_pred = []
        for r in results:
            for i, expected_rel in enumerate(r['expected_reliability']):
                if i < len(r['predicted_reliability']):
                    reliability_true.append(expected_rel)
                    reliability_pred.append(r['predicted_reliability'][i])
        
        metrics = {
            'total_cases': total,
        }
        
        # Validity metrics (1-6)
        if validity_true and validity_pred:
            val_accuracy = accuracy_score(validity_true, validity_pred)
            val_precision, val_recall, val_f1, val_support = precision_recall_fscore_support(
                validity_true, validity_pred, labels=[1,2,3,4,5,6], average=None, zero_division=0
            )
            
            metrics['validity_accuracy'] = val_accuracy
            metrics['validity_macro_f1'] = np.mean(val_f1)
            
            # Per-rating validity metrics
            for rating in range(1, 7):
                idx = rating - 1
                metrics[f'validity_{rating}_precision'] = val_precision[idx]
                metrics[f'validity_{rating}_recall'] = val_recall[idx]
                metrics[f'validity_{rating}_f1'] = val_f1[idx]
                metrics[f'validity_{rating}_support'] = int(val_support[idx])
            
            # Validity confusion matrix
            val_cm = confusion_matrix(validity_true, validity_pred, labels=[1,2,3,4,5,6])
            metrics['validity_confusion_matrix'] = val_cm.tolist()
        
        # Reliability metrics (A-F)
        if reliability_true and reliability_pred:
            rel_labels = ['A', 'B', 'C', 'D', 'E', 'F']
            rel_accuracy = accuracy_score(reliability_true, reliability_pred)
            rel_precision, rel_recall, rel_f1, rel_support = precision_recall_fscore_support(
                reliability_true, reliability_pred, labels=rel_labels, average=None, zero_division=0
            )
            
            metrics['reliability_accuracy'] = rel_accuracy
            metrics['reliability_macro_f1'] = np.mean(rel_f1)
            
            # Per-rating reliability metrics
            for i, rating in enumerate(rel_labels):
                metrics[f'reliability_{rating}_precision'] = rel_precision[i]
                metrics[f'reliability_{rating}_recall'] = rel_recall[i]
                metrics[f'reliability_{rating}_f1'] = rel_f1[i]
                metrics[f'reliability_{rating}_support'] = int(rel_support[i])
            
            # Reliability confusion matrix
            rel_cm = confusion_matrix(reliability_true, reliability_pred, labels=rel_labels)
            metrics['reliability_confusion_matrix'] = rel_cm.tolist()
        
        # Overall strict accuracy (both validity AND all reliability scores correct)
        both_correct = sum(1 for r in results if r.get('correct', False))
        metrics['strict_accuracy'] = both_correct / total if total > 0 else 0
        metrics['strict_correct'] = both_correct
        
        return metrics
    
    def _get_dataset_type(self) -> str:
        """Determine dataset type from path"""
        if not self.dataset_path:
            return "unknown"
        
        path_lower = self.dataset_path.lower()
        if "manual" in path_lower:
            return "manual"
        elif "coverage" in path_lower or "triangulation_benchmark" in path_lower:
            return "coverage"
        elif "synthesis" in path_lower:
            return "synthesis"
        else:
            return "unknown"
    
    def _get_tier_metrics(self, dataset_type: str, tier: str) -> list:
        """Get metrics for specific tier and dataset type"""
        
        tier_definitions = {
            "manual": {
                "tier1": [
                    "reliability_accuracy", "validity_accuracy", "strict_accuracy", "reliability_A_f1"
                ],
                "tier2": [
                    "reliability_F_f1", "validity_1_f1", "validity_6_f1", 
                    "reliability_macro_f1", "validity_macro_f1", "total_cases"
                ],
                "tier3": [
                    "reliability_A_precision", "reliability_A_recall", "reliability_B_precision", "reliability_B_recall",
                    "reliability_C_precision", "reliability_C_recall", "reliability_D_precision", "reliability_D_recall", 
                    "reliability_E_precision", "reliability_E_recall", "reliability_F_precision", "reliability_F_recall",
                    "validity_1_precision", "validity_1_recall", "validity_2_precision", "validity_2_recall",
                    "validity_3_precision", "validity_3_recall", "validity_4_precision", "validity_4_recall",
                    "validity_5_precision", "validity_5_recall", "validity_6_precision", "validity_6_recall",
                    "validity_confusion_matrix", "reliability_confusion_matrix"
                ]
            },
            "coverage": {
                "tier1": [
                    "strict_accuracy", "reliability_accuracy", "validity_accuracy", 
                    "reliability_A_f1", "reliability_F_f1"
                ],
                "tier2": [
                    "reliability_B_f1", "reliability_C_f1", "validity_2_f1", "validity_3_f1",
                    "reliability_macro_f1", "validity_macro_f1", "total_cases"
                ],
                "tier3": [
                    "reliability_A_precision", "reliability_A_recall", "reliability_B_precision", "reliability_B_recall",
                    "reliability_C_precision", "reliability_C_recall", "reliability_D_precision", "reliability_D_recall", 
                    "reliability_E_precision", "reliability_E_recall", "reliability_F_precision", "reliability_F_recall",
                    "validity_1_precision", "validity_1_recall", "validity_2_precision", "validity_2_recall",
                    "validity_3_precision", "validity_3_recall", "validity_4_precision", "validity_4_recall",
                    "validity_5_precision", "validity_5_recall", "validity_6_precision", "validity_6_recall",
                    "validity_confusion_matrix", "reliability_confusion_matrix"
                ]
            },
            "synthesis": {
                "tier1": [
                    "strict_accuracy", "reliability_accuracy", "validity_accuracy",
                    "validity_2_f1", "reliability_A_f1", "reliability_F_f1"
                ],
                "tier2": [
                    "validity_3_f1", "validity_4_f1", "reliability_B_f1", "reliability_C_f1",
                    "reliability_macro_f1", "validity_macro_f1", "total_cases"
                ],
                "tier3": [
                    "reliability_A_precision", "reliability_A_recall", "reliability_B_precision", "reliability_B_recall",
                    "reliability_C_precision", "reliability_C_recall", "reliability_D_precision", "reliability_D_recall", 
                    "reliability_E_precision", "reliability_E_recall", "reliability_F_precision", "reliability_F_recall",
                    "validity_1_precision", "validity_1_recall", "validity_2_precision", "validity_2_recall",
                    "validity_3_precision", "validity_3_recall", "validity_4_precision", "validity_4_recall",
                    "validity_5_precision", "validity_5_recall", "validity_6_precision", "validity_6_recall",
                    "validity_confusion_matrix", "reliability_confusion_matrix"
                ]
            },
            "unknown": {
                "tier1": ["strict_accuracy", "reliability_accuracy", "validity_accuracy"],
                "tier2": ["reliability_macro_f1", "validity_macro_f1", "total_cases"],
                "tier3": ["reliability_confusion_matrix", "validity_confusion_matrix"]
            }
        }
        
        return tier_definitions.get(dataset_type, tier_definitions["unknown"]).get(tier, [])
    
    def _filter_metrics_by_level(self, metrics: Dict) -> Dict:
        """Filter metrics based on selected level"""
        if self.metric_level == 'all':
            return metrics
        
        dataset_type = self._get_dataset_type()
        
        # Get metrics for selected tier and all lower tiers
        filtered_metrics = {}
        
        if self.metric_level in ['tier1', 'tier2', 'tier3']:
            # Always include tier 1 (critical)
            tier1_metrics = self._get_tier_metrics(dataset_type, 'tier1')
            
            for metric in tier1_metrics:
                if metric in metrics:
                    filtered_metrics[metric] = metrics[metric]
        
        if self.metric_level in ['tier2', 'tier3']:
            # Include tier 2 (diagnostic)
            tier2_metrics = self._get_tier_metrics(dataset_type, 'tier2')
            
            for metric in tier2_metrics:
                if metric in metrics:
                    filtered_metrics[metric] = metrics[metric]
        
        if self.metric_level == 'tier3':
            # Include tier 3 (analytical)
            tier3_metrics = self._get_tier_metrics(dataset_type, 'tier3')
            
            for metric in tier3_metrics:
                if metric in metrics:
                    filtered_metrics[metric] = metrics[metric]
        
        return filtered_metrics
    
    def _print_metrics(self, model_name: str, metrics: Dict):
        """Print metrics in a readable format based on selected tier"""
        
        # Filter metrics based on level
        filtered_metrics = self._filter_metrics_by_level(metrics)
        dataset_type = self._get_dataset_type()
        
        print(f"\n📊 Results for {model_name} ({self.metric_level.upper()} METRICS):")
        print(f"Dataset Type: {dataset_type.title()} | Level: {self.metric_level}")
        
        # Tier 1 - Critical Metrics (always shown unless empty)
        if self.metric_level in ['tier1', 'tier2', 'tier3', 'all']:
            print(f"\n🎯 TIER 1 - CRITICAL METRICS:")
            
            if 'strict_accuracy' in filtered_metrics:
                print(f"    ⭐ Strict Accuracy: {filtered_metrics['strict_accuracy']:.2%}")
            if 'reliability_accuracy' in filtered_metrics:
                print(f"    🔍 Reliability Accuracy: {filtered_metrics['reliability_accuracy']:.2%}")
            if 'validity_accuracy' in filtered_metrics:
                print(f"    🎯 Validity Accuracy: {filtered_metrics['validity_accuracy']:.2%}")
            
            # Critical F1 scores
            if 'reliability_A_f1' in filtered_metrics:
                print(f"    🏆 A-Tier Source F1: {filtered_metrics['reliability_A_f1']:.3f}")
            if 'reliability_F_f1' in filtered_metrics:
                print(f"    ⚠️  F-Tier Source F1: {filtered_metrics['reliability_F_f1']:.3f}")
            if 'validity_2_f1' in filtered_metrics:
                print(f"    🎯 Validity Level 2 F1: {filtered_metrics['validity_2_f1']:.3f}")
        
        # Tier 2 - Diagnostic Metrics
        if self.metric_level in ['tier2', 'tier3', 'all']:
            print(f"\n📈 TIER 2 - DIAGNOSTIC METRICS:")
            
            if 'reliability_macro_f1' in filtered_metrics:
                print(f"    📊 Reliability Macro F1: {filtered_metrics['reliability_macro_f1']:.3f}")
            if 'validity_macro_f1' in filtered_metrics:
                print(f"    📊 Validity Macro F1: {filtered_metrics['validity_macro_f1']:.3f}")
            
            # Additional diagnostic F1 scores
            diagnostic_f1s = ['validity_1_f1', 'validity_3_f1', 'validity_6_f1', 'reliability_B_f1', 'reliability_C_f1']
            for metric in diagnostic_f1s:
                if metric in filtered_metrics:
                    rating = metric.split('_')[1]
                    metric_type = metric.split('_')[0]
                    print(f"    📋 {metric_type.title()} {rating} F1: {filtered_metrics[metric]:.3f}")
        
        # Tier 3 - Analytical Metrics (detailed per-rating performance)
        if self.metric_level in ['tier3', 'all']:
            print(f"\n🔬 TIER 3 - ANALYTICAL METRICS:")
            
            # Validity detailed breakdown
            validity_ratings_with_data = []
            for rating in range(1, 7):
                if f'validity_{rating}_precision' in filtered_metrics:
                    validity_ratings_with_data.append(rating)
            
            if validity_ratings_with_data:
                print(f"    🎯 Validity Per-Rating Performance:")
                for rating in validity_ratings_with_data:
                    p = filtered_metrics.get(f'validity_{rating}_precision', 0)
                    r = filtered_metrics.get(f'validity_{rating}_recall', 0)
                    f1 = filtered_metrics.get(f'validity_{rating}_f1', 0)
                    sup = filtered_metrics.get(f'validity_{rating}_support', 0)
                    print(f"      Rating {rating}: P={p:.2f}, R={r:.2f}, F1={f1:.2f}, Support={sup}")
            
            # Reliability detailed breakdown
            reliability_ratings_with_data = []
            for rating in ['A', 'B', 'C', 'D', 'E', 'F']:
                if f'reliability_{rating}_precision' in filtered_metrics:
                    reliability_ratings_with_data.append(rating)
            
            if reliability_ratings_with_data:
                print(f"    🔍 Reliability Per-Rating Performance:")
                for rating in reliability_ratings_with_data:
                    p = filtered_metrics.get(f'reliability_{rating}_precision', 0)
                    r = filtered_metrics.get(f'reliability_{rating}_recall', 0)
                    f1 = filtered_metrics.get(f'reliability_{rating}_f1', 0)
                    sup = filtered_metrics.get(f'reliability_{rating}_support', 0)
                    print(f"      Rating {rating}: P={p:.2f}, R={r:.2f}, F1={f1:.2f}, Support={sup}")
        
        # Dataset-specific insights
        if dataset_type != "unknown":
            print(f"\n💡 {dataset_type.upper()} DATASET INSIGHTS:")
            if dataset_type == "manual":
                print(f"    Foundation Skills: Single-source assessment capability")
            elif dataset_type == "coverage":
                print(f"    Pattern Recognition: Multi-source triangulation across {metrics.get('total_cases', 0)} cases")
            elif dataset_type == "synthesis":
                print(f"    Advanced Reasoning: Complex logic and conflict resolution")
        
        print(f"\n📊 Cases: {filtered_metrics.get('total_cases', 0)} | Metric Level: {self.metric_level.upper()}")
    
    def _log_metrics_to_comet(self, experiment, metrics: Dict):
        """Log all metrics to Comet"""
        for metric_name, value in metrics.items():
            if isinstance(value, (int, float)):
                experiment.log_metric(metric_name, value)
    
    def save_results(self, results: Dict, output_dir: str = "results"):
        """Save results to JSON file"""
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filepath = os.path.join(output_dir, f"evaluation_results_{timestamp}.json")
        
        with open(filepath, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n💾 Results saved to: {filepath}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='A1Facts Benchmark Evaluation')
    parser.add_argument('--dataset', type=str, help='Path to dataset JSON file')
    parser.add_argument('--models', nargs='+', help='Models to evaluate (default: all)')
    parser.add_argument('--metrics', choices=['tier1', 'tier2', 'tier3', 'all'], default='all',
                       help='Metric detail level: tier1=critical, tier2=diagnostic, tier3=analytical, all=everything')
    parser.add_argument('--no-comet', action='store_true', help='Disable Comet logging')
    
    args = parser.parse_args()
    
    # Initialize evaluator
    evaluator = BenchmarkEvaluator(dataset_path=args.dataset)
    
    # Set metric level
    evaluator.metric_level = args.metrics
    
    # Run evaluation
    results = evaluator.run_evaluation(
        model_names=args.models,
        use_comet=not args.no_comet
    )
    
    # Save results
    evaluator.save_results(results)
