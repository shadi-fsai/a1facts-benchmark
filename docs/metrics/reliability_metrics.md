# Reliability Metrics - Source Quality Assessment

## 📊 Overview
Reliability metrics measure how well the model evaluates the quality and trustworthiness of information sources. These metrics are fundamental to all A1Facts triangulation capabilities.

---

## 🔍 Reliability Macro F1
**Formula**: `average(f1_scores_for_all_reliability_ratings)`  
**Range**: 0.0 - 1.0

### What It Measures
Average F1 score across all reliability ratings (A, B, C, D, E, F), giving equal weight to each rating level.

### Why It Matters
- **Balanced assessment** of performance across all source quality levels
- More robust than accuracy alone (handles class imbalance)
- Critical for deployment where you need consistent source evaluation

### Interpretation Guidelines
| Score | Interpretation | Source Assessment Quality |
|-------|---------------|---------------------------|
| **≥0.85** | Excellent | Consistently identifies all source quality levels |
| **0.75-0.84** | Good | Reliable source assessment with minor gaps |
| **0.65-0.74** | Fair | Decent performance but inconsistent on some levels |
| **<0.65** | Poor | Cannot reliably assess source quality |

### Example
```
reliability_macro_f1: 0.773
```
**Meaning**: Average F1 performance of 77.3% across all reliability ratings (A-F).

---

## 🏆 Reliability A F1 Score
**Formula**: `2 * (precision_A * recall_A) / (precision_A + recall_A)`  
**Range**: 0.0 - 1.0

### What It Measures
How well the model identifies and correctly classifies **A-tier sources** (highest quality: peer-reviewed, authoritative).

### Why It Matters
- **Most critical reliability metric** - A-tier sources are foundation of trust
- High-stakes decisions depend on correctly identifying premium sources
- Poor A-tier detection = cannot trust model for important decisions

### A-Tier Source Characteristics
- Peer-reviewed academic papers
- Government agency reports
- Established medical/scientific institutions
- Authoritative regulatory bodies

### Interpretation Guidelines
| Score | Interpretation | Business Impact |
|-------|---------------|-----------------|
| **≥0.90** | Excellent | Can trust model to identify premium sources |
| **0.80-0.89** | Good | Generally reliable A-tier detection |
| **0.70-0.79** | Fair | May miss some premium sources |
| **<0.70** | Poor | Cannot reliably identify highest-quality sources |

### Dataset-Specific Expectations
- **Manual Dataset**: ≥0.85 (foundation requirement)
- **Coverage Dataset**: ≥0.85 (triangulation base)
- **Synthesis Dataset**: ≥0.80 (complex scenarios may be harder)

---

## ⚠️ Reliability F F1 Score
**Formula**: `2 * (precision_F * recall_F) / (precision_F + recall_F)`  
**Range**: 0.0 - 1.0

### What It Measures
How well the model identifies and correctly classifies **F-tier sources** (lowest quality: unreliable, discredited).

### Why It Matters
- **Critical for safety** - must detect unreliable sources
- Prevents dangerous misinformation from being trusted
- Protects users from poor decision-making based on bad sources

### F-Tier Source Characteristics
- Discredited publications
- Conspiracy theory websites
- Fraudulent or retracted studies
- Biased advocacy without evidence
- Anonymous or unverifiable sources

### Interpretation Guidelines
| Score | Interpretation | Safety Impact |
|-------|---------------|---------------|
| **≥0.80** | Excellent | Reliably filters out bad sources |
| **0.70-0.79** | Good | Generally catches unreliable sources |
| **0.60-0.69** | Fair | May let some bad sources through |
| **<0.60** | Poor | Dangerous - cannot filter unreliable sources |

### Critical Thresholds
- **Minimum for deployment**: 0.70 (catches most bad sources)
- **Recommended for safety**: 0.75 (high confidence in filtering)
- **Gold standard**: 0.80+ (excellent protection)

---

## 📊 Per-Rating Reliability Metrics

### Reliability B-F Individual F1 Scores
Each reliability rating (B, C, D, E, F) has individual precision, recall, and F1 metrics.

#### **Reliability B F1** (Reputable sources)
- **Target**: ≥0.75
- **Importance**: High - these are commonly used quality sources
- **Examples**: Established news organizations, reputable companies

#### **Reliability C F1** (Generally reliable)
- **Target**: ≥0.70  
- **Importance**: Medium - everyday reliable sources
- **Examples**: Local government, established organizations

#### **Reliability D F1** (Questionable)
- **Target**: ≥0.65
- **Importance**: Medium - important to flag concerns
- **Examples**: Sources with some issues, outdated information

#### **Reliability E F1** (Poor reliability)
- **Target**: ≥0.60
- **Importance**: High - must identify problematic sources  
- **Examples**: Biased sources, poor methodology

---

## 🎯 Precision vs Recall Trade-offs

### High Precision, Lower Recall
- **Good for**: Conservative applications where false positives are costly
- **Risk**: May miss some sources of that quality level
- **Use case**: Medical/legal applications

### High Recall, Lower Precision  
- **Good for**: Comprehensive detection where false negatives are costly
- **Risk**: May over-classify sources to that level
- **Use case**: Research/exploration applications

### Balanced F1 (Recommended)
- **Best overall measure** for most applications
- **Balances** both precision and recall concerns
- **Most interpretable** single metric per rating

---

## 🏢 Business Applications

### Content Moderation
- **Focus**: High F-tier F1 (filter bad sources)
- **Minimum**: F-tier F1 ≥ 0.75
- **Goal**: Protect users from misinformation

### Research Applications
- **Focus**: High A-tier F1 (find premium sources)  
- **Minimum**: A-tier F1 ≥ 0.85
- **Goal**: Identify highest-quality evidence

### General Decision Support
- **Focus**: Balanced macro F1 (consistent across all levels)
- **Minimum**: Macro F1 ≥ 0.75
- **Goal**: Reliable source assessment for all decisions

### News/Media Applications
- **Focus**: B-tier and C-tier F1 (everyday sources)
- **Minimum**: B-tier F1 ≥ 0.80, C-tier F1 ≥ 0.75
- **Goal**: Accurately assess common news sources

---

## 🚨 Red Flags in Reliability Metrics

### Pattern: High A-tier, Low F-tier F1
**Problem**: Model can identify good sources but not bad ones  
**Risk**: Users exposed to misinformation  
**Action**: Focus training on identifying unreliable sources

### Pattern: Very High F1 for Some Ratings, Very Low for Others
**Problem**: Model is inconsistent across source quality spectrum  
**Risk**: Unpredictable performance in deployment  
**Action**: Balance training data across all reliability levels

### Pattern: Reliability Accuracy > Reliability Macro F1 by >10%
**Problem**: Performance skewed by dominant classes  
**Risk**: Poor performance on minority source types  
**Action**: Check individual class performance, rebalance if needed

---

## 📈 Performance Benchmarks

### By Model Capability Level

#### **Basic Model** (Minimum viable)
- Reliability Macro F1: ≥0.65
- A-tier F1: ≥0.70
- F-tier F1: ≥0.65

#### **Production Model** (Deployment ready)
- Reliability Macro F1: ≥0.75
- A-tier F1: ≥0.80
- F-tier F1: ≥0.75

#### **Advanced Model** (High performance)
- Reliability Macro F1: ≥0.85
- A-tier F1: ≥0.90
- F-tier F1: ≥0.85

### By Dataset Type

#### **Manual Dataset** (Foundation)
- Higher expectations - single source assessment should be mastered
- A-tier F1: ≥0.85, F-tier F1: ≥0.80

#### **Coverage Dataset** (Patterns)
- Standard expectations - systematic multi-source assessment
- A-tier F1: ≥0.80, F-tier F1: ≥0.75

#### **Synthesis Dataset** (Complex)
- Slightly lower expectations - focus on reasoning over source assessment
- A-tier F1: ≥0.75, F-tier F1: ≥0.70