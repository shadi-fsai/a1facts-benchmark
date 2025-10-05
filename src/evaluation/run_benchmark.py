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
                self.dataset = json.load(f)
            print(f"📁 Loaded {len(self.dataset)} test cases from {dataset_path}")
        else:
            print("📝 Generating new dataset...")
            generator = TestCaseGenerator()
            self.dataset = generator.generate_all()
            print(f"✅ Generated {len(self.dataset)} test cases")
        
        # Initialize models
        self.models = {}
        self._init_models()
        
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
            
            # Standard GPT-4
            try:
                self.models['gpt-4'] = GPT4Model("gpt-4")
                print("  ✅ GPT-4 initialized")
            except Exception as e:
                print(f"  ⚠️  GPT-4 failed: {e}")
            
            # GPT-3.5 Turbo (for comparison)
            try:
                self.models['gpt-3.5-turbo'] = GPT4Model("gpt-3.5-turbo")
                print("  ✅ GPT-3.5-turbo initialized")
            except Exception as e:
                print(f"  ⚠️  GPT-3.5-turbo failed: {e}")
        
        # Anthropic and Google models disabled - only using OpenAI
        # if os.getenv("ANTHROPIC_API_KEY"):
        #     try:
        #         self.models['claude-3.5-sonnet'] = ClaudeModel("claude-3-5-sonnet-20241022")
        #         print("  ✅ Claude 3.5 Sonnet initialized")
        #     except Exception as e:
        #         print(f"  ⚠️  Claude failed: {e}")
        # 
        # if os.getenv("GOOGLE_API_KEY"):
        #     try:
        #         self.models['gemini-2.0-flash'] = GeminiModel("gemini-2.0-flash-exp")
        #         print("  ✅ Gemini 2.0 Flash initialized")
        #     except Exception as e:
        #         print(f"  ⚠️  Gemini failed: {e}")
        
        if not self.models:
            raise ValueError("No models initialized. Please set OPENAI_API_KEY in .env file")
    
    def run_evaluation(self, model_names: List[str] = None, use_comet: bool = True):
        """
        Run evaluation on specified models
        
        Args:
            model_names: List of model names to evaluate (None = all)
            use_comet: Whether to log to Comet
        """
        if model_names is None:
            model_names = list(self.models.keys())
        
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
            metrics = self._calculate_metrics(model_results)
            self._print_metrics(model_name, metrics)
            
            if experiment:
                try:
                    self._log_metrics_to_comet(experiment, metrics)
                    experiment.end()
                    print(f"✅ Logged {model_name} results to Comet successfully")
                except Exception as e:
                    print(f"⚠️  Warning: Failed to log {model_name} to Comet: {e}")
                    print(f"   Results are still saved locally in results/")
        
        return results
    
    def _evaluate_model(self, model, experiment=None) -> List[Dict]:
        """Evaluate a single model on all test cases"""
        results = []
        
        for test_case in tqdm(self.dataset, desc=f"Evaluating {model.model_name}"):
            # Get model prediction
            prediction = model.assess_validity(test_case)
            
            # Compare with ground truth
            validity_correct = prediction['validity_rating'] == test_case['expected_validity']
            
            # Check if reliability scores match (must be same length and same ratings)
            reliability_correct = (
                len(prediction['reliability_scores']) == len(test_case['expected_reliability_scores']) and
                prediction['reliability_scores'] == test_case['expected_reliability_scores']
            )
            
            # Overall correctness: BOTH validity AND reliability must be correct
            both_correct = validity_correct and reliability_correct
            
            result = {
                'test_case_id': test_case['id'],
                'category': test_case['category'],
                'expected_validity': test_case['expected_validity'],
                'predicted_validity': prediction['validity_rating'],
                'expected_reliability': test_case['expected_reliability_scores'],
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
    
    def _print_metrics(self, model_name: str, metrics: Dict):
        """Print metrics in a readable format"""
        print(f"\n📊 Results for {model_name}:")
        print(f"\n  🎯 VALIDITY ASSESSMENT (1-6 scale):")
        print(f"    Overall Accuracy: {metrics.get('validity_accuracy', 0):.2%}")
        print(f"    Macro F1-Score: {metrics.get('validity_macro_f1', 0):.3f}")
        print(f"\n    Per-Rating Performance:")
        for rating in range(1, 7):
            p = metrics.get(f'validity_{rating}_precision', 0)
            r = metrics.get(f'validity_{rating}_recall', 0)
            f1 = metrics.get(f'validity_{rating}_f1', 0)
            sup = metrics.get(f'validity_{rating}_support', 0)
            print(f"      Rating {rating}: P={p:.2f}, R={r:.2f}, F1={f1:.2f}, Support={sup}")
        
        print(f"\n  🔍 RELIABILITY ASSESSMENT (A-F scale):")
        print(f"    Overall Accuracy: {metrics.get('reliability_accuracy', 0):.2%}")
        print(f"    Macro F1-Score: {metrics.get('reliability_macro_f1', 0):.3f}")
        print(f"\n    Per-Rating Performance:")
        for rating in ['A', 'B', 'C', 'D', 'E', 'F']:
            p = metrics.get(f'reliability_{rating}_precision', 0)
            r = metrics.get(f'reliability_{rating}_recall', 0)
            f1 = metrics.get(f'reliability_{rating}_f1', 0)
            sup = metrics.get(f'reliability_{rating}_support', 0)
            print(f"      Rating {rating}: P={p:.2f}, R={r:.2f}, F1={f1:.2f}, Support={sup}")
        
        print(f"\n  ⭐ STRICT ACCURACY (Both correct):")
        print(f"    {metrics.get('strict_accuracy', 0):.2%} ({metrics.get('strict_correct', 0)}/{metrics.get('total_cases', 0)})")
    
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
    # Example usage
    evaluator = BenchmarkEvaluator()
    results = evaluator.run_evaluation(use_comet=True)
    evaluator.save_results(results)
