
# Manual 300 Dataset - Comprehensive Visualization Report

## 📊 **Dataset Overview**
- **Total Cases**: 300 high-quality manual test cases
- **Models Evaluated**: 5 (Gemini 2.5 Flash, Gemini 2.5 Pro, GPT-4 Turbo, Gemini Flash, Gemini 2.0 Flash)
- **Evaluation Type**: Parallel processing (5x faster than sequential)
- **Perfect Balance**: 50 cases per reliability grade (A-F)

## 🏆 **Key Performance Rankings**

### Strict Accuracy (Both Validity + Reliability Correct)
1. **Gemini 2.5 Flash**: 13.7% (41/300 cases)
2. **Gemini 2.5 Pro**: 12.3% (37/300 cases)
3. **GPT-4 Turbo**: 9.7% (29/300 cases)
4. **Gemini Flash**: 8.0% (24/300 cases)
5. **Gemini 2.0 Flash**: 2.3% (7/300 cases)

### Individual Performance
- **Best Validity**: Gemini Flash (53.0%)
- **Best Reliability**: Gemini 2.5 Pro (47.3%)
- **Most Balanced**: Gemini 2.5 Flash (46.5% validity, 38.5% reliability)

## 🎯 **Critical Findings**

### Performance Challenges
1. **Overall Strict Accuracy**: Range 2.3% - 13.7% (very challenging)
2. **Validity Assessment**: Generally stronger (40-53% accuracy)  
3. **Reliability Assessment**: More difficult (33-47% accuracy)
4. **Grade C Reliability**: Complete failure across all models (0% performance)

### Model Strengths & Weaknesses
- **Gemini 2.5 Flash**: Best overall balanced performance
- **Gemini 2.5 Pro**: Excels at reliability assessment, especially grades D-F
- **GPT-4 Turbo**: Consistent performance, good at validity level 4
- **Gemini Flash**: Exceptional validity detection but poor reliability assessment
- **Gemini 2.0 Flash**: Significantly underperforms across all metrics

## 📈 **Generated Visualizations**
1. `manual_300_tier1_strict_accuracy.png` - Rankings and case counts
2. `manual_300_tier2_individual_accuracies.png` - Validity vs reliability comparison
3. `manual_300_tier3_validity_by_level.png` - Performance by validity levels 1-6
4. `manual_300_tier3_reliability_by_grade.png` - Performance by reliability grades A-F
5. `manual_300_key_insights.png` - Summary of critical findings
6. `manual_300_comprehensive_dashboard.html` - Interactive analysis dashboard

## 🚀 **Research Implications**

### Practical Applications
- Current AI models require human oversight for reliability assessment
- Validity ratings more trustworthy than reliability scores  
- Best use case: Pre-screening with human verification

### Future Development Priorities
1. Improve reliability assessment capabilities, especially Grade C detection
2. Enhance validity level 4 (doubtful) performance
3. Balance trade-offs between validity and reliability accuracy

Generated from: results/manual_300_evaluation_summary.md
Date: October 15, 2025
