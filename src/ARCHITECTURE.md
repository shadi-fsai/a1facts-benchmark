# A1Facts Benchmark - Complete Structure

## 📁 Directory Tree

```
c:\a1facts\benchmark\
│
├── 📄 README.md                          Main documentation
├── 📄 SETUP_GUIDE.md                     Setup instructions
├── 📄 PROJECT_SUMMARY.md                 Project overview
├── 📄 requirements.txt                   Python dependencies
├── 📄 .env.example                       Environment template
├── 📄 .gitignore                         Git ignore rules
├── 📄 run_benchmark.py                   🚀 Main execution script
│
├── 📂 src/                               Source code
│   ├── __init__.py
│   │
│   ├── 📂 data_generation/              Test case generation
│   │   ├── __init__.py
│   │   ├── domain_authority.py          80+ domain reliability mappings
│   │   └── generate_dataset.py          Test case generator (14 cases)
│   │
│   ├── 📂 models/                       LLM wrappers
│   │   ├── __init__.py
│   │   ├── base_model.py                Abstract interface
│   │   ├── gpt4_model.py                OpenAI GPT-4o
│   │   ├── claude_model.py              Anthropic Claude 3.5
│   │   └── gemini_model.py              Google Gemini 2.0
│   │
│   └── 📂 evaluation/                   Evaluation pipeline
│       ├── __init__.py
│       ├── run_benchmark.py             Main evaluation + Comet
│       └── analyze_results.py           Analysis & visualization
│
├── 📂 datasets/                         Test datasets
│   ├── README.md
│   └── (generated) triangulation_benchmark_v1.json
│
├── 📂 results/                          Evaluation outputs
│   └── (generated) evaluation_results_*.json
│   └── (generated) *.png, *.csv
│
├── 📂 experiments/                      Comet experiment logs
│
└── 📂 notebooks/                        Jupyter analysis notebooks
```

## 🎯 What Each File Does

### Core Execution
| File | Purpose | Usage |
|------|---------|-------|
| `run_benchmark.py` | One-command execution | `python run_benchmark.py` |
| `requirements.txt` | Dependencies | `pip install -r requirements.txt` |
| `.env.example` | API key template | Copy to `.env` and configure |

### Data Generation
| File | Purpose | Key Features |
|------|---------|--------------|
| `domain_authority.py` | Website reliability mappings | 80+ domains (NIH=A, Mayo=B, WebMD=C, etc.) |
| `generate_dataset.py` | Test case generator | 14 objective cases across 6 validity ratings |

### Model Integration
| File | Model | API |
|------|-------|-----|
| `gpt4_model.py` | GPT-4o | OpenAI |
| `claude_model.py` | Claude 3.5 Sonnet | Anthropic |
| `gemini_model.py` | Gemini 2.0 Flash | Google |
| `base_model.py` | Interface | All models inherit |

### Evaluation
| File | Purpose | Output |
|------|---------|--------|
| `run_benchmark.py` | Run evaluation | JSON results + Comet logs |
| `analyze_results.py` | Generate reports | CSV tables + PNG charts |

## 🔄 Data Flow

```
1. Dataset Generation
   generate_dataset.py → triangulation_benchmark_v1.json
   
2. Model Evaluation
   run_benchmark.py → Loads dataset
                   → Initializes models (GPT-4o, Claude, Gemini)
                   → Runs evaluation
                   → Logs to Comet
                   → Saves results/*.json
   
3. Analysis
   analyze_results.py → Loads results/*.json
                      → Generates comparison tables
                      → Creates visualizations
                      → Outputs CSV + PNG files
```

## 📊 Test Cases Breakdown

### Validity Rating 1: Confirmed (3 cases)
- **medical_fact**: CDC + NIH + WHO agree on diabetes prevalence
- **financial_fact**: SEC filing + Reuters + Bloomberg confirm Apple revenue
- **historical_event**: AP + BBC + Reuters confirm 2020 election results

### Validity Rating 2: Probably True (2 cases)
- **market_reaction**: Earnings → stock rise → analyst upgrade (logical chain)
- **medical_correlation**: Drug effectiveness → recommendations → sales (consistent)

### Validity Rating 3: Possibly True (2 cases)
- **geopolitical_implication**: Russia invasion → China readiness → defense stocks
- **tech_speculation**: Apple AI chip → semiconductor stocks → industry expectations

### Validity Rating 4: Doubtful (2 cases)
- **contradiction**: Record revenue contradicts bankruptcy filing
- **logical_inconsistency**: Obesity ↓ contradicts diabetes ↑ + fast food ↑

### Validity Rating 5: Improbable (3 cases)
- **mathematical_impossibility**: 5 employees × $50k ≠ $10B revenue
- **temporal_impossibility**: Cannot discontinue before release
- **physical_impossibility**: 500mph × 2hr ≠ 3,500 miles

### Validity Rating 6: Cannot Judge (2 cases)
- **unrelated_information**: Weather + Bitcoin + NFL (no connection)
- **insufficient_context**: Vague claims from unknown sources

## 🚀 Usage Workflow

### Quick Start (1 command)
```bash
python run_benchmark.py
```

### Manual Steps
```bash
# 1. Generate dataset
cd src/data_generation
python generate_dataset.py

# 2. Run evaluation
cd ../..
python -m src.evaluation.run_benchmark

# 3. Analyze results
python -m src.evaluation.analyze_results results/evaluation_results_*.json
```

### Custom Evaluation
```python
from src.evaluation import BenchmarkEvaluator

evaluator = BenchmarkEvaluator("datasets/triangulation_benchmark_v1.json")

# Evaluate specific models
results = evaluator.run_evaluation(
    model_names=["gpt-4o", "claude-3.5-sonnet"],
    use_comet=True
)

evaluator.save_results(results)
```

## 📈 Expected Metrics

### Overall Accuracy
- Target: >85% for production-ready models
- Measures: Correct validity rating predictions

### Per-Validity Accuracy
- Rating 1 (Confirmed): Should be 100% (obvious agreement)
- Rating 5 (Improbable): Should be >90% (clear impossibilities)
- Rating 3 (Possibly True): Hardest category (subjective boundary)

### Confusion Matrix
- Shows which ratings models confuse (e.g., 2 vs 3)
- Identifies systematic biases

## 🎓 Comet Dashboard Metrics

Automatically logged for each experiment:
- `overall_accuracy`: Primary metric
- `validity_1_accuracy` through `validity_6_accuracy`
- `medical_fact_accuracy`, `financial_fact_accuracy`, etc.
- `total_cases`, `correct_predictions`

## ✅ Validation Checklist

Before running:
- [ ] API keys configured in `.env`
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Comet account created (free at comet.com)

After running:
- [ ] Check `results/` for JSON output
- [ ] Check Comet dashboard for experiments
- [ ] Review confusion matrices for systematic errors
- [ ] Compare models in CSV table

## 🔧 Troubleshooting

**Import Error: comet_ml**
```bash
pip install comet-ml
```

**API Key Not Found**
```bash
# Edit .env file
OPENAI_API_KEY=sk-...
COMET_API_KEY=...
```

**No Models Available**
- Ensure at least one model API key is set
- Models initialize independently (partial success OK)

## 📝 Next Development Steps

1. **Expand Dataset**: 20+ cases per validity rating (120 total)
2. **Add Domains**: Legal, scientific, technical scenarios
3. **Expert Validation**: Get domain experts to review edge cases
4. **Real-time Events**: Test on post-training-cutoff news
5. **Custom Analysis**: Domain-specific performance metrics

## 🎯 Success Criteria

✅ Framework evaluates triangulation logic
✅ Multi-model comparison enabled
✅ Objective ground truth established
✅ Comet integration working
✅ Production-ready code quality
✅ Extensible architecture
