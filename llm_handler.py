"""
LLM Handler - Manages LLM API calls with Groq and Gemini fallback
"""
import os
import time
from dotenv import load_dotenv

load_dotenv()


class LLMHandler:
    """
    Handles LLM API calls with retry logic and fallback.
    Primary: Groq
    Fallback: Gemini
    """
    
    def __init__(self, provider="groq", mock=False):
        self.mock = mock
        self.provider = provider
        self.gemini_key = os.getenv("GEMINI_API_KEY")
        self.groq_key = os.getenv("GROQ_API_KEY")
        
        if not mock:
            if self.groq_key:
                from groq import Groq
                self.groq_client = Groq(api_key=self.groq_key)
            elif self.gemini_key:
                import google.generativeai as genai
                genai.configure(api_key=self.gemini_key)
                self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    def call(self, sys, usr, json_m=False, retries=3):
        """
        Call LLM with system and user prompts.
        
        Args:
            sys: System prompt
            usr: User prompt
            json_m: Whether to request JSON response
            retries: Number of retry attempts
        
        Returns:
            LLM response as string
        """
        if self.mock:
            return '{"mock": "data"}' if json_m else "PASS"
        
        for attempt in range(retries + 1):
            try:
                if self.groq_key:
                    full_sys = sys + " Respond in JSON format." if json_m and "json" not in sys.lower() else sys
                    res = self.groq_client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": full_sys},
                            {"role": "user", "content": usr}
                        ],
                        model="llama-3.3-70b-versatile",
                        response_format={"type": "json_object" if json_m else "text"}
                    )
                    resp = res.choices[0].message.content
                
                elif self.gemini_key:
                    prompt = f"{sys}\n\n{usr}"
                    if json_m:
                        prompt += "\n\nRespond ONLY with JSON."
                    resp = self.model.generate_content(prompt).text.strip()
                
                if json_m:
                    text = resp.strip()
                    if text.startswith("```json"):
                        text = text.split("```json")[1].split("```")[0].strip()
                    elif text.startswith("```"):
                        text = text.split("```")[1].split("```")[0].strip()
                    return text
                
                return resp
            
            except Exception as e:
                if attempt == retries:
                    raise e
                time.sleep(2)
        
        raise ValueError("No API Key.")
