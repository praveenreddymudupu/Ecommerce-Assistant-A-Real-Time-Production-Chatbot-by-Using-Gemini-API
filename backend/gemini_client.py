import os
import google.generativeai as genai

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found.")

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-3-flash-preview")

    def generate(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return "⚠️ API limit reached. Please wait a few seconds and try again."
