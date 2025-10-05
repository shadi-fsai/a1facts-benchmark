"""
Analyze benchmark results and generate comparison reports
"""

import json
import os
from typing import Dict, List
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report


class ResultsAnalyzer:
    """Analyze and visualize benchmark results"""
    
    def __init__(self, results_file: str):
        with open(results_file, 'r') as f:
            self.results = json.load(f)
        
        self.models = list(self.results.keys())
        print(f"📊 Loaded results for {len(self.models)} models")
    
    def generate_comparison_table(self) -> pd.DataFrame:
        """Generate model comparison table"""
        comparison_data = []
        
        for model_name, model_results in self.results.items():
            # Calculate metrics
            total = len(model_results)
            correct = sum(1 for r in model_results if r['correct'])
            accuracy = correct / total if total > 0 else 0
            
            # Per-validity accuracy
            validity_accuracies = {}
            for rating in range(1, 7):
                rating_cases = [r for r in model_results if r['expected_validity'] == rating]
                if rating_cases:
                    rating_correct = sum(1 for r in rating_cases if r['correct'])
                    validity_accuracies[f'V{rating}'] = f"{rating_correct/len(rating_cases):.1%}"
                else:
                    validity_accuracies[f'V{rating}'] = 'N/A'
            
            comparison_data.append({
                'Model': model_name,
                'Overall Accuracy': f"{accuracy:.1%}",
                'Correct': f"{correct}/{total}",
                **validity_accuracies
            })
        
        df = pd.DataFrame(comparison_data)
        return df
    
    def plot_model_comparison(self, output_file: str = None):
        """Plot model comparison chart"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Overall accuracy comparison
        accuracies = []
        model_names = []
        for model_name, model_results in self.results.items():
            total = len(model_results)
            correct = sum(1 for r in model_results if r['correct'])
            accuracies.append(correct / total if total > 0 else 0)
            model_names.append(model_name)
        
        ax1.bar(model_names, accuracies, color='skyblue')
        ax1.set_ylabel('Accuracy')
        ax1.set_title('Overall Model Accuracy Comparison')
        ax1.set_ylim(0, 1)
        for i, v in enumerate(accuracies):
            ax1.text(i, v + 0.02, f'{v:.1%}', ha='center')
        
        # Per-validity accuracy heatmap
        validity_data = []
        for model_name in model_names:
            model_results = self.results[model_name]
            row = []
            for rating in range(1, 7):
                rating_cases = [r for r in model_results if r['expected_validity'] == rating]
                if rating_cases:
                    rating_correct = sum(1 for r in rating_cases if r['correct'])
                    row.append(rating_correct / len(rating_cases))
                else:
                    row.append(0)
            validity_data.append(row)
        
        sns.heatmap(validity_data, annot=True, fmt='.1%', cmap='YlGnBu',
                    xticklabels=[f'V{i}' for i in range(1, 7)],
                    yticklabels=model_names, ax=ax2)
        ax2.set_title('Per-Validity-Rating Accuracy')
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"📈 Plot saved to: {output_file}")
        else:
            plt.show()
    
    def generate_confusion_matrices(self, model_name: str):
        """Generate confusion matrix for a specific model"""
        model_results = self.results[model_name]
        
        y_true = [r['expected_validity'] for r in model_results]
        y_pred = [r['predicted_validity'] if r['predicted_validity'] else 0 
                  for r in model_results]
        
        cm = confusion_matrix(y_true, y_pred, labels=[1, 2, 3, 4, 5, 6])
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=[f'V{i}' for i in range(1, 7)],
                    yticklabels=[f'V{i}' for i in range(1, 7)])
        plt.title(f'Confusion Matrix: {model_name}')
        plt.ylabel('True Validity Rating')
        plt.xlabel('Predicted Validity Rating')
        plt.tight_layout()
        
        output_file = f"results/confusion_matrix_{model_name}.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"📊 Confusion matrix saved to: {output_file}")
        
        # Print classification report
        print(f"\n📋 Classification Report for {model_name}:")
        print(classification_report(y_true, y_pred, 
                                   labels=[1, 2, 3, 4, 5, 6],
                                   target_names=[f'V{i}' for i in range(1, 7)]))
    
    def generate_full_report(self, output_dir: str = "results"):
        """Generate complete analysis report"""
        os.makedirs(output_dir, exist_ok=True)
        
        print("\n" + "="*60)
        print("A1FACTS TRIANGULATION BENCHMARK - FULL REPORT")
        print("="*60)
        
        # Comparison table
        print("\n📊 Model Comparison Table:")
        df = self.generate_comparison_table()
        print(df.to_string(index=False))
        
        # Save to CSV
        csv_file = os.path.join(output_dir, "model_comparison.csv")
        df.to_csv(csv_file, index=False)
        print(f"\n💾 Table saved to: {csv_file}")
        
        # Comparison plot
        plot_file = os.path.join(output_dir, "model_comparison.png")
        self.plot_model_comparison(plot_file)
        
        # Confusion matrices for each model
        for model_name in self.models:
            self.generate_confusion_matrices(model_name)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python analyze_results.py <results_file.json>")
        sys.exit(1)
    
    analyzer = ResultsAnalyzer(sys.argv[1])
    analyzer.generate_full_report()
