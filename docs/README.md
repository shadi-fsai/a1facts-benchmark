# A1Facts Benchmark Documentation

Welcome to the comprehensive documentation for the A1Facts triangulation benchmark. This directory contains detailed guides, metrics explanations, and technical specifications.

---

# 📚 Documentation Structure

| Directory/File | Purpose | Audience |
|----------------|---------|----------|
| **metrics/** | Complete metrics guide and definitions | Researchers, Data Scientists |
| **ARCHITECTURE.md** | System design and technical architecture | Developers, System Architects |
| **SETUP_GUIDE.md** | Installation and configuration guide | All Users |

---

# 🎯 Quick Navigation

## 📊 **Metrics & Evaluation**
- **[Metrics Overview](metrics/README.md)** - Complete guide to all benchmark metrics
- **[Core Metrics](metrics/core_metrics.md)** - Essential performance indicators  
- **[Business Interpretation](metrics/business_interpretation.md)** - Real-world impact analysis
- **[Tier Definitions](metrics/tier_definitions.md)** - Performance classification levels

## 🔧 **Technical Guides**
- **[Architecture](../ARCHITECTURE.md)** - System design and components
- **[Setup Guide](../SETUP_GUIDE.md)** - Installation instructions
- **[Project Summary](../PROJECT_SUMMARY.md)** - High-level project overview

## 📋 **Dataset Documentation**
- **[Dataset Guide](../datasets/README.md)** - Complete dataset documentation
- **[Data Generation](../src/data_generation/)** - How test cases are created

---

# 🚀 Getting Started

## 1. **First-Time Setup**
```bash
# Clone and install
git clone https://github.com/shadi-fsai/a1facts-benchmark.git
cd a1facts-benchmark
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

## 2. **Run Basic Benchmark**
```bash
# Quick start (uses existing datasets)
python run_benchmark.py

# Or use the full evaluation system
python -m src.evaluation.run_benchmark --dataset datasets/triangulation_benchmark_v1.json
```

## 3. **Understand Results**
- Read **[Metrics Guide](metrics/README.md)** to interpret scores
- Check **[Business Interpretation](metrics/business_interpretation.md)** for decision-making guidance

---

# 📊 Benchmark Overview

## **Three-Dataset Framework**

### 🏗️ **Foundation Dataset** (Manual - 300 cases)
- **Purpose**: Test basic single-source assessment
- **Use Case**: Foundation capability validation
- **File**: `datasets/a1facts_manual_300_cases.json`

### 🔺 **Coverage Dataset** (Triangulation - 134 cases)  
- **Purpose**: Systematic multi-source pattern testing
- **Use Case**: Deployment readiness assessment
- **File**: `datasets/triangulation_benchmark_v1.json`

### 🧠 **Synthesis Dataset** (Advanced - 100 cases)
- **Purpose**: Complex reasoning and conflict resolution
- **Use Case**: Strategic decision support validation  
- **File**: `datasets/triangulation_synthesis_benchmark_v1.json`

## **Supported AI Models**
- **GPT-4** (OpenAI)
- **Claude** (Anthropic)  
- **Gemini** (Google)
- **Extensible architecture** for additional models

---

# 🎯 Use Cases by Role

## 👨‍💼 **Business Leaders**
- **Start with**: [Business Interpretation Guide](metrics/business_interpretation.md)
- **Focus on**: ROI metrics, deployment readiness scores
- **Key question**: "Is this AI ready for production?"

## 👨‍🔬 **Researchers & Data Scientists**
- **Start with**: [Core Metrics Guide](metrics/core_metrics.md)
- **Focus on**: F1 scores, classification performance, statistical analysis
- **Key question**: "How does this model perform across different scenarios?"

## 👨‍💻 **Developers & Engineers**  
- **Start with**: [Architecture Guide](../ARCHITECTURE.md)
- **Focus on**: Implementation details, API integration, scalability
- **Key question**: "How do I integrate and deploy this?"

## 🎓 **Academic Users**
- **Start with**: [Dataset Documentation](../datasets/README.md)
- **Focus on**: Methodology, ground truth reasoning, reproducibility
- **Key question**: "How was this benchmark designed and validated?"

---

# 🔍 Advanced Usage

## **Custom Evaluation Scenarios**

### **Single Dataset Testing**
```bash
# Test foundation capabilities only
python -m src.evaluation.run_benchmark --dataset datasets/a1facts_manual_300_cases.json --metrics tier1

# Test advanced reasoning only  
python -m src.evaluation.run_benchmark --dataset datasets/triangulation_synthesis_benchmark_v1.json --metrics comprehensive
```

### **Comparative Analysis**
```bash
# Compare models across all datasets
python -m src.evaluation.run_benchmark --dataset all --models gpt4,claude,gemini --comparative
```

### **Custom Metrics Selection**
```bash
# Focus on specific metrics
python -m src.evaluation.run_benchmark --metrics accuracy,f1 --detailed-output
```

## **Dataset Generation**
```bash
# Generate custom test cases
cd src/data_generation
python generate_dataset.py --type coverage --count 50 --domains medical,financial

# Create domain-specific benchmarks
python generate_dataset.py --type synthesis --complexity high --domains technology
```

---

# 📈 Performance Benchmarks

## **Expected Performance Ranges**

| Dataset | Basic AI | Advanced AI | Expert-Level AI |
|---------|----------|-------------|-----------------|
| **Manual** | 60-70% | 75-85% | 85-95% |
| **Coverage** | 45-60% | 65-80% | 80-90% |
| **Synthesis** | 35-50% | 55-75% | 75-85% |

## **Deployment Readiness Thresholds**

- **🟢 Production Ready**: >80% on Coverage + >70% on Synthesis
- **🟡 Limited Deployment**: >70% on Coverage + >60% on Synthesis  
- **🔴 Development Only**: <70% on Coverage or <60% on Synthesis

---

# 🤝 Contributing

## **Adding New Test Cases**
1. Follow [Dataset Documentation](../datasets/README.md) format
2. Use `src/data_generation/generate_dataset.py` for consistency
3. Include expert reasoning for ground truth

## **Supporting New Models**
1. Implement `BaseModel` interface in `src/models/`
2. Add model configuration to evaluation framework
3. Test against existing benchmarks

## **Documentation Updates**
- Keep metrics documentation synchronized with code
- Update performance benchmarks with new results
- Maintain business interpretation guides

---

# 📞 Support & Resources

## **Getting Help**
- **Issues**: Report bugs and request features on GitHub
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Check this guide first for answers

## **External Resources**
- **Comet ML**: Experiment tracking and visualization
- **OpenAI API**: GPT model integration
- **Anthropic API**: Claude model integration
- **Google AI**: Gemini model integration

---

# 🏆 Citation

If you use A1Facts benchmark in your research, please cite:

```bibtex
@misc{a1facts2024,
  title={A1Facts: Comprehensive Triangulation Benchmark for AI Information Assessment},
  author={[Author Names]},
  year={2024},
  url={https://github.com/shadi-fsai/a1facts-benchmark}
}
```

---

**🎯 Ready to get started? Check the [Setup Guide](../SETUP_GUIDE.md) or jump straight to [running your first benchmark](../run_benchmark.py)!**