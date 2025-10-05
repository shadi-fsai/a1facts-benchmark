# A1Facts Triangulation Benchmark - Setup Guide

## Prerequisites

- Python 3.9 or higher
- API keys for the models you want to test

## Quick Setup

### 1. Install Dependencies

```bash
cd c:\a1facts\benchmark
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy example environment file
copy .env.example .env
```

Edit `.env` and add your API keys:

```env
# Required: At least one model API key
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AI...

# Required: Comet tracking (get free API key at comet.com)
COMET_API_KEY=...
COMET_PROJECT_NAME=a1facts-benchmark
COMET_WORKSPACE=your-username
```

### 3. Run the Benchmark

```bash
python run_benchmark.py
```

This will:
1. Generate test dataset (14 initial cases across 6 validity categories)
2. Evaluate all available models
3. Log results to Comet
4. Save detailed results to `results/` directory

## Manual Steps

### Generate Dataset Only

```bash
cd src/data_generation
python generate_dataset.py
```

### Run Evaluation Only

```python
from src.evaluation import BenchmarkEvaluator

evaluator = BenchmarkEvaluator("datasets/triangulation_benchmark_v1.json")
results = evaluator.run_evaluation(model_names=["gpt-4o"], use_comet=True)
evaluator.save_results(results)
```

### Analyze Results

```bash
python -m src.evaluation.analyze_results results/evaluation_results_TIMESTAMP.json
```

This generates:
- Model comparison table (CSV)
- Accuracy comparison chart (PNG)
- Confusion matrices per model (PNG)
- Classification reports (console)

## Expected Output

### Dataset Statistics
```
✅ Generated 14 test cases
📁 Saved to: datasets/triangulation_benchmark_v1.json

📊 Dataset Statistics:
  Rating 1: 3 cases  (Confirmed)
  Rating 2: 2 cases  (Probably True)
  Rating 3: 2 cases  (Possibly True)
  Rating 4: 2 cases  (Doubtful)
  Rating 5: 3 cases  (Improbable)
  Rating 6: 2 cases  (Cannot Judge)
```

### Evaluation Results
```
🎯 Evaluating gpt-4o
Evaluating gpt-4o: 100%|████████| 14/14 [00:45<00:00,  3.24s/it]

📊 Results for gpt-4o:
  Overall Accuracy: 85.71%
  Correct: 12/14

  Per-Validity-Rating Accuracy:
    Rating 1: 100.00% (3 cases)
    Rating 2: 100.00% (2 cases)
    Rating 3: 50.00% (2 cases)
    Rating 4: 100.00% (2 cases)
    Rating 5: 100.00% (3 cases)
    Rating 6: 50.00% (2 cases)
```

## Comet Dashboard

Once experiments are running, view them at:
- https://www.comet.com/YOUR_WORKSPACE/a1facts-benchmark

You'll see:
- Real-time accuracy metrics
- Per-validity-rating performance
- Model comparison charts
- Experiment parameters and logs

## Troubleshooting

### Import Errors
```bash
# Install missing packages
pip install comet-ml openai anthropic google-generativeai
```

### API Key Errors
```
ValueError: OPENAI_API_KEY not found in environment
```
Solution: Add API key to `.env` file

### Comet Not Logging
- Get free API key at https://www.comet.com/signup
- Add to `.env`: `COMET_API_KEY=your-key`
- Set workspace: `COMET_WORKSPACE=your-username`

## Next Steps

1. **Expand Dataset**: Add more test cases in `src/data_generation/generate_dataset.py`
2. **Add Models**: Create new model wrappers in `src/models/`
3. **Custom Metrics**: Extend `analyze_results.py` with domain-specific analysis
4. **Production Validation**: Use results to select best model for A1Facts

## File Structure

```
benchmark/
├── README.md                      # This file
├── SETUP_GUIDE.md                 # Detailed setup
├── run_benchmark.py               # Quick start script
├── requirements.txt               # Dependencies
├── .env.example                   # Environment template
│
├── src/
│   ├── data_generation/
│   │   ├── domain_authority.py    # Website reliability mapping
│   │   └── generate_dataset.py    # Test case generator
│   ├── models/
│   │   ├── base_model.py          # Model interface
│   │   ├── gpt4_model.py          # GPT-4o wrapper
│   │   ├── claude_model.py        # Claude wrapper
│   │   └── gemini_model.py        # Gemini wrapper
│   └── evaluation/
│       ├── run_benchmark.py       # Main evaluation
│       └── analyze_results.py     # Results analysis
│
├── datasets/
│   └── triangulation_benchmark_v1.json
├── results/
│   └── evaluation_results_*.json
└── experiments/                   # Comet logs
```
