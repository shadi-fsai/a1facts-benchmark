"""
OpenAI GPT-4o model wrapper
"""

import os
from typing import Dict
from openai import OpenAI
from .base_model import BaseModel


class GPT4Model(BaseModel):
    """OpenAI GPT-4o implementation"""
    
    def __init__(self, model_id: str = "gpt-4o"):
        super().__init__(model_id)
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        self.client = OpenAI(api_key=api_key)
    
    def assess_validity(self, test_case: Dict) -> Dict:
        """Assess validity using GPT-4o"""
        prompt = self.format_prompt(test_case)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are an expert at evaluating source reliability and information validity using systematic triangulation methods."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,  # Deterministic for evaluation
                max_tokens=1000
            )
            
            raw_response = response.choices[0].message.content
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
