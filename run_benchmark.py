"""
Quick start script to run the complete A1Facts benchmark
"""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.data_generation import TestCaseGenerator
from src.evaluation import BenchmarkEvaluator


def main():
    print("🚀 A1Facts Triangulation Benchmark")
    print("="*60)
    
    # Step 1: Generate dataset
    print("\n📝 Step 1: Generating test dataset...")
    generator = TestCaseGenerator()
    dataset_path = "datasets/triangulation_benchmark_v1.json"
    generator.save_dataset(dataset_path)
    
    # Step 2: Run evaluation
    print("\n🎯 Step 2: Running evaluation...")
    evaluator = BenchmarkEvaluator(dataset_path)
    
    # Ask user about Comet
    use_comet = input("\nLog to Comet? (y/n) [default: n]: ").lower() == 'y'
    
    # Run evaluation on all available models
    results = evaluator.run_evaluation(use_comet=use_comet)
    
    # Step 3: Save results
    print("\n💾 Step 3: Saving results...")
    evaluator.save_results(results)
    
    print("\n✅ Benchmark complete!")
    print("\n📊 Next steps:")
    print("  1. Check results/ directory for detailed output")
    print("  2. Run: python -m src.evaluation.analyze_results <results_file>")
    print("  3. Check Comet dashboard for experiment tracking")


if __name__ == "__main__":
    main()
