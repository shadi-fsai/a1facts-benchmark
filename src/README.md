# A1Facts Triangulation Benchmark

This benchmark evaluates how well different LLMs can perform the core triangulation tasks that power A1Facts knowledge acquisition:

1. **Source Reliability Assessment** (A-F scale)
2. **Information Validity Assessment** (1-6 scale)

## Purpose

A1Facts claims to solve LLM hallucination through intelligent triangulation of multiple sources. This benchmark validates whether LLMs can reliably:
- Assess web source credibility
- Identify logical contradictions
- Triangulate information across multiple sources
- Make validity judgments based on source agreement

## Models Tested

- OpenAI GPT-4o
- OpenAI O3 (when available)
- Anthropic Claude 3.5 Sonnet
- Google Gemini 2.5 Pro
- Open source models (Llama, Mistral)

## Project Structure

```
benchmark/
├── src/
│   ├── data_generation/     # Dataset creation scripts
│   ├── evaluation/          # Evaluation pipeline
│   └── models/              # Model wrappers
├── datasets/                # Test case datasets
├── experiments/             # Comet experiment logs
├── results/                 # Evaluation results
└── notebooks/               # Analysis notebooks
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Add your API keys to .env

# Generate dataset
python -m src.data_generation.generate_dataset

# Run evaluation
python -m src.evaluation.run_benchmark --models gpt-4o,claude-3.5-sonnet

# View results
python -m src.evaluation.analyze_results
```

## Dataset

The benchmark uses objectively verifiable test cases across 6 validity categories:

- **Rating 1 (Confirmed)**: Multiple independent sources agree
- **Rating 2 (Probably True)**: Logical consistency across sources
- **Rating 3 (Possibly True)**: Plausible but weak corroboration
- **Rating 4 (Doubtful)**: Contradictions or logical issues
- **Rating 5 (Improbable)**: Clear contradictions/impossibilities
- **Rating 6 (Cannot Judge)**: Insufficient/unrelated information

## Metrics

- F1-score per validity class
- Overall accuracy
- Precision/Recall per class
- Confusion matrices
- Domain-specific performance

## Comet Integration

All experiments are tracked in Comet for reproducibility and comparison.
