# Core Metrics - Overall Performance Indicators

## 📊 Overview
Core metrics provide high-level assessment of model performance across the A1Facts benchmark. These are the primary metrics for deployment decisions and model comparison.

---

## 🎯 Strict Accuracy
**Formula**: `correct_cases / total_cases`  
**Range**: 0.0 - 1.0 (0% - 100%)

### What It Measures
The percentage of test cases where the model gets **BOTH** reliability assessment **AND** validity determination completely correct.

### Why It Matters
- **Most important metric** for deployment readiness
- Reflects real-world performance where partial answers aren't useful
- Conservative estimate - if this is high, the model is robust

### Interpretation Guidelines
| Score | Interpretation | Business Decision |
|-------|---------------|-------------------|
| **≥85%** | Excellent - Production ready |  Deploy with confidence |
| **70-84%** | Good - Consider deployment |  Deploy with monitoring |
| **55-69%** | Fair - Needs improvement |  Require additional training |
| **<55%** | Poor - Not deployment ready |  Significant issues to address |

### Example
```
strict_accuracy: 0.7239 (72.39%)
```
**Meaning**: Model got both reliability and validity completely correct on 72.39% of test cases.

**Business Impact**: Good performance, consider deployment with monitoring systems in place.

---

## 🔍 Reliability Accuracy
**Formula**: `correct_reliability_predictions / total_reliability_predictions`  
**Range**: 0.0 - 1.0 (0% - 100%)

### What It Measures
How accurately the model assesses the quality/trustworthiness of information sources using the A-F reliability scale.

### Why It Matters
- Critical for information verification
- Determines if users can trust the model's source assessment
- Foundation for all triangulation logic

### A-F Reliability Scale
- **A**: Peer-reviewed, authoritative sources
- **B**: Reputable, well-established sources  
- **C**: Generally reliable sources
- **D**: Questionable reliability
- **E**: Poor reliability
- **F**: Unreliable, discredited sources

### Interpretation Guidelines
| Score | Interpretation | Impact |
|-------|---------------|---------|
| **≥88%** | Excellent source assessment | High trust in model's source evaluation |
| **78-87%** | Good source discrimination | Reliable for most applications |
| **68-77%** | Fair source evaluation | Use with caution, validate critical sources |
| **<68%** | Poor source assessment | Cannot trust source reliability judgments |

### Dataset-Specific Expectations
- **Manual Dataset**: Should be highest (≥85%) - foundation skill
- **Coverage Dataset**: Should be strong (≥80%) - triangulation base
- **Synthesis Dataset**: May be lower (≥75%) - complex scenarios

---

##  Validity Accuracy  
**Formula**: `correct_validity_predictions / total_validity_predictions`  
**Range**: 0.0 - 1.0 (0% - 100%)

### What It Measures
How accurately the model determines information confidence using the 1-6 validity scale after triangulating sources.

### Why It Matters
- Determines confidence in final conclusions
- Critical for decision-making applications
- Shows reasoning sophistication

### 1-6 Validity Scale
- **6**: Extremely high confidence (multiple A-tier sources agree)
- **5**: High confidence (strong consensus)
- **4**: Moderate confidence (good evidence)
- **3**: Some confidence (limited evidence)
- **2**: Low confidence (weak/mixed evidence)
- **1**: Very low confidence (poor/contradictory evidence)

### Interpretation Guidelines
| Score | Interpretation | Decision Confidence |
|-------|---------------|-------------------|
| **≥85%** | Excellent confidence assessment | Trust model's confidence levels |
| **75-84%** | Good confidence calibration | Generally reliable confidence |
| **65-74%** | Fair confidence determination | Validate high-stakes decisions |
| **<65%** | Poor confidence assessment | Cannot trust confidence levels |

### Dataset-Specific Patterns
- **Manual Dataset**: Often high due to single-source simplicity
- **Coverage Dataset**: Tests systematic confidence across patterns
- **Synthesis Dataset**: Most challenging due to complex reasoning

---

##  Total Cases
**Value**: Integer count

### What It Measures
Number of test cases evaluated in the dataset.

### Why It Matters
- Provides context for statistical significance
- Helps interpret performance reliability
- Different datasets have different case counts

### Dataset Sizes
- **Manual Dataset**: 300 cases (foundation skills)
- **Coverage Dataset**: 134 cases (triangulation patterns)
- **Synthesis Dataset**: 100 cases (advanced reasoning)

### Statistical Significance
| Cases | Confidence | Notes |
|-------|------------|-------|
| **≥100** | High | Statistically robust |
| **50-99** | Medium | Generally reliable |
| **<50** | Low | May be noisy |

---

##  Performance Targets by Dataset

### Manual Dataset (Foundation)
- **Strict Accuracy**: ≥82% (foundation requirement)
- **Reliability Accuracy**: ≥85% (core skill)
- **Validity Accuracy**: ≥87% (decision-making)

### Coverage Dataset (Patterns)
- **Strict Accuracy**: ≥75% (systematic performance)
- **Reliability Accuracy**: ≥80% (multi-source handling)
- **Validity Accuracy**: ≥78% (pattern-based confidence)

### Synthesis Dataset (Reasoning)
- **Strict Accuracy**: ≥68% (complex scenarios)
- **Reliability Accuracy**: ≥75% (sophisticated assessment)
- **Validity Accuracy**: ≥73% (advanced reasoning)

---

##  Using Core Metrics for Decisions

### Deployment Readiness Assessment
1. **Check strict accuracy** against dataset-specific targets
2. **Verify reliability accuracy** meets minimum thresholds
3. **Confirm validity accuracy** supports decision-making needs

### Model Comparison
1. **Primary sort**: Strict accuracy (most important)
2. **Secondary sort**: Reliability accuracy (foundation skill)
3. **Tertiary sort**: Validity accuracy (reasoning quality)

### Red Flags
-  **Strict accuracy < 50%**: Model fundamentally broken
-  **Reliability accuracy < validity accuracy**: Source assessment issues
-  **Large accuracy drops between datasets**: Generalization problems