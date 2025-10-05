"""
Google Gemini model wrapper
"""

import os
from typing import Dict
import google.generativeai as genai
from .base_model import BaseModel


class GeminiModel(BaseModel):
    """Google Gemini 2.5 Pro implementation"""
    
    def __init__(self, model_id: str = "gemini-2.0-flash-exp"):
        super().__init__(model_id)
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_id)
    
    def assess_validity(self, test_case: Dict) -> Dict:
        """Assess validity using Gemini"""
        prompt = self.format_prompt(test_case)
        
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    'temperature': 0.0,
                    'max_output_tokens': 1000,
                }
            )
            
            raw_response = response.text
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
