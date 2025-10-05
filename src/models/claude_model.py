"""
Anthropic Claude model wrapper
"""

import os
from typing import Dict
from anthropic import Anthropic
from .base_model import BaseModel


class ClaudeModel(BaseModel):
    """Anthropic Claude 3.5 Sonnet implementation"""
    
    def __init__(self, model_id: str = "claude-3-5-sonnet-20241022"):
        super().__init__(model_id)
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        self.client = Anthropic(api_key=api_key)
    
    def assess_validity(self, test_case: Dict) -> Dict:
        """Assess validity using Claude"""
        prompt = self.format_prompt(test_case)
        
        try:
            response = self.client.messages.create(
                model=self.model_name,
                max_tokens=1000,
                temperature=0.0,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            raw_response = response.content[0].text
            result = self.parse_response(raw_response)
            
            # Add metadata
            result['model'] = self.model_name
            result['test_case_id'] = test_case.get('id', 'unknown')
            
            return result
            
        except Exception as e:
            return {
                'validity_rating': None,
                'reliability_scores': [],
                'reasoning': f'Error: {str(e)}',
                'raw_response': '',
                'model': self.model_name,
                'test_case_id': test_case.get('id', 'unknown'),
                'error': str(e)
            }
