"""
A1Facts Triangulation Benchmark - Quick Start Runner

This script provides an easy way to run the complete A1Facts benchmark evaluation
across all datasets and models. For advanced usage, use the src.evaluation module directly.

Usage:
    python run_benchmark.py                    # Interactive mode
    python run_benchmark.py --quick           # Quick evaluation (Coverage dataset only)
    python run_benchmark.py --comprehensive   # All datasets evaluation
    python run_benchmark.py --help           # Show detailed help

For advanced usage:
    python -m src.evaluation.run_benchmark --dataset <dataset> --metrics <metrics>
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Optional

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def print_banner():
    """Print the A1Facts benchmark banner"""
    print("🎯" + "="*70 + "🎯")
    print("   🚀 A1Facts Triangulation Benchmark - Quick Start")
    print("   📊 Comprehensive AI Information Assessment Framework")
    print("🎯" + "="*70 + "🎯")

def print_dataset_info():
    """Print information about available datasets"""
    print("\n📋 Available Datasets:")
    print("  1. 🏗️  Manual Dataset (300 cases) - Foundation skills assessment")
    print("  2. 🔺 Coverage Dataset (134 cases) - Systematic triangulation patterns") 
    print("  3. 🧠 Synthesis Dataset (100 cases) - Advanced reasoning & conflicts")
    print("  4. 📊 All Datasets (534 cases) - Complete evaluation framework")

def get_user_choice(prompt: str, options: List[str], default: Optional[str] = None) -> str:
    """Get user choice from a list of options"""
    while True:
        if default:
            choice = input(f"{prompt} [{'/'.join(options)}] (default: {default}): ").strip().lower()
            if not choice:
                return default
        else:
            choice = input(f"{prompt} [{'/'.join(options)}]: ").strip().lower()
        
        if choice in options:
            return choice
        print(f"❌ Please choose from: {', '.join(options)}")

def select_datasets() -> List[str]:
    """Interactive dataset selection"""
    print_dataset_info()
    
    choice = get_user_choice(
        "\n🎯 Select evaluation scope",
        ["1", "2", "3", "4", "quick", "full"],
        "2"
    )
    
    dataset_map = {
        "1": ["datasets/a1facts_manual_300_cases.json"],
        "2": ["datasets/triangulation_benchmark_v1.json"],
        "3": ["datasets/triangulation_synthesis_benchmark_v1.json"], 
        "4": [
            "datasets/a1facts_manual_300_cases.json",
            "datasets/triangulation_benchmark_v1.json",
            "datasets/triangulation_synthesis_benchmark_v1.json"
        ],
        "quick": ["datasets/triangulation_benchmark_v1.json"],
        "full": [
            "datasets/a1facts_manual_300_cases.json",
            "datasets/triangulation_benchmark_v1.json", 
            "datasets/triangulation_synthesis_benchmark_v1.json"
        ]
    }
    
    return dataset_map[choice]

def select_models() -> List[str]:
    """Interactive model selection"""
    print("\n🤖 Available Models:")
    print("  1. GPT-4 (OpenAI)")
    print("  2. Claude (Anthropic)")
    print("  3. Gemini (Google)")
    print("  4. All Models")
    
    choice = get_user_choice(
        "\n🎯 Select models to evaluate",
        ["1", "2", "3", "4", "all"],
        "4"
    )
    
    model_map = {
        "1": ["gpt4"],
        "2": ["claude"],
        "3": ["gemini"],
        "4": ["gpt4", "claude", "gemini"],
        "all": ["gpt4", "claude", "gemini"]
    }
    
    return model_map[choice]

def check_environment() -> bool:
    """Check if environment is properly configured"""
    print("\n🔧 Checking environment configuration...")
    
    # Check for .env file
    env_file = Path(".env")
    if not env_file.exists():
        print("⚠️  .env file not found. Copy .env.example to .env and add your API keys")
        return False
    
    # Check for required directories
    required_dirs = ["datasets", "results", "src"]
    for dir_name in required_dirs:
        if not Path(dir_name).exists():
            print(f"❌ Required directory '{dir_name}' not found")
            return False
    
    # Check for dataset files
    datasets = [
        "datasets/triangulation_benchmark_v1.json",
        "datasets/a1facts_manual_300_cases.json",
        "datasets/triangulation_synthesis_benchmark_v1.json"
    ]
    
    missing_datasets = [d for d in datasets if not Path(d).exists()]
    if missing_datasets:
        print("⚠️  Some datasets are missing:")
        for dataset in missing_datasets:
            print(f"    - {dataset}")
        print("   Run dataset generation first if needed")
    
    print("✅ Environment check complete")
    return True

def run_evaluation(datasets: List[str], models: List[str], use_comet: bool = False):
    """Run the benchmark evaluation"""
    try:
        from src.evaluation.run_benchmark import main as run_benchmark_main
        
        print(f"\n🚀 Starting evaluation...")
        print(f"📊 Datasets: {len(datasets)} dataset(s)")
        print(f"🤖 Models: {', '.join(models)}")
        print(f"📈 Comet logging: {'Enabled' if use_comet else 'Disabled'}")
        
        # Run evaluation for each dataset
        for i, dataset in enumerate(datasets, 1):
            print(f"\n{'='*60}")
            print(f"📋 Dataset {i}/{len(datasets)}: {Path(dataset).name}")
            print(f"{'='*60}")
            
            # Prepare arguments for the evaluation module
            sys.argv = [
                "run_benchmark.py",
                "--dataset", dataset,
                "--models", ",".join(models),
                "--metrics", "tier1"
            ]
            
            if use_comet:
                sys.argv.extend(["--comet"])
            
            # Run the evaluation
            try:
                run_benchmark_main()
            except Exception as e:
                print(f"❌ Error evaluating {dataset}: {e}")
                continue
        
        print(f"\n🎉 Evaluation complete!")
        print(f"\n📊 Next steps:")
        print(f"  1. Check 'results/' directory for detailed output")
        print(f"  2. Review metrics in docs/metrics/README.md") 
        if use_comet:
            print(f"  3. Check your Comet dashboard for experiment tracking")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure you've installed all requirements: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Evaluation error: {e}")

def main():
    """Main entry point for quick start benchmark"""
    parser = argparse.ArgumentParser(
        description="A1Facts Triangulation Benchmark Quick Start",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python run_benchmark.py                    # Interactive mode
    python run_benchmark.py --quick           # Quick evaluation  
    python run_benchmark.py --comprehensive   # All datasets
    
For advanced usage:
    python -m src.evaluation.run_benchmark --help
        """
    )
    
    parser.add_argument("--quick", action="store_true", 
                       help="Quick evaluation (Coverage dataset, all models)")
    parser.add_argument("--comprehensive", action="store_true",
                       help="Comprehensive evaluation (all datasets, all models)")
    parser.add_argument("--comet", action="store_true",
                       help="Enable Comet ML experiment tracking")
    parser.add_argument("--datasets", type=str,
                       help="Comma-separated list of dataset files")
    parser.add_argument("--models", type=str, 
                       help="Comma-separated list of models (gpt4,claude,gemini)")
    
    args = parser.parse_args()
    
    print_banner()
    
    # Check environment first
    if not check_environment():
        print("\n❌ Environment check failed. Please fix the issues above.")
        return 1
    
    # Handle command line modes
    if args.quick:
        datasets = ["datasets/triangulation_benchmark_v1.json"]
        models = ["gpt4", "claude", "gemini"]
        use_comet = args.comet
        
        print("\n⚡ Quick Mode: Coverage dataset with all models")
        
    elif args.comprehensive:
        datasets = [
            "datasets/a1facts_manual_300_cases.json",
            "datasets/triangulation_benchmark_v1.json",
            "datasets/triangulation_synthesis_benchmark_v1.json"
        ]
        models = ["gpt4", "claude", "gemini"]
        use_comet = args.comet
        
        print("\n� Comprehensive Mode: All datasets with all models")
        
    elif args.datasets and args.models:
        datasets = [d.strip() for d in args.datasets.split(",")]
        models = [m.strip() for m in args.models.split(",")]
        use_comet = args.comet
        
        print(f"\n🎯 Custom Mode: {len(datasets)} datasets, {len(models)} models")
        
    else:
        # Interactive mode
        print("\n🎯 Interactive Setup")
        print("Configure your benchmark evaluation:")
        
        datasets = select_datasets()
        models = select_models()
        
        # Ask about Comet
        use_comet_choice = get_user_choice(
            "\n📈 Enable Comet ML experiment tracking?",
            ["y", "n"],
            "n"
        )
        use_comet = use_comet_choice == "y"
    
    # Validate dataset files exist
    missing_files = [d for d in datasets if not Path(d).exists()]
    if missing_files:
        print(f"\n❌ Missing dataset files:")
        for file in missing_files:
            print(f"    - {file}")
        print("\n💡 Generate missing datasets or check file paths")
        return 1
    
    # Run the evaluation
    run_evaluation(datasets, models, use_comet)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
