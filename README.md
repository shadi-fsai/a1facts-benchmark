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

Current benchmark tests multiple model families:

**OpenAI Models:**
- GPT-4o
- GPT-4o-mini
- GPT-4-turbo
- GPT-3.5-turbo

**Google Gemini Models:**
- Gemini-2.5-pro
- Gemini-2.5-flash
- Gemini-2.0-flash
- Gemini-flash

## Key Findings

**Best Model**: **Gemini-2.5-pro** (20.1% strict accuracy)  
**Challenge**: Both validity AND reliability must be correct simultaneously  
**Critical Gap**: Grade C reliability completely undetected by ALL models  
**Insight**: Models stronger at reliability assessment than validity assessment  

## Model Performance Rankings

### Strict Accuracy Rankings
*Both validity AND reliability must be correct*

| Rank | Model | Strict Accuracy | Validity Accuracy | Reliability Accuracy |
|------|-------|-----------------|-------------------|----------------------|
| 1st  | gemini-2.5-pro | 20.1% | 60.8% | 77.0% |
| 2nd  | gpt-4o | 23.9% | 38.8% | 64.2% |
| 3rd  | gemini-flash | 23.1% | 44.0% | 73.4% |
| 4th  | gpt-4-turbo | 17.2% | 39.6% | 62.5% |
| 5th  | gpt-4o-mini | 15.7% | 26.9% | 60.0% |
| 6th  | gemini-2.5-flash | 14.9% | 42.3% | 62.9% |
| 7th  | gemini-2.0-flash | 5.2% | 59.1% | 63.6% |

### Performance by Validity Level

| Validity Level | Best F1 Score | Best Model | Pattern |
|----------------|---------------|------------|---------|
| 1 (Confirmed) | 85.7% | gemini-2.5-pro | Strong |
| 2 (Probably) | 47.8% | gemini-flash | Moderate |
| 3 (Possibly) | 44.7% | gemini-2.5-flash | Moderate |
| 4 (Doubtful) | 33.0% | gpt-4-turbo | Weak |
| 5 (Improbable) | 50.0% | gpt-4-turbo | Moderate |
| 6 (Cannot Judge) | 53.7% | gemini-flash | Moderate |

### Performance by Reliability Grade

| Reliability Grade | Best F1 Score | Best Model | Pattern |
|-------------------|---------------|------------|---------|
| A (Reliable) | 63.2% | gemini-2.5-pro | Strong |
| B (Usually) | 17.3% | gpt-4-turbo | Critical |
| C (Fairly) | 0.0% | ALL MODELS | FAILURE |
| D (Not Usually) | 52.5% | gemini-2.5-pro | Moderate |
| E (Unreliable) | 64.4% | gemini-2.5-pro | Strong |
| F (Cannot Judge) | 52.6% | gemini-2.5-pro | Moderate |

## Datasets

| Dataset | Cases | Description |
|---------|-------|-------------|
| **Manual 300** | 300 | High-quality curated cases, balanced reliability grades A-F |
| **Triangulation 134** | 134 | Multi-source triangulation scenarios with contradictions |
| **Synthesis 100** | 100 | Synthetic edge cases and controlled conditions |
| **Total** | **534** | **Comprehensive evaluation coverage** |

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
├── datasets/                # Test case datasets
│   ├── triangulation_benchmark_v1.json
│   ├── a1facts_manual_300_cases.json
│   └── triangulation_synthesis_benchmark_v1.json
├── results/                 # Evaluation results (JSON)
├── visualizations/          # Generated charts and analysis
└── .env                     # API keys configuration
```

## Quick Start

### 1. Install Dependencies
```bash
cd c:\a1facts-benchmark
pip install -r requirements.txt
```

### 2. Configure API Keys
```bash
# Edit .env file and add your API keys
OPENAI_API_KEY=sk-proj-...
GOOGLE_API_KEY=your-gemini-key-here
COMET_API_KEY=your-comet-key-here  # Optional
COMET_WORKSPACE=your-username
```

### 3. Run the Benchmark
```bash
# Run all models on all datasets
python -m src.evaluation.run_benchmark --dataset all --models all --metrics all

# Run specific models on manual dataset  
python -m src.evaluation.run_benchmark \
  --dataset datasets/a1facts_manual_300_cases.json \
  --models gpt-4-turbo gemini-2.5-flash gemini-2.5-pro \
  --metrics all
```

## Rating Scales

### Validity Scale (1-6)

| Rating | Label | Description | Example |
|--------|-------|-------------|---------|
| **1** | **Confirmed** | Multiple reliable sources agree | "Diabetes affects 11.3% of US adults" (NIH, CDC, WHO) |
| **2** | **Probably True** | Logical and consistent | Market reactions matching known events |  
| **3** | **Possibly True** | Plausible but limited corroboration | Medical correlations from preliminary studies |
| **4** | **Doubtful** | Contradicted by other information | Claims opposing established facts |
| **5** | **Improbable** | Illogical, multiple contradictions | Mathematical impossibilities |
| **6** | **Cannot Judge** | Insufficient/unrelated information | Missing context, irrelevant sources |

### Reliability Scale (A-F)

| Grade | Label | Description | Example Sources |
|-------|-------|-------------|-----------------|
| **A** | **Completely Reliable** | Government agencies, peer-reviewed | NIH, CDC, Nature, Science |
| **B** | **Usually Reliable** | Major news, reputable institutions | Reuters, Bloomberg, Mayo Clinic |
| **C** | **Fairly Reliable** | Established but some concerns | WebMD, Wikipedia, trade publications |
| **D** | **Not Usually Reliable** | Blogs, opinion sites | Personal blogs, unverified sources |
| **E** | **Unreliable** | Known for misinformation | Conspiracy sites, debunked sources |
| **F** | **Cannot Judge** | Unknown domains | Insufficient information to assess |

## Evaluation Metrics

The benchmark calculates **57 total metrics** across three categories:

### Validity Assessment Metrics (27)
- Overall accuracy and macro F1-score
- Per-rating (1-6) metrics:
  - Precision: Of predictions for this rating, how many were correct?
  - Recall: Of actual cases with this rating, how many were found?
  - F1-score: Harmonic mean of precision and recall
  - Support: Number of test cases with this rating
- Confusion matrix: 6×6 matrix showing prediction patterns

### Reliability Assessment Metrics (27)
- Overall accuracy and macro F1-score
- Per-rating (A-F) metrics:
  - Precision: Of predictions for this rating, how many were correct?
  - Recall: Of actual sources with this rating, how many were found?
  - F1-score: Harmonic mean of precision and recall
  - Support: Number of sources with this rating
- Confusion matrix: 6×6 matrix showing prediction patterns

### Overall Metrics (3)
- **Strict accuracy**: Both validity AND all reliability scores must be correct
- Correct count
- Total test cases

## Results & Visualizations

All evaluation results and analysis are available in:

**Results:**
- `results/evaluation_results_<timestamp>.json` - Complete model performance data
- `results/manual_300_evaluation_summary.md` - Detailed analysis report

**Visualizations:**
- `visualizations/model_rankings.png` - Performance comparison charts
- `visualizations/comprehensive_dashboard.html` - Interactive analysis dashboard
- `visualizations/manual_300_*.png` - Dataset-specific analysis charts

## Dataset-Specific Analysis

Each dataset serves a unique analytical purpose requiring different evaluation focus:

| Dataset | Cases | Primary Focus | Critical Insight |
|---------|-------|---------------|------------------|
| **Manual (300)** | 300 | **Strict Accuracy** | Grade C Reliability: 0% (complete failure) |
| **Triangulation (134)** | 134 | **Relative Accuracy** | Models stronger at reliability than validity |
| **Synthesis (100)** | 100 | **Reasoning Quality** | Synthesis quality varies significantly |

## Comet ML Integration

All experiments are automatically tracked in Comet ML for:
- Experiment comparison across models
- Metric visualization and analysis
- Reproducibility and version control
- Confusion matrix visualization

Access your experiments at: `https://www.comet.com/<your-workspace>/testing`

## Key Design Principles

1. **Objective Ground Truth**: Test cases use verifiable facts (mathematical, historical, temporal)
2. **No LLM-Generated Ground Truth**: Avoids circular dependency in evaluation
3. **Standard Classification Metrics**: Uses industry-standard precision/recall/F1
4. **Dual Assessment**: Evaluates BOTH reliability and validity (not just one)
5. **Strict Scoring**: Only counts as correct if BOTH dimensions are accurate