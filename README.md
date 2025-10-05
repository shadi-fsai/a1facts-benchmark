# a1facts-benchmark

# A1Facts Triangulation Benchmark

This benchmark evaluates how well different LLMs can perform the core triangulation tasks that power A1Facts knowledge acquisition:

1. **Source Reliability Assessment** (A-F scale)
2. **Information Validity Assessment** (1-6 scale)

## Purpose

A1Facts uses intelligent triangulation to solve LLM hallucination by combining multiple information sources. This benchmark validates whether LLMs can reliably perform both critical dimensions of triangulation:

- **Assess web source credibility** (Rate each source A-F based on reliability)
- **Evaluate information validity** (Rate claims 1-6 based on corroboration and logic)
- **Triangulate across sources** (Synthesize multiple sources into a validity judgment)
- **Identify contradictions** (Detect logical inconsistencies and impossibilities)

## Models Evaluated

Current benchmark tests 5 OpenAI models:
-  GPT-4o
-  GPT-4o-mini
-  GPT-4-turbo
-  GPT-4
-  GPT-3.5-turbo

Future models to add:
- Anthropic Claude 3.5 Sonnet
- Google Gemini 2.0 Flash
- OpenAI O3 (when available)

## Project Structure

```
benchmark/
├── src/
│   ├── data_generation/     # Dataset creation scripts
│   │   ├── generate_dataset.py
│   │   └── domain_authority.py
│   ├── evaluation/          # Evaluation pipeline
│   │   ├── run_benchmark.py
│   │   └── analyze_results.py
│   └── models/              # Model wrappers (GPT, Claude, Gemini)
│       ├── base_model.py
│       ├── gpt4_model.py
│       ├── claude_model.py
│       └── gemini_model.py
├── datasets/                # Test case datasets (23 cases)
│   └── triangulation_benchmark_v1.json
├── results/                 # Evaluation results (JSON)
└── .env                     # API keys configuration
```

## Quick Start

### 1. Install Dependencies
```bash
cd c:\a1facts\benchmark
pip install -r requirements.txt
```

### 2. Configure API Keys
```bash
# Edit .env file and add your OpenAI API key
OPENAI_API_KEY=sk-proj-...

# Optional: Add Comet for experiment tracking
COMET_API_KEY=...
COMET_WORKSPACE=your-username
```

### 3. Run the Benchmark
```bash
python run_benchmark.py
```

This will:
- Load 23 test cases from the dataset
- Evaluate all OpenAI models (GPT-4o, GPT-4o-mini, GPT-4-turbo, GPT-4, GPT-3.5-turbo)
- Calculate precision, recall, F1-scores for both validity and reliability
- Save results to `results/evaluation_results_<timestamp>.json`
- Optionally log to Comet ML

## Dataset Overview

**Current Dataset:** 23 test cases covering all 6 validity ratings

### Validity Rating Scale (1-6)

- **Rating 1 (Confirmed)**: Multiple independent reliable sources agree
  - Example: "Diabetes affects 11.3% of US adults" (NIH, CDC, WHO all confirm)
  
- **Rating 2 (Probably True)**: Logical and consistent, but not fully corroborated
  - Example: Market reactions consistent with known events
  
- **Rating 3 (Possibly True)**: Plausible but lacks strong corroboration
  - Example: Medical correlations from limited studies
  
- **Rating 4 (Doubtful)**: Contradicted by other information
  - Example: Claims contradicting established facts
  
- **Rating 5 (Improbable)**: Illogical and contradicted by multiple sources
  - Example: Medical impossibilities, mathematical contradictions
  
- **Rating 6 (Cannot Judge)**: Insufficient or unrelated information
  - Example: Context missing, sources don't address the question

### Reliability Rating Scale (A-F)

- **A (Completely reliable)**: Government agencies (NIH, CDC, SEC), peer-reviewed journals
- **B (Usually reliable)**: Major news outlets (Reuters, Bloomberg), reputable institutions
- **C (Fairly reliable)**: Established sites (WebMD, Mayo Clinic) with some quality concerns
- **D (Not usually reliable)**: Blogs, opinion sites, unverified sources
- **E (Unreliable)**: Known for misinformation (NaturalNews, conspiracy sites)
- **F (Cannot judge)**: Unknown domains, insufficient information

## Evaluation Metrics

The benchmark calculates **57 total metrics** across three categories:

### 🎯 Validity Assessment Metrics (27)
- Overall accuracy and macro F1-score
- Per-rating (1-6) metrics:
  - Precision: Of predictions for this rating, how many were correct?
  - Recall: Of actual cases with this rating, how many were found?
  - F1-score: Harmonic mean of precision and recall
  - Support: Number of test cases with this rating
- Confusion matrix: 6×6 matrix showing prediction patterns

### 🔍 Reliability Assessment Metrics (27)
- Overall accuracy and macro F1-score
- Per-rating (A-F) metrics:
  - Precision: Of predictions for this rating, how many were correct?
  - Recall: Of actual sources with this rating, how many were found?
  - F1-score: Harmonic mean of precision and recall
  - Support: Number of sources with this rating
- Confusion matrix: 6×6 matrix showing prediction patterns

### ⭐ Overall Metrics (3)
- **Strict accuracy**: Both validity AND all reliability scores must be correct
- Correct count
- Total test cases

## Sample Results

Based on initial evaluation of 23 test cases:

| Model | Validity Accuracy | Reliability Accuracy | Strict Accuracy |
|-------|-------------------|----------------------|-----------------|
| GPT-4 | TBD | TBD | TBD |
| GPT-4o | TBD | TBD | TBD |
| GPT-4-turbo | TBD | TBD | TBD |

*(Run the benchmark to see actual results)*

## Comet ML Integration

All experiments are automatically tracked in Comet ML for:
- Experiment comparison across models
- Metric visualization and analysis
- Reproducibility and version control
- Confusion matrix visualization

Access your experiments at: `https://www.comet.com/<your-workspace>/testing`

## Extending the Dataset

Current: 23 test cases
Target: 100 test cases in batches of 20

To generate more test cases:
1. Edit `src/data_generation/generate_dataset.py`
2. Add new test cases following the existing patterns
3. Ensure balanced distribution across validity ratings
4. Run `python -m src.data_generation.generate_dataset`

## Key Design Principles

1. **Objective Ground Truth**: Test cases use verifiable facts (mathematical, historical, temporal)
2. **No LLM-Generated Ground Truth**: Avoids circular dependency in evaluation
3. **Standard Classification Metrics**: Uses industry-standard precision/recall/F1
4. **Dual Assessment**: Evaluates BOTH reliability and validity (not just one)
5. **Strict Scoring**: Only counts as correct if BOTH dimensions are accurate
