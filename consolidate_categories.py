"""
Fix: Consolidate test case categories to reduce metric explosion

Current: 23 unique categories (one per test case)
Target: 5-7 broad categories reused across test cases
"""

import json

# Load current dataset
with open('datasets/triangulation_benchmark_v1.json', 'r') as f:
    data = json.load(f)

# Category mapping: old_category -> new_category
CATEGORY_MAPPING = {
    # Medical/Health
    'medical_fact': 'medical',
    'clinical_trial': 'medical',
    'medical_impossibility': 'medical',
    'medical_speculation': 'medical',
    'medical_correlation': 'medical',
    'ambiguous_medical': 'medical',
    'drug_safety': 'medical',
    'clinical_contradiction': 'medical',
    
    # Financial/Business
    'financial_fact': 'financial',
    'market_reaction': 'financial',
    
    # Technology
    'technology_trend': 'technology',
    'tech_speculation': 'technology',
    
    # Historical/Events
    'historical_event': 'historical',
    'geopolitical_implication': 'historical',
    
    # Logic/Math
    'mathematical_impossibility': 'logic',
    'physical_impossibility': 'logic',
    'temporal_impossibility': 'logic',
    'logical_inconsistency': 'logic',
    'contradiction': 'logic',
    'mixed_reliability_contradiction': 'logic',
    
    # Information Quality
    'insufficient_context': 'information_quality',
    'missing_context': 'information_quality',
    'unrelated_information': 'information_quality',
}

# Update categories
for case in data:
    old_cat = case['category']
    new_cat = CATEGORY_MAPPING.get(old_cat, 'other')
    case['category'] = new_cat

# Save updated dataset
with open('datasets/triangulation_benchmark_v1_consolidated.json', 'w') as f:
    json.dump(data, f, indent=2)

# Print summary
from collections import Counter
categories = [case['category'] for case in data]
cat_counts = Counter(categories)

print("✅ Consolidated categories:")
print(f"\nBefore: 23 unique categories")
print(f"After: {len(cat_counts)} categories\n")

for cat, count in sorted(cat_counts.items()):
    print(f"  {cat}: {count} cases")

print(f"\nTotal metrics now:")
print(f"  - Per-test-case: 23")
print(f"  - Overall: 3")
print(f"  - Per-validity: 12")
print(f"  - Per-category: {len(cat_counts)}")
print(f"  = {23 + 3 + 12 + len(cat_counts)} total (was 62)")

print(f"\n✅ Saved to: datasets/triangulation_benchmark_v1_consolidated.json")
