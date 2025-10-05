"""
Count expected metrics in the new implementation
"""

# Validity metrics (1-6)
validity_metrics = []
validity_metrics.append('validity_accuracy')
validity_metrics.append('validity_macro_f1')
for rating in range(1, 7):
    validity_metrics.append(f'validity_{rating}_precision')
    validity_metrics.append(f'validity_{rating}_recall')
    validity_metrics.append(f'validity_{rating}_f1')
    validity_metrics.append(f'validity_{rating}_support')
validity_metrics.append('validity_confusion_matrix')

# Reliability metrics (A-F)
reliability_metrics = []
reliability_metrics.append('reliability_accuracy')
reliability_metrics.append('reliability_macro_f1')
for rating in ['A', 'B', 'C', 'D', 'E', 'F']:
    reliability_metrics.append(f'reliability_{rating}_precision')
    reliability_metrics.append(f'reliability_{rating}_recall')
    reliability_metrics.append(f'reliability_{rating}_f1')
    reliability_metrics.append(f'reliability_{rating}_support')
reliability_metrics.append('reliability_confusion_matrix')

# Overall metrics
overall_metrics = ['strict_accuracy', 'strict_correct', 'total_cases']

print("📊 ALL METRICS - COMPLETE LIST:\n")

print(f"🎯 VALIDITY METRICS ({len(validity_metrics)} total):")
for i, m in enumerate(validity_metrics, 1):
    print(f"  {i:2d}. {m}")

print(f"\n🔍 RELIABILITY METRICS ({len(reliability_metrics)} total):")
for i, m in enumerate(reliability_metrics, 1):
    print(f"  {i:2d}. {m}")

print(f"\n⭐ OVERALL METRICS ({len(overall_metrics)} total):")
for i, m in enumerate(overall_metrics, 1):
    print(f"  {i:2d}. {m}")

total = len(validity_metrics) + len(reliability_metrics) + len(overall_metrics)
print(f"\n{'='*60}")
print(f"✅ TOTAL: {total} metrics")
print(f"{'='*60}")
print(f"\nBreakdown:")
print(f"  - Validity (1-6 scale): {len(validity_metrics)} metrics")
print(f"  - Reliability (A-F scale): {len(reliability_metrics)} metrics")
print(f"  - Overall: {len(overall_metrics)} metrics")
