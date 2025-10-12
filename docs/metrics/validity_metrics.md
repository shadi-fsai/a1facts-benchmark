# Validity Metrics - Information Confidence Determination

## 📊 Overview
Validity metrics measure how well the model determines the appropriate confidence level for information after triangulating multiple sources. This represents the final "answer confidence" that users will rely on for decisions.

---

## 🎯 Validity Macro F1
**Formula**: `average(f1_scores_for_validity_ratings_1_through_6)`  
**Range**: 0.0 - 1.0

### What It Measures
Average F1 score across all validity confidence levels (1-6), giving equal weight to each confidence level.

### Why It Matters
- **Balanced confidence calibration** across the full spectrum
- More robust than accuracy (handles different confidence distributions)
- Critical for users to trust the model's confidence assessments

### Interpretation Guidelines
| Score | Interpretation | Confidence Calibration Quality |
|-------|---------------|--------------------------------|
| **≥0.80** | Excellent | Well-calibrated confidence across all levels |
| **0.70-0.79** | Good | Generally reliable confidence assessment |
| **0.60-0.69** | Fair | Decent but inconsistent confidence |
| **<0.60** | Poor | Cannot trust model's confidence levels |

### Example
```
validity_macro_f1: 0.742
```
**Meaning**: Average F1 performance of 74.2% across all validity confidence levels (1-6).

---

## 🔥 Validity 2 F1 Score
**Formula**: `2 * (precision_2 * recall_2) / (precision_2 + recall_2)`  
**Range**: 0.0 - 1.0

### What It Measures
Performance on **Validity Level 2** - "Low confidence, weak/mixed evidence" - the most common triangulation outcome.

### Why It Matters
- **Most frequent validity level** in real-world triangulation (40-50% of cases)
- Represents challenging scenarios where sources provide mixed signals
- Critical for practical deployment success

### When Validity 2 Occurs
- Sources provide contradictory information
- Mix of reliable and unreliable sources
- Limited evidence available
- Sources agree but have reliability concerns

### Interpretation Guidelines
| Score | Interpretation | Practical Impact |
|-------|---------------|------------------|
| **≥0.80** | Excellent | Correctly identifies mixed/weak evidence scenarios |
| **0.70-0.79** | Good | Generally handles uncertain cases well |
| **0.60-0.69** | Fair | May over/under-confidence mixed evidence |
| **<0.60** | Poor | Cannot handle most real-world uncertainty |

### Dataset-Specific Importance
- **Coverage Dataset**: Critical - systematic pattern testing
- **Synthesis Dataset**: Highest importance - 63% of cases are Validity 2
- **Manual Dataset**: Less common but still important baseline

---

## 🏆 Validity 1 F1 Score (Very Low Confidence)
**Formula**: `2 * (precision_1 * recall_1) / (precision_1 + recall_1)`

### What It Measures
Performance on **Validity Level 1** - "Very low confidence, poor/contradictory evidence."

### Why It Matters
- **Safety critical** - must recognize when information is unreliable
- Prevents overconfident decisions based on poor evidence
- Protects users from acting on contradictory information

### When Validity 1 Occurs
- Multiple sources directly contradict each other
- Only F-tier (unreliable) sources available
- No credible evidence supporting the claim
- Evidence strongly suggests information is false

### Interpretation Guidelines
| Score | Interpretation | Safety Impact |
|-------|---------------|---------------|
| **≥0.75** | Excellent | Reliably warns users about poor information |
| **0.65-0.74** | Good | Generally catches bad information |
| **0.55-0.64** | Fair | May miss some problematic cases |
| **<0.55** | Poor | Dangerous - may provide false confidence |

---

## 🎯 Validity 6 F1 Score (Extremely High Confidence)
**Formula**: `2 * (precision_6 * recall_6) / (precision_6 + recall_6)`

### What It Measures
Performance on **Validity Level 6** - "Extremely high confidence, multiple A-tier sources agree."

### Why It Matters
- **Premium confidence detection** - when evidence is strongest
- Enables high-confidence decision-making
- Represents best-case triangulation scenarios

### When Validity 6 Occurs
- Multiple A-tier sources provide identical information
- Consensus across different types of authoritative sources
- Strong peer-reviewed evidence with replication
- Official confirmations from multiple authorities

### Interpretation Guidelines
| Score | Interpretation | Decision Support |
|-------|---------------|------------------|
| **≥0.85** | Excellent | Correctly identifies strongest evidence |
| **0.75-0.84** | Good | Generally recognizes high-quality consensus |
| **0.65-0.74** | Fair | May under-confidence strong evidence |
| **<0.65** | Poor | Misses opportunities for high-confidence decisions |

### Business Impact
- **High Validity 6 F1**: Users can act decisively on model's highest confidence
- **Low Validity 6 F1**: Users must be more cautious even with "high confidence"

---

## 📊 Validity Levels Overview

### Complete Confidence Spectrum

#### **Validity 6: Extremely High Confidence**
- **Target F1**: ≥0.80
- **Frequency**: Rare (5-10% of cases)
- **Business use**: Decisive action, high-stakes decisions

#### **Validity 5: High Confidence**  
- **Target F1**: ≥0.75
- **Frequency**: Uncommon (10-15% of cases)
- **Business use**: Confident decisions, planning

#### **Validity 4: Moderate Confidence**
- **Target F1**: ≥0.70
- **Frequency**: Common (20-25% of cases)  
- **Business use**: Proceed with caution, monitor

#### **Validity 3: Some Confidence**
- **Target F1**: ≥0.70
- **Frequency**: Common (15-20% of cases)
- **Business use**: Tentative action, seek more evidence

#### **Validity 2: Low Confidence** 
- **Target F1**: ≥0.72 (most important)
- **Frequency**: Most common (40-50% of cases)
- **Business use**: High caution, additional verification needed

#### **Validity 1: Very Low Confidence**
- **Target F1**: ≥0.70 (safety critical)
- **Frequency**: Uncommon (5-10% of cases)
- **Business use**: Avoid action, seek alternative evidence

---

## 🎯 Advanced Validity Metrics

### Validity 3 F1 Score (Some Confidence)
**Importance**: Medium-high  
**Target**: ≥0.70  
**Use case**: Moderate evidence scenarios, tentative decisions

### Validity 4 F1 Score (Moderate Confidence)  
**Importance**: High  
**Target**: ≥0.70  
**Use case**: Balanced evidence, standard business decisions

### Validity 5 F1 Score (High Confidence)
**Importance**: Medium  
**Target**: ≥0.75  
**Use case**: Strong evidence, confident action

---

## 🏢 Business Applications by Validity Level

### Medical/Healthcare Applications
- **Focus**: High Validity 1 F1 (safety), High Validity 5-6 F1 (treatment confidence)
- **Critical threshold**: Validity 1 F1 ≥ 0.80 (patient safety)

### Financial Decision Support
- **Focus**: High Validity 4-5 F1 (investment decisions)  
- **Critical threshold**: Validity 2 F1 ≥ 0.75 (risk management)

### Legal Research
- **Focus**: High Validity 5-6 F1 (precedent confidence)
- **Critical threshold**: Validity 1 F1 ≥ 0.75 (avoid bad precedents)

### General Business Intelligence
- **Focus**: High Validity 2-4 F1 (everyday decisions)
- **Critical threshold**: Validity 2 F1 ≥ 0.70 (practical deployment)

---

## 🚨 Red Flags in Validity Metrics

### Pattern: High Validity 6 F1, Low Validity 1 F1
**Problem**: Model overconfident - doesn't recognize poor evidence  
**Risk**: Users make bad decisions thinking they have good evidence  
**Action**: Improve detection of contradictory/poor evidence

### Pattern: Low Validity 2 F1 Compared to Others
**Problem**: Poor handling of most common scenario  
**Risk**: Poor practical performance despite good overall accuracy  
**Action**: Focus training on mixed/uncertain evidence scenarios

### Pattern: Very Uneven F1 Scores Across Validity Levels
**Problem**: Model has learned biases toward certain confidence levels  
**Risk**: Miscalibrated confidence in deployment  
**Action**: Rebalance training data, improve confidence calibration

### Pattern: Validity Accuracy >> Validity Macro F1
**Problem**: Performance driven by dominant classes  
**Risk**: Poor performance on minority confidence levels  
**Action**: Check individual validity level performance

---

## 📈 Performance Benchmarks

### By Application Risk Level

#### **High-Risk Applications** (Medical, Legal, Safety)
- Validity Macro F1: ≥0.80
- Validity 1 F1: ≥0.80 (safety critical)
- Validity 2 F1: ≥0.75 (uncertainty handling)
- Validity 6 F1: ≥0.85 (high-confidence decisions)

#### **Medium-Risk Applications** (Business, Finance)
- Validity Macro F1: ≥0.75
- Validity 1 F1: ≥0.70
- Validity 2 F1: ≥0.72
- Validity 6 F1: ≥0.80

#### **Low-Risk Applications** (Research, Exploration)
- Validity Macro F1: ≥0.65
- Validity 1 F1: ≥0.65
- Validity 2 F1: ≥0.68
- Validity 6 F1: ≥0.75

### By Dataset Type

#### **Manual Dataset** (Foundation)
- Higher Validity 4-6 F1 expected (simpler single-source scenarios)
- Validity 2 F1: ≥0.75

#### **Coverage Dataset** (Systematic)
- Balanced performance across all levels expected
- Validity 2 F1: ≥0.72 (systematic testing)

#### **Synthesis Dataset** (Advanced)
- Lower overall F1 acceptable (complex reasoning)
- Validity 2 F1: ≥0.70 (most challenging scenarios)