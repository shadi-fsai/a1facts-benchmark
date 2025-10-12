# Tier Definitions - Dataset-Specific Metric Hierarchies

## 📊 Overview
Each dataset has three tiers of metrics based on importance for decision-making. This tiered approach allows focused evaluation depending on your needs and time constraints.

---

## 🎯 Tier Philosophy

### **Tier 1: Critical Metrics** 
- **Purpose**: Go/No-Go deployment decisions
- **Time**: Quick assessment (5-10 minutes)
- **Audience**: Executives, product managers
- **Question**: "Is this model ready for deployment?"

### **Tier 2: Diagnostic Metrics**
- **Purpose**: Performance analysis and improvement planning  
- **Time**: Standard evaluation (15-20 minutes)
- **Audience**: ML engineers, researchers
- **Question**: "Where does this model need improvement?"

### **Tier 3: Analytical Metrics**
- **Purpose**: Deep research, optimization, academic analysis
- **Time**: Comprehensive analysis (30+ minutes)
- **Audience**: Researchers, model developers
- **Question**: "How does this model perform in fine detail?"

---

# 📋 Manual Dataset (Foundation Skills) - 300 Cases

**Purpose**: Single-source reliability and validity assessment  
**Focus**: Foundation AI capabilities for basic information evaluation

## 🎯 Tier 1: Critical Foundation Metrics (4 metrics)

### Core Decision Metrics
- **`strict_accuracy`** - Gets both reliability AND validity correct
  - **Target**: ≥82%
  - **Why critical**: Overall deployment readiness
  
- **`reliability_accuracy`** - Can it assess individual source quality?
  - **Target**: ≥85%  
  - **Why critical**: Foundation of all information assessment

- **`validity_accuracy`** - Can it determine information confidence?
  - **Target**: ≥87%
  - **Why critical**: Users need accurate confidence levels

- **`reliability_A_f1`** - Critical for identifying high-quality sources
  - **Target**: ≥0.85
  - **Why critical**: Premium source detection is essential

### Business Decision Framework
| All Tier 1 ≥ Targets | Decision |
|----------------------|----------|
| ✅ Yes | **Deploy** - Foundation skills confirmed |
| ❌ No | **Block** - Basic capabilities insufficient |

## 📈 Tier 2: Diagnostic Foundation Metrics (6 metrics)

### Performance Analysis
- **`reliability_F_f1`** - Can it detect unreliable sources?
  - **Target**: ≥0.75
  - **Diagnostic**: Safety and misinformation filtering

- **`validity_1_f1`** - High confidence detection
  - **Target**: ≥0.70
  - **Diagnostic**: Safety - recognizing poor evidence

- **`validity_6_f1`** - Low confidence detection  
  - **Target**: ≥0.65
  - **Diagnostic**: Premium confidence identification

- **`reliability_macro_f1`** - Overall reliability assessment balance
  - **Target**: ≥0.80
  - **Diagnostic**: Consistent performance across source types

- **`validity_macro_f1`** - Overall validity assessment balance
  - **Target**: ≥0.75
  - **Diagnostic**: Consistent confidence calibration

- **`total_cases`** - Error rate tracking and statistical power
  - **Value**: 300
  - **Diagnostic**: Sample size adequacy

### Improvement Planning
Focus areas identified by poor Tier 2 performance:
- Low `reliability_F_f1` → Improve bad source detection
- Low `validity_1_f1` → Improve safety mechanisms  
- Low macro F1s → Address class imbalance issues

## 🔬 Tier 3: Analytical Foundation Metrics (~20 metrics)

### Detailed Classification Performance
- **Per-reliability-rating precision/recall** (A, B, C, D, E, F)
  - 12 metrics: `reliability_X_precision`, `reliability_X_recall` 
  - **Purpose**: Fine-grained source assessment analysis

- **Per-validity-rating precision/recall** (1, 2, 3, 4, 5, 6)
  - 12 metrics: `validity_X_precision`, `validity_X_recall`
  - **Purpose**: Detailed confidence calibration analysis

- **Confusion matrices**
  - `reliability_confusion_matrix`, `validity_confusion_matrix`
  - **Purpose**: Error pattern analysis and improvement guidance

### Research Applications
- Model comparison across all performance dimensions
- Error analysis for targeted improvement
- Academic performance reporting
- Detailed ablation studies

---

# 🔺 Coverage Dataset (Triangulation Patterns) - 134 Cases

**Purpose**: Systematic multi-source triangulation across all reliability combinations  
**Focus**: Pattern recognition and systematic triangulation logic

## 🎯 Tier 1: Core Triangulation Metrics (5 metrics)

### Essential Triangulation Capabilities
- **`strict_accuracy`** - Complete triangulation success
  - **Target**: ≥75%
  - **Why critical**: Multi-source reasoning deployment readiness

- **`reliability_accuracy`** - Multi-source reliability assessment  
  - **Target**: ≥80%
  - **Why critical**: Foundation for triangulation logic

- **`validity_accuracy`** - Triangulated validity determination
  - **Target**: ≥78%
  - **Why critical**: Confidence after source integration

- **`reliability_A_f1`** - Premium source identification in patterns
  - **Target**: ≥0.85
  - **Why critical**: Must recognize quality sources in complex scenarios

- **`reliability_F_f1`** - Unreliable source detection in patterns
  - **Target**: ≥0.75
  - **Why critical**: Must filter bad sources in triangulation

### Business Decision Framework
| Tier 1 Performance | Decision |
|-------------------|----------|
| All ≥ targets | **Deploy** - Systematic triangulation ready |
| 4/5 ≥ targets | **Deploy with monitoring** - Strong but watch weak area |
| ≤3/5 ≥ targets | **Block** - Insufficient pattern recognition |

## 📈 Tier 2: Pattern Analysis Metrics (8 metrics)

### Triangulation Pattern Performance
- **`reliability_B_f1`, `reliability_C_f1`** - Mid-tier source handling
  - **Target**: ≥0.75 each
  - **Diagnostic**: Everyday source assessment in triangulation

- **`validity_2_f1`** - Most common triangulation outcome (mixed evidence)
  - **Target**: ≥0.75
  - **Diagnostic**: Critical - handles most real-world scenarios

- **`validity_3_f1`** - Moderate confidence scenarios
  - **Target**: ≥0.70
  - **Diagnostic**: Balanced evidence interpretation

- **`reliability_macro_f1`, `validity_macro_f1`** - Overall balance
  - **Target**: ≥0.75 each
  - **Diagnostic**: Consistent performance across patterns

- **`total_cases`** - Pattern coverage completeness
  - **Value**: 134 (covers all 19 systematic patterns)
  - **Diagnostic**: Comprehensive pattern testing

### Pattern-Specific Insights
Based on systematic reliability combinations:
- **High agreement patterns** (AAA, BBB): Should show high performance
- **Mixed patterns** (ABC, DEF): More challenging, lower performance expected
- **Low reliability patterns** (FFF, EEF): Safety-critical detection

## 🔬 Tier 3: Detailed Pattern Metrics (~25 metrics)

### Complete Pattern Analysis
- **All individual precision/recall metrics** for reliability (A-F) and validity (1-6)
- **Confusion matrices** showing exact error patterns
- **Per-pattern performance analysis** 
  - Performance on each of the 19 reliability combinations
  - Pattern complexity vs. performance relationships

### Advanced Triangulation Research
- **Pattern transition analysis** - how performance changes with complexity
- **Source combination effects** - interaction between different reliability levels
- **Triangulation logic validation** - detailed reasoning pattern analysis

---

# 🧠 Synthesis Dataset (Advanced Reasoning) - 100 Cases

**Purpose**: Complex triangulation logic and reasoning quality assessment  
**Focus**: Sophisticated AI reasoning in challenging real-world scenarios

## 🎯 Tier 1: Reasoning Excellence Metrics (6 metrics)

### Advanced Reasoning Capabilities
- **`strict_accuracy`** - Advanced triangulation success
  - **Target**: ≥68%
  - **Why critical**: Complex reasoning deployment readiness

- **`reliability_accuracy`** - Source quality in complex scenarios
  - **Target**: ≥75%
  - **Why critical**: Must maintain source assessment under complexity

- **`validity_accuracy`** - Confidence determination in conflicts
  - **Target**: ≥73%
  - **Why critical**: Reasoning-based confidence calibration

- **`validity_2_f1`** - Performance on most practical scenarios (63% of synthesis cases)
  - **Target**: ≥0.72
  - **Why critical**: Most common complex reasoning outcome

- **`reliability_A_f1`** - Premium source identification in complex logic
  - **Target**: ≥0.80
  - **Why critical**: Quality sources must be recognized in sophisticated scenarios

- **`reliability_F_f1`** - Bad source filtering with complex reasoning
  - **Target**: ≥0.70
  - **Why critical**: Safety even in sophisticated analysis

### Business Decision Framework
| Tier 1 Performance | Decision |
|-------------------|----------|
| All ≥ targets | **Deploy for advanced applications** - Sophisticated reasoning ready |
| 5/6 ≥ targets | **Deploy with expert oversight** - Strong but monitor weak area |
| ≤4/6 ≥ targets | **Block advanced deployment** - Insufficient reasoning capability |

## 📈 Tier 2: Advanced Capability Metrics (7 metrics)

### Sophisticated Reasoning Analysis
- **`validity_3_f1`** - Moderate confidence in complex scenarios
  - **Target**: ≥0.70
  - **Diagnostic**: Balanced reasoning under uncertainty

- **`validity_4_f1`** - Higher confidence reasoning
  - **Target**: ≥0.68
  - **Diagnostic**: Confident decisions in complex analysis

- **`reliability_B_f1`, `reliability_C_f1`** - Nuanced source assessment
  - **Target**: ≥0.70 each
  - **Diagnostic**: Sophisticated source quality evaluation

- **`reliability_macro_f1`, `validity_macro_f1`** - Overall reasoning balance
  - **Target**: ≥0.70 each
  - **Diagnostic**: Consistent sophisticated performance

- **`total_cases`** - Advanced reasoning sample size
  - **Value**: 100 (focus on quality over quantity)
  - **Diagnostic**: Sufficient for advanced reasoning assessment

### Reasoning Quality Indicators
- Complex scenario handling capability
- Conflict resolution in sophisticated contexts
- Methodological awareness in reasoning
- Uncertainty expression in complex analysis

## 🔬 Tier 3: Specialized Analysis Metrics (~15 metrics)

### Deep Reasoning Analysis
- **Complete precision/recall breakdown** for all reliability and validity levels
- **Reasoning component analysis**
  - Conflict resolution strategies
  - Source weighting logic
  - Methodological considerations
  - Uncertainty quantification

### Advanced Research Applications
- **Triangulation type performance** (agreement, majority, expert weighting, conflict resolution)
- **Domain-specific performance** (medical, technical, regulatory scenarios)
- **Reasoning sophistication metrics** (depth, logic chains, evidence integration)
- **Complex scenario benchmarking** against human expert performance

---

# 🎯 Usage Guidelines

## Quick Decision Making (Tier 1 Only)
```bash
python -m src.evaluation.run_benchmark --dataset [dataset] --metrics tier1
```
**Time**: 5-10 minutes  
**Decision**: Deploy or not?

## Standard Evaluation (Tier 1 + 2)
```bash
python -m src.evaluation.run_benchmark --dataset [dataset] --metrics tier2
```  
**Time**: 15-20 minutes  
**Decision**: Deploy + improvement areas

## Research Analysis (All Tiers)
```bash
python -m src.evaluation.run_benchmark --dataset [dataset] --metrics tier3
```
**Time**: 30+ minutes  
**Decision**: Complete performance understanding

## Model Comparison Strategy
1. **Start with Tier 1** across all models - identify top performers
2. **Use Tier 2** on top 2-3 models - understand trade-offs  
3. **Use Tier 3** on final candidate - validate deployment decision

---

# 📊 Cross-Dataset Comparison

## Progressive Capability Assessment
1. **Manual Dataset Tier 1** - Foundation skills verification
2. **Coverage Dataset Tier 1** - Systematic triangulation readiness  
3. **Synthesis Dataset Tier 1** - Advanced reasoning capability

## Deployment Readiness Matrix
| Manual T1 | Coverage T1 | Synthesis T1 | Deployment Recommendation |
|-----------|-------------|--------------|---------------------------|
| ✅ | ✅ | ✅ | **Full deployment** - All capabilities ready |
| ✅ | ✅ | ❌ | **Standard deployment** - Basic + systematic triangulation |
| ✅ | ❌ | ❌ | **Limited deployment** - Single-source applications only |
| ❌ | ❌ | ❌ | **No deployment** - Insufficient basic capabilities |