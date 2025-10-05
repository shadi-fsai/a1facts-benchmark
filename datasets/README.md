# Datasets

This directory contains the test case datasets for A1Facts triangulation evaluation.

## Dataset Format

Each test case contains:
- `id`: Unique identifier
- `category`: Domain category (medical, financial, etc.)
- `sources`: List of source claims with URLs
- `expected_reliability_scores`: Ground truth reliability ratings (A-F)
- `expected_validity`: Ground truth validity rating (1-6)
- `reasoning`: Explanation of ground truth rating

## Validity Ratings

1. **Confirmed**: Multiple independent, reliable sources agree
2. **Probably True**: Logical and consistent, not fully corroborated
3. **Possibly True**: Plausible but lacks strong corroboration
4. **Doubtful**: Not logical or contradicted
5. **Improbable**: Illogical and contradicted, or impossible
6. **Cannot Judge**: Insufficient or unrelated information

## Generating Datasets

```bash
cd src/data_generation
python generate_dataset.py
```

This will create `triangulation_benchmark_v1.json` with test cases across all validity categories.
