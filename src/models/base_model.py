"""
Base model interface for A1Facts benchmark evaluation
"""

from abc import ABC, abstractmethod
from typing import Dict, List


class BaseModel(ABC):
    """Abstract base class for all LLM models"""
    
    def __init__(self, model_name: str):
        self.model_name = model_name
    
    @abstractmethod
    def assess_validity(self, test_case: Dict) -> Dict:
        """
        Assess information validity for a test case.
        
        Args:
            test_case: Dict containing sources and metadata
            
        Returns:
            Dict with:
                - validity_rating: int (1-6)
                - reliability_scores: List[str] (A-F for each source)
                - reasoning: str (explanation)
                - raw_response: str (full model output)
        """
        pass
    
    def format_prompt(self, test_case: Dict) -> str:
        """
        Format test case into evaluation prompt using A1Facts template.
        
        This uses the exact prompt from knowledge_acquirer.py
        Handles both dataset formats:
        - Triangulation format: test_case['sources'] (list of dicts)
        - Manual format: test_case['source_url'] + test_case['source_summary'] (single source)
        """
        # Handle different dataset structures
        if 'sources' in test_case:
            # Triangulation dataset format
            sources_text = "\n".join([
                f"{i+1}. {source['url']}: {source['claim']}"
                for i, source in enumerate(test_case['sources'])
            ])
        elif 'source_url' in test_case and 'source_summary' in test_case:
            # Manual dataset format
            sources_text = f"1. {test_case['source_url']}: {test_case['source_summary']}"
        else:
            # Fallback - try to extract from available fields
            sources_text = "1. Unknown source: " + str(test_case.get('content', test_case.get('claim', 'No content available')))
        
        
        prompt = f"""You are evaluating information validity using the A1Facts triangulation methodology.

IMPORTANT: Source Reliability Assessment
Evaluate each web source using this scale:
A: Completely reliable - The source is undoubtedly authentic and trustworthy.
B: Usually reliable - Minor doubts exist, but the source is historically valid.
C: Fairly reliable - Doubts exist, but the source has provided valid information before.
D: Not usually reliable - Significant doubts about the source's reliability.
E: Unreliable - The source has a history of providing invalid information.
F: Reliability cannot be judged - Insufficient information for evaluation.

IMPORTANT: Information Validity Assessment
After gathering information, assess each piece of data using this scale:
1. Confirmed: Corroborated by multiple, independent, reliable sources.
2. Probably true: Logical and consistent with other data, but not fully corroborated.
3. Possibly true: Plausible but lacks strong corroboration.
4. Doubtful: Not logical or may be contradicted by other information.
5. Improbable: Illogical and contradicted by other information.
6. Cannot be judged: Insufficient information to assess validity.

SOURCES TO EVALUATE:
{sources_text}

Provide your assessment in the following format:
SOURCE RELIABILITY SCORES:
[List each source with its A-F rating]

OVERALL VALIDITY RATING: [1-6]

REASONING:
[Explain your assessment]
"""
        return prompt
    
    def parse_response(self, response: str) -> Dict:
        """
        Parse model response to extract structured assessment.
        
        This is a basic parser - subclasses can override for model-specific parsing.
        """
        result = {
            'validity_rating': None,
            'reliability_scores': [],
            'reasoning': '',
            'raw_response': response
        }
        
        lines = response.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if 'OVERALL VALIDITY RATING' in line.upper():
                # Extract validity rating (1-6)
                for char in line:
                    if char.isdigit() and char in '123456':
                        result['validity_rating'] = int(char)
                        break
            
            elif 'SOURCE RELIABILITY' in line.upper():
                current_section = 'reliability'
            
            elif 'REASONING' in line.upper():
                current_section = 'reasoning'
            
            elif current_section == 'reliability' and line:
                # Extract reliability scores (A-F) - look for pattern like "source: A" or "A:"
                import re
                # Match patterns like "reuters.com: A" or "1. source: B" or just "A" at end of line
                match = re.search(r':\s*([A-F])\b', line)
                if match:
                    result['reliability_scores'].append(match.group(1))
                elif re.search(r'\b([A-F])\s*$', line):  # A-F at end of line
                    rating = re.search(r'\b([A-F])\s*$', line).group(1)
                    result['reliability_scores'].append(rating)
            
            elif current_section == 'reasoning' and line:
                result['reasoning'] += line + ' '
        
        result['reasoning'] = result['reasoning'].strip()
        return result
