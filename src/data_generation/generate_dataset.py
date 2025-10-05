"""
Generate objective test cases for A1Facts triangulation evaluation.

This module creates test cases where the ground truth is objectively determinable
based on logical consistency, mathematical validity, and established facts.
"""

import json
from typing import Dict, List
try:
    from .domain_authority import get_reliability_rating, get_domains_by_rating
except ImportError:
    from domain_authority import get_reliability_rating, get_domains_by_rating


class TestCaseGenerator:
    """Generate test cases for each validity rating (1-6)"""
    
    def __init__(self):
        self.test_cases = []
    
    def generate_rating_1_confirmed(self) -> List[Dict]:
        """
        Rating 1: Confirmed - Multiple independent, reliable sources agree
        """
        return [
            {
                "id": "confirmed_001",
                "category": "medical_fact",
                "sources": [
                    {"url": "nih.gov", "claim": "Diabetes affects approximately 11.3% of US adults"},
                    {"url": "cdc.gov", "claim": "Diabetes prevalence is 11.3% among US adults"},
                    {"url": "who.int", "claim": "About 11% of American adults have diabetes"}
                ],
                "expected_reliability_scores": ["A", "A", "A"],
                "expected_validity": 1,
                "reasoning": "Three independent A-tier sources confirm same statistic"
            },
            {
                "id": "confirmed_002",
                "category": "financial_fact",
                "sources": [
                    {"url": "sec.gov", "claim": "Apple reported $97.3B revenue in Q1 2024"},
                    {"url": "reuters.com", "claim": "Apple Q1 2024 revenue: $97.3 billion"},
                    {"url": "bloomberg.com", "claim": "AAPL Q1 revenue reached $97.3B"}
                ],
                "expected_reliability_scores": ["A", "B", "B"],
                "expected_validity": 1,
                "reasoning": "Official filing plus two major financial news sources confirm"
            },
            {
                "id": "confirmed_003",
                "category": "historical_event",
                "sources": [
                    {"url": "apnews.com", "claim": "Biden won 2020 election with 306 electoral votes"},
                    {"url": "bbc.com", "claim": "Biden secured 306 electoral votes in 2020"},
                    {"url": "reuters.com", "claim": "2020 US election result: Biden 306, Trump 232"}
                ],
                "expected_reliability_scores": ["A", "A", "A"],
                "expected_validity": 1,
                "reasoning": "Historical fact confirmed by multiple wire services"
            },
            {
                "id": "confirmed_004",
                "category": "clinical_trial",
                "sources": [
                    {"url": "clinicaltrials.gov", "claim": "NCT02569242 Phase III trial completed with 1,296 participants"},
                    {"url": "nejm.org", "claim": "Pembrolizumab trial enrolled 1,296 patients in Phase III study"},
                    {"url": "fda.gov", "claim": "Approval based on trial with 1,296 subjects"}
                ],
                "expected_reliability_scores": ["A", "A", "A"],
                "expected_validity": 1,
                "reasoning": "Official trial registry, peer-reviewed journal, and FDA all confirm same enrollment number"
            },
        ]
    
    def generate_rating_2_probably_true(self) -> List[Dict]:
        """
        Rating 2: Probably True - Logical and consistent, not fully corroborated
        """
        return [
            {
                "id": "probably_001",
                "category": "market_reaction",
                "sources": [
                    {"url": "sec.gov", "claim": "Tesla reported record Q3 profits"},
                    {"url": "bloomberg.com", "claim": "TSLA stock rises 8% in after-hours trading"},
                    {"url": "wsj.com", "claim": "Analyst upgrades Tesla rating to 'buy'"}
                ],
                "expected_reliability_scores": ["A", "B", "B"],
                "expected_validity": 2,
                "reasoning": "Stock rise logically follows good earnings, analyst confirms trend"
            },
            {
                "id": "probably_002",
                "category": "medical_correlation",
                "sources": [
                    {"url": "nejm.org", "claim": "Study shows Drug X reduces heart attacks by 45%"},
                    {"url": "mayoclinic.org", "claim": "Cardiologists recommend Drug X for high-risk patients"},
                    {"url": "reuters.com", "claim": "Drug X sales increased 200% this quarter"}
                ],
                "expected_reliability_scores": ["A", "B", "A"],
                "expected_validity": 2,
                "reasoning": "Medical effectiveness logically explains recommendation and sales"
            },
            {
                "id": "probably_003",
                "category": "drug_safety",
                "sources": [
                    {"url": "fda.gov", "claim": "Drug Y associated with 2.3% rate of severe allergic reactions"},
                    {"url": "hopkinsmedicine.org", "claim": "Patients with drug allergies should avoid Drug Y"},
                    {"url": "webmd.com", "claim": "Drug Y can cause allergic reactions in some patients"}
                ],
                "expected_reliability_scores": ["A", "B", "C"],
                "expected_validity": 2,
                "reasoning": "Logical consistency between FDA data and medical advice, though WebMD is less specific"
            },
            {
                "id": "probably_004",
                "category": "technology_trend",
                "sources": [
                    {"url": "wsj.com", "claim": "Apple acquires AI startup for $200M"},
                    {"url": "bloomberg.com", "claim": "Apple expanding AI team by 300 engineers"},
                    {"url": "reuters.com", "claim": "Industry analysts expect major AI announcement from Apple"}
                ],
                "expected_reliability_scores": ["B", "B", "A"],
                "expected_validity": 2,
                "reasoning": "Acquisition and hiring logically support prediction, but prediction not yet confirmed"
            },
        ]
    
    def generate_rating_3_possibly_true(self) -> List[Dict]:
        """
        Rating 3: Possibly True - Plausible but lacks strong corroboration
        """
        return [
            {
                "id": "possibly_001",
                "category": "geopolitical_implication",
                "sources": [
                    {"url": "reuters.com", "claim": "Russia invaded Ukraine"},
                    {"url": "bloomberg.com", "claim": "China increased military readiness level"},
                    {"url": "ft.com", "claim": "Global defense stocks rise 12%"}
                ],
                "expected_reliability_scores": ["A", "B", "B"],
                "expected_validity": 3,
                "reasoning": "Plausible connection between events but indirect correlation"
            },
            {
                "id": "possibly_002",
                "category": "tech_speculation",
                "sources": [
                    {"url": "wsj.com", "claim": "Apple developing new AI chip"},
                    {"url": "marketwatch.com", "claim": "Semiconductor stocks rise on AI demand"},
                    {"url": "cnbc.com", "claim": "Industry insiders expect major AI announcements"}
                ],
                "expected_reliability_scores": ["B", "C", "C"],
                "expected_validity": 3,
                "reasoning": "Plausible industry trends but speculative connection"
            },
            {
                "id": "possibly_003",
                "category": "medical_speculation",
                "sources": [
                    {"url": "healthline.com", "claim": "Vitamin D supplements may boost immune function"},
                    {"url": "webmd.com", "claim": "Some studies suggest vitamin D benefits for immunity"},
                    {"url": "medicalnewstoday.com", "claim": "Researchers investigating vitamin D and immune health"}
                ],
                "expected_reliability_scores": ["C", "C", "C"],
                "expected_validity": 3,
                "reasoning": "Plausible health claim but uses hedging language (may, suggest), lacks strong evidence"
            },
        ]
    
    def generate_rating_4_doubtful(self) -> List[Dict]:
        """
        Rating 4: Doubtful - Not logical or contradicted by other information
        """
        return [
            {
                "id": "doubtful_001",
                "category": "contradiction",
                "sources": [
                    {"url": "reuters.com", "claim": "Company X reports $5B quarterly revenue"},
                    {"url": "sec.gov", "claim": "Company X filed for bankruptcy protection"},
                    {"url": "bloomberg.com", "claim": "Company X stock trading halted"}
                ],
                "expected_reliability_scores": ["A", "A", "B"],
                "expected_validity": 4,
                "reasoning": "Record revenue contradicts bankruptcy filing"
            },
            {
                "id": "doubtful_002",
                "category": "logical_inconsistency",
                "sources": [
                    {"url": "cdc.gov", "claim": "Obesity rates decreased 15% in 2023"},
                    {"url": "nih.gov", "claim": "Diabetes cases increased 20% in 2023"},
                    {"url": "mayoclinic.org", "claim": "Fast food consumption rose to all-time high"}
                ],
                "expected_reliability_scores": ["A", "A", "B"],
                "expected_validity": 4,
                "reasoning": "Obesity decrease conflicts with diabetes increase and fast food rise"
            },
            {
                "id": "doubtful_003",
                "category": "clinical_contradiction",
                "sources": [
                    {"url": "clinicaltrials.gov", "claim": "Trial NCT12345 shows Drug Z effective for Stage IV cancer"},
                    {"url": "fda.gov", "claim": "Drug Z only approved for Stage I-II cancer treatment"},
                    {"url": "reuters.com", "claim": "FDA rejects Drug Z application for advanced cancer"}
                ],
                "expected_reliability_scores": ["A", "A", "A"],
                "expected_validity": 4,
                "reasoning": "Trial claim contradicts FDA approval scope and rejection"
            },
            {
                "id": "doubtful_004",
                "category": "mixed_reliability_contradiction",
                "sources": [
                    {"url": "mayoclinic.org", "claim": "Aspirin reduces heart attack risk by 25% in clinical trials"},
                    {"url": "healthblog.net", "claim": "Aspirin causes more heart attacks than it prevents"},
                    {"url": "webmd.com", "claim": "Aspirin has proven cardiovascular benefits for at-risk patients"}
                ],
                "expected_reliability_scores": ["B", "E", "C"],
                "expected_validity": 4,
                "reasoning": "Unreliable blog contradicts established medical consensus from reputable sources"
            },
        ]
    
    def generate_rating_5_improbable(self) -> List[Dict]:
        """
        Rating 5: Improbable - Illogical and contradicted, or mathematically impossible
        """
        return [
            {
                "id": "improbable_001",
                "category": "mathematical_impossibility",
                "sources": [
                    {"url": "reuters.com", "claim": "Company has $10 billion annual revenue"},
                    {"url": "sec.gov", "claim": "Company employs 5 people total"},
                    {"url": "bloomberg.com", "claim": "Average employee salary is $50,000"}
                ],
                "expected_reliability_scores": ["A", "A", "B"],
                "expected_validity": 5,
                "reasoning": "Mathematically impossible: 5 employees × $50k = $250k costs, cannot generate $10B"
            },
            {
                "id": "improbable_002",
                "category": "temporal_impossibility",
                "sources": [
                    {"url": "apnews.com", "claim": "iPhone 15 released September 2023"},
                    {"url": "reuters.com", "claim": "iPhone 15 discontinued in 2020"},
                    {"url": "bloomberg.com", "claim": "Apple announced iPhone 15 in 2019"}
                ],
                "expected_reliability_scores": ["A", "A", "B"],
                "expected_validity": 5,
                "reasoning": "Timeline impossible: cannot discontinue before release"
            },
            {
                "id": "improbable_003",
                "category": "physical_impossibility",
                "sources": [
                    {"url": "reuters.com", "claim": "Flight from NYC to London took 2 hours"},
                    {"url": "bbc.com", "claim": "Average cruising speed was 500 mph"},
                    {"url": "apnews.com", "claim": "Distance covered: 3,500 miles"}
                ],
                "expected_reliability_scores": ["A", "A", "A"],
                "expected_validity": 5,
                "reasoning": "Physics impossible: 500 mph × 2 hours = 1,000 miles ≠ 3,500 miles"
            },
            {
                "id": "improbable_004",
                "category": "medical_impossibility",
                "sources": [
                    {"url": "naturalnews.com", "claim": "Vitamin C cures all cancers within 48 hours"},
                    {"url": "healthfraud.org", "claim": "Big Pharma hiding the cancer cure in lemons"},
                    {"url": "conspiracy-health.net", "claim": "Doctors don't want you to know about vitamin C miracle"}
                ],
                "expected_reliability_scores": ["E", "E", "E"],
                "expected_validity": 5,
                "reasoning": "Medically impossible claim from unreliable sources, contradicts all medical evidence"
            },
        ]
    
    def generate_rating_6_cannot_judge(self) -> List[Dict]:
        """
        Rating 6: Cannot Judge - Insufficient or unrelated information
        """
        return [
            {
                "id": "cannot_judge_001",
                "category": "unrelated_information",
                "sources": [
                    {"url": "reuters.com", "claim": "Weather is sunny in Seattle"},
                    {"url": "bloomberg.com", "claim": "Bitcoin price is $45,000"},
                    {"url": "wsj.com", "claim": "NFL season starts in September"}
                ],
                "expected_reliability_scores": ["A", "B", "B"],
                "expected_validity": 6,
                "reasoning": "Completely unrelated facts, no logical connection to assess"
            },
            {
                "id": "cannot_judge_002",
                "category": "insufficient_context",
                "sources": [
                    {"url": "unknown-blog.com", "claim": "The product works well"},
                    {"url": "random-site.net", "claim": "Results may vary"},
                    {"url": "mystery-domain.org", "claim": "Further research needed"}
                ],
                "expected_reliability_scores": ["F", "F", "F"],
                "expected_validity": 6,
                "reasoning": "Vague claims from unknown sources, cannot assess validity"
            },
            {
                "id": "cannot_judge_003",
                "category": "ambiguous_medical",
                "sources": [
                    {"url": "random-health-blog.com", "claim": "Some patients feel better"},
                    {"url": "unverified-site.org", "claim": "Treatment might help"},
                    {"url": "anonymous-forum.net", "claim": "I heard it works sometimes"}
                ],
                "expected_reliability_scores": ["F", "F", "F"],
                "expected_validity": 6,
                "reasoning": "Extremely vague claims from unknown sources, no specific information to evaluate"
            },
            {
                "id": "cannot_judge_004",
                "category": "missing_context",
                "sources": [
                    {"url": "obscure-news.com", "claim": "The trial was successful"},
                    {"url": "unknown-medical.net", "claim": "Patients responded positively"},
                    {"url": "mystery-health.org", "claim": "Results exceeded expectations"}
                ],
                "expected_reliability_scores": ["F", "F", "F"],
                "expected_validity": 6,
                "reasoning": "No context about which trial, which patients, what outcome - cannot judge without specifics"
            },
        ]
    
    def generate_all(self) -> List[Dict]:
        """Generate complete dataset across all validity ratings"""
        dataset = []
        dataset.extend(self.generate_rating_1_confirmed())
        dataset.extend(self.generate_rating_2_probably_true())
        dataset.extend(self.generate_rating_3_possibly_true())
        dataset.extend(self.generate_rating_4_doubtful())
        dataset.extend(self.generate_rating_5_improbable())
        dataset.extend(self.generate_rating_6_cannot_judge())
        return dataset
    
    def save_dataset(self, filepath: str):
        """Save generated dataset to JSON file"""
        dataset = self.generate_all()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)
        print(f"✅ Generated {len(dataset)} test cases")
        print(f"📁 Saved to: {filepath}")
        
        # Print statistics
        validity_counts = {}
        for case in dataset:
            v = case['expected_validity']
            validity_counts[v] = validity_counts.get(v, 0) + 1
        
        print("\n📊 Dataset Statistics:")
        for rating in sorted(validity_counts.keys()):
            print(f"  Rating {rating}: {validity_counts[rating]} cases")


if __name__ == "__main__":
    import os
    generator = TestCaseGenerator()
    
    # Create datasets directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(__file__), "..", "..", "datasets")
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, "triangulation_benchmark_v1.json")
    generator.save_dataset(output_file)
