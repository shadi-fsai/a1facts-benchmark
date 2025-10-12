# A1Facts Benchmark Datasets

This directory contains three complementary datasets for comprehensive A1Facts triangulation evaluation. Each dataset tests different aspects of information triangulation capabilities.

---

# 📊 Dataset Overview

| Dataset | Cases | Purpose | Focus Area | Complexity |
|---------|-------|---------|------------|------------|
| **Manual** | 300 | Foundation Skills | Single-source assessment | Basic |
| **Coverage** | 134 | Pattern Recognition | Multi-source triangulation | Systematic |
| **Synthesis** | 100 | Advanced Reasoning | Complex conflict resolution | Advanced |
| **TOTAL** | **534** | **Complete AI Assessment** | **End-to-end triangulation** | **Progressive** ?

---

# 📋 Manual Dataset (Foundation Skills) - 300 Cases

## Purpose
Tests fundamental single-source reliability and validity assessment capabilities. This is the **foundation layer** that must be mastered before advanced triangulation.

## Dataset Characteristics
- **File**: `a1facts_manual_300_cases.json`
- **Focus**: Individual source quality assessment
- **Scenario**: Single source per test case
- **Difficulty**: Basic to intermediate

## Statistical Distribution

### Validity Distribution (1-6 Scale)
- **Validity 1** (Very Low): ~15% (45 cases) - Poor/contradictory evidence
- **Validity 2** (Low): ~25% (75 cases) - Weak/mixed evidence  
- **Validity 3** (Some): ~20% (60 cases) - Limited evidence
- **Validity 4** (Moderate): ~20% (60 cases) - Good evidence
- **Validity 5** (High): ~15% (45 cases) - Strong evidence
- **Validity 6** (Extremely High): ~5% (15 cases) - Multiple A-tier agreement

### Reliability Distribution (A-F Scale)
- **A-Tier** (Premium): ~20% (60 cases) - Peer-reviewed, authoritative
- **B-Tier** (Reputable): ~25% (75 cases) - Established sources
- **C-Tier** (Generally Reliable): ~25% (75 cases) - Standard sources
- **D-Tier** (Questionable): ~15% (45 cases) - Some concerns
- **E-Tier** (Poor): ~10% (30 cases) - Significant issues  
- **F-Tier** (Unreliable): ~5% (15 cases) - Discredited/dangerous

### Domain Categories
- **Medical/Health**: ~30% (90 cases)
- **Technology**: ~20% (60 cases)
- **Finance/Economics**: ~15% (45 cases)
- **Science/Research**: ~15% (45 cases)
- **Policy/Government**: ~10% (30 cases)
- **General/Other**: ~10% (30 cases)

## Business Applications
- **Foundation verification**: Can AI assess basic source quality?
- **Single-source decisions**: Medical recommendations, financial advice
- **Quality gate**: Minimum capability before advanced deployment

---

# 🔺 Coverage Dataset (Triangulation Patterns) - 134 Cases

## Purpose
Systematic testing of multi-source triangulation across **all possible reliability combinations**. Tests pattern recognition and consistent triangulation logic.

## Dataset Characteristics
- **File**: `triangulation_benchmark_v1.json`
- **Focus**: Multi-source pattern recognition (2-4 sources per case)
- **Coverage**: All 19 unique reliability patterns
- **Scenario**: Systematic triangulation across reliability spectrum

## Statistical Distribution

### Validity Distribution (Triangulation Outcomes)
- **Validity 1** (Very Low): ~8% (11 cases) - Contradictory sources
- **Validity 2** (Low): ~45% (60 cases) - Mixed evidence (most common)
- **Validity 3** (Some): ~25% (33 cases) - Moderate triangulation
- **Validity 4** (Moderate): ~15% (20 cases) - Good consensus
- **Validity 5** (High): ~5% (7 cases) - Strong agreement
- **Validity 6** (Extremely High): ~2% (3 cases) - Perfect A-tier consensus

### Reliability Pattern Coverage (19 Systematic Patterns)

#### **High Agreement Patterns** (~15 cases)
- **AAA**: 3 A-tier sources (Validity 6 - Perfect)
- **BBB**: 3 B-tier sources (Validity 5 - Strong)
- **CCC**: 3 C-tier sources (Validity 4 - Good)

#### **Majority Consensus Patterns** (~35 cases)
- **AAB, ABB**: A-tier majority (Validity 5-6)
- **BBC, CCB**: B-tier majority (Validity 4-5)
- **CCD, DCC**: C-tier majority (Validity 3-4)

#### **Mixed Reliability Patterns** (~45 cases)
- **ABC**: Declining quality (Validity 2-3)
- **ACD**: Skip pattern (Validity 2-3)
- **BDE**: Poor trend (Validity 1-2)

#### **Low Reliability Patterns** (~25 cases)
- **DEF**: All poor quality (Validity 1)
- **EFF**: F-tier majority (Validity 1)
- **FFF**: All unreliable (Validity 1)

#### **Conflict Patterns** (~14 cases)
- **AEF**: Premium vs. Poor (Validity 2)
- **BDF**: Mixed spread (Validity 2)
- **ACF**: Wide range (Validity 1-2)

### Domain Distribution
- **Medical Research**: ~25% (33 cases) - Clinical studies, treatments
- **Technology**: ~20% (27 cases) - Product reviews, specifications  
- **Financial Markets**: ~15% (20 cases) - Market analysis, predictions
- **Scientific Research**: ~15% (20 cases) - Academic studies
- **Policy Analysis**: ~10% (13 cases) - Government reports
- **Consumer Products**: ~10% (13 cases) - Product comparisons
- **General News**: ~5% (8 cases) - Current events

## Pattern Complexity Analysis
- **Simple Patterns** (Same/adjacent ratings): ~25% - Should achieve >85% accuracy
- **Moderate Patterns** (2-level spread): ~50% - Target >75% accuracy
- **Complex Patterns** (3+ level spread): ~25% - Expect >65% accuracy

## Business Applications
- **Systematic deployment**: Handles all triangulation scenarios consistently
- **Pattern-based decisions**: E-commerce, content moderation, research
- **Reliability assessment**: Multi-source journalism, fact-checking

---

# 🧠 Synthesis Dataset (Advanced Reasoning) - 100 Cases

## Purpose
Tests sophisticated triangulation logic, conflict resolution, and complex reasoning in challenging real-world scenarios.

## Dataset Characteristics
- **File**: `triangulation_synthesis_benchmark_v1.json`
- **Focus**: Advanced reasoning and conflict resolution
- **Scenario**: Complex multi-source conflicts requiring sophisticated logic
- **Complexity**: Highest difficulty with nuanced reasoning requirements

## Statistical Distribution

### Validity Distribution (Complex Reasoning Focus)
- **Validity 1** (Very Low): ~5% (5 cases) - Clear contradictions
- **Validity 2** (Low): **~63% (63 cases)** - **Most common** (mixed evidence requiring reasoning)
- **Validity 3** (Some): ~20% (20 cases) - Balanced but uncertain
- **Validity 4** (Moderate): ~8% (8 cases) - Good reasoning prevails
- **Validity 5** (High): ~3% (3 cases) - Clear expert consensus
- **Validity 6** (Extremely High): ~1% (1 case) - Overwhelming evidence

### Reliability Pattern Distribution (Advanced Scenarios)
- **Expert vs. Popular**: ~25% (25 cases) - A-tier experts vs. C-tier popular sources
- **Methodological Conflicts**: ~20% (20 cases) - Different study designs, conflicting results
- **Temporal Conflicts**: ~15% (15 cases) - Newer vs. older sources with conflicting info
- **Authority Conflicts**: ~15% (15 cases) - Multiple A-tier sources disagreeing
- **Domain Expertise**: ~15% (15 cases) - Specialist vs. generalist sources
- **Regulatory Conflicts**: ~10% (10 cases) - Government vs. independent sources

### Advanced Reasoning Types

#### **Conflict Resolution** (~40 cases)
- **Expert Weighting**: Prioritize specialist knowledge
- **Methodological Assessment**: Evaluate research quality
- **Temporal Relevance**: Weight newer vs. established knowledge
- **Consensus Building**: Find common ground in disagreement

#### **Uncertainty Handling** (~35 cases)
- **Confidence Expression**: Appropriate uncertainty quantification
- **Evidence Gaps**: Acknowledge missing information
- **Limitation Recognition**: Understand scope constraints
- **Risk Assessment**: Balance confidence with consequences

#### **Sophisticated Logic** (~25 cases)
- **Multi-dimensional Analysis**: Consider multiple factors simultaneously  
- **Contextual Reasoning**: Apply domain-specific logic
- **Meta-analysis**: Synthesize across different evidence types
- **Regulatory Awareness**: Understand compliance implications

### Domain Distribution (Complex Scenarios)
- **Medical/Clinical**: ~35% (35 cases) - Treatment conflicts, regulatory disputes
- **Financial/Investment**: ~20% (20 cases) - Market predictions, risk analysis
- **Technology/Engineering**: ~15% (15 cases) - Technical specifications, safety assessments
- **Legal/Regulatory**: ~10% (10 cases) - Policy interpretation, compliance
- **Scientific Research**: ~10% (10 cases) - Methodological conflicts, replication
- **Business Strategy**: ~10% (10 cases) - Market analysis, competitive intelligence

### Reasoning Quality Metrics
- **Methodological Awareness**: Does AI consider research quality?
- **Expert Weighting**: Does AI properly weight specialist sources?
- **Conflict Resolution**: Can AI resolve contradictory high-quality sources?
- **Uncertainty Expression**: Does AI express appropriate confidence levels?
- **Contextual Understanding**: Does AI apply domain-specific logic?

## Business Applications
- **High-stakes decisions**: Medical treatments, financial investments
- **Expert systems**: Professional advisory services
- **Regulatory compliance**: Policy interpretation, risk assessment
- **Strategic planning**: Complex multi-factor business decisions

---

# 🎯 Dataset Format Specification

## Common Structure
Each test case contains:
```json
{
  "id": "unique_case_identifier",
  "category": "domain_category",
  "claim": "information_to_assess",
  "sources": [
    {
      "content": "source_claim_text",
      "url": "source_url_or_reference",
      "reliability": "A-F_reliability_rating"
    }
  ],
  "expected_reliability": ["A", "B", "C"],
  "expected_validity": 2,
  "reasoning": "expert_explanation_of_ground_truth",
  "triangulation_type": "scenario_type"
}
```

## Validity Scale (1-6)
- **6**: Extremely high confidence - Multiple A-tier sources agree
- **5**: High confidence - Strong consensus from reliable sources
- **4**: Moderate confidence - Good evidence with minor gaps
- **3**: Some confidence - Limited but plausible evidence
- **2**: Low confidence - Weak/mixed evidence requiring caution
- **1**: Very low confidence - Poor/contradictory evidence

## Reliability Scale (A-F)
- **A**: Premium quality - Peer-reviewed, authoritative institutions
- **B**: Reputable - Established, well-known reliable sources  
- **C**: Generally reliable - Standard sources with good track record
- **D**: Questionable - Some reliability concerns or limitations
- **E**: Poor reliability - Significant quality or bias issues
- **F**: Unreliable - Discredited, dangerous, or fraudulent sources

---

# 🚀 Usage Guidelines

## Progressive Testing Strategy
1. **Start with Manual** - Verify foundation capabilities
2. **Advance to Coverage** - Test systematic triangulation
3. **Challenge with Synthesis** - Evaluate advanced reasoning

## Dataset Selection by Use Case

### **Basic Deployment** (Single dataset)
- **Manual only**: Foundation AI capabilities
- **Coverage only**: Systematic multi-source handling
- **Synthesis only**: Advanced reasoning assessment

### **Standard Evaluation** (Two datasets)
- **Manual + Coverage**: Foundation + systematic patterns
- **Coverage + Synthesis**: Patterns + advanced reasoning
- **Manual + Synthesis**: Foundation + complexity handling

### **Comprehensive Assessment** (All three datasets)
- **Complete capability evaluation**: End-to-end triangulation assessment
- **Full deployment readiness**: All complexity levels tested
- **Strategic decision support**: Complete AI capability profile

## Generating Additional Test Cases

```bash
# Generate new manual cases
cd src/data_generation
python generate_dataset.py --type manual --count 100

# Generate coverage patterns
python generate_dataset.py --type coverage --patterns all

# Generate synthesis scenarios  
python generate_dataset.py --type synthesis --complexity high
```

---

# 📊 Dataset Statistics Summary

| Metric | Manual | Coverage | Synthesis | Combined |
|--------|---------|-----------|-----------|----------|
| **Total Cases** | 300 | 134 | 100 | **534** |
| **Avg Sources/Case** | 1.0 | 2.8 | 3.2 | 2.1 |
| **Unique Patterns** | 6 | 19 | 25+ | 50+ |
| **Domain Coverage** | 6 | 7 | 6 | 8+ |
| **Validity Focus** | Balanced | V2 (45%) | V2 (63%) | V2 (52%) |
| **Reliability Focus** | A-C (70%) | All levels | A+F conflicts | Full spectrum |
| **Complexity Level** | Basic | Systematic | Advanced | Progressive |
| **Business Readiness** | Foundation | Deployment | Strategic | Complete |

**Total Evaluation Coverage**: 534 test cases across all triangulation scenarios for comprehensive AI assessment. 🎯
