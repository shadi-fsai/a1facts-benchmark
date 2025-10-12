# A1Facts Benchmark Metrics Guide

## 📖 Overview

This guide explains every metric in the A1Facts benchmark evaluation system, what they measure, and how to interpret them for decision-making.

## 🎯 Quick Reference

| Metric Type | What It Measures | Business Impact |
|-------------|------------------|-----------------|
| **Strict Accuracy** | Both reliability AND validity correct | Overall deployment readiness |
| **Reliability Accuracy** | Source quality assessment capability | Trust in information sources |
| **Validity Accuracy** | Information confidence determination | Decision-making confidence |
| **F1 Scores** | Balanced precision and recall | Performance on specific ratings |

## 📊 Core Metrics Categories

### 1. **Overall Performance Metrics**
- **Purpose**: High-level deployment readiness assessment
- **Use Case**: Executive decision-making and model comparison

### 2. **Reliability Assessment Metrics**  
- **Purpose**: How well the model evaluates source quality
- **Use Case**: Information verification and source trust

### 3. **Validity Assessment Metrics**
- **Purpose**: How well the model determines information confidence
- **Use Case**: Decision confidence and risk assessment

### 4. **Detailed Classification Metrics**
- **Purpose**: Performance on specific rating levels
- **Use Case**: Fine-tuning and diagnostic analysis

## 🎯 Tiered Evaluation Framework

### **Tier 1: Critical Metrics** (Go/No-Go Decisions)
Essential metrics for deployment decisions. If these fail, the model is not ready.

### **Tier 2: Diagnostic Metrics** (Performance Analysis)
Metrics for understanding strengths/weaknesses and improvement areas.

### **Tier 3: Analytical Metrics** (Deep Insights)
Detailed metrics for optimization, research, and comprehensive analysis.

## 📋 Dataset-Specific Applications

### **Manual Dataset** (Foundation Skills)
- **Focus**: Single-source reliability and validity assessment
- **Critical for**: Basic deployment readiness
- **Key Question**: "Can it assess individual sources correctly?"

### **Coverage Dataset** (Triangulation Patterns)
- **Focus**: Multi-source pattern recognition across all reliability combinations
- **Critical for**: Systematic triangulation deployment
- **Key Question**: "Can it handle all triangulation scenarios consistently?"

### **Synthesis Dataset** (Advanced Reasoning)
- **Focus**: Complex logic, conflict resolution, and sophisticated reasoning
- **Critical for**: Advanced AI deployment in complex domains
- **Key Question**: "Can it reason through complex conflicting information?"

## 🎪 See Individual Metric Files

- [**Core Metrics**](./core_metrics.md) - Overall performance indicators
- [**Reliability Metrics**](./reliability_metrics.md) - Source quality assessment
- [**Validity Metrics**](./validity_metrics.md) - Information confidence determination  
- [**Classification Metrics**](./classification_metrics.md) - Detailed per-rating performance
- [**Tier Definitions**](./tier_definitions.md) - Complete tier breakdown by dataset
- [**Business Interpretation**](./business_interpretation.md) - How to use metrics for decisions

## ⚡ Quick Start

1. **New to A1Facts?** Start with [Core Metrics](./core_metrics.md)
2. **Need deployment decision?** Check [Tier Definitions](./tier_definitions.md)
3. **Model comparison?** Use [Business Interpretation](./business_interpretation.md)
4. **Performance issues?** See [Classification Metrics](./classification_metrics.md)

## 🔍 Metric Lookup

**Looking for a specific metric?** Use Ctrl+F with these terms:

- `strict_accuracy` → [Core Metrics](./core_metrics.md)
- `reliability_A_f1` → [Reliability Metrics](./reliability_metrics.md)
- `validity_2_precision` → [Validity Metrics](./validity_metrics.md)
- `confusion_matrix` → [Classification Metrics](./classification_metrics.md)