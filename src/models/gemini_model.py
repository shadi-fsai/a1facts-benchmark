"""
Google Gemini model wrapper
"""

import os
from typing import Dict
import google.generativeai as genai
from dotenv import load_dotenv
from .base_model import BaseModel

# Ensure .env is loaded
load_dotenv()


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
        """Assess validity using Gemini with SAME methodology as other models"""
        # Use the exact same prompt as BaseModel (same as OpenAI)
        prompt = self.format_prompt(test_case)
        try:
            # Configure safety settings to be more permissive for academic research
            safety_settings = [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_NONE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH", 
                    "threshold": "BLOCK_NONE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_NONE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_NONE"
                }
            ]
            
            response = self.model.generate_content(
                prompt,
                generation_config={
                    'temperature': 0.0,
                    'max_output_tokens': 2048,
                    'candidate_count': 1,
                    'top_p': 1.0,
                    'top_k': 40
                },
                safety_settings=safety_settings
            )
            
            # Check response status before accessing text
            if response.candidates and response.candidates[0].content.parts:
                raw_response = response.text
                result = self.parse_response(raw_response)
            else:
                # Handle blocked or empty responses
                finish_reason = response.candidates[0].finish_reason if response.candidates else "UNKNOWN"
                safety_ratings = response.candidates[0].safety_ratings if response.candidates else []
                
                return {
                    'validity_rating': None,
                    'reliability_scores': [],
                    'reasoning': f'Response blocked. Finish reason: {finish_reason}',
                    'raw_response': '',
                    'model': self.model_name,
                    'test_case_id': test_case.get('id', 'unknown'),
                    'error': f'Content blocked by safety filters. Reason: {finish_reason}',
                    'safety_ratings': [str(r) for r in safety_ratings]
                }
            
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
