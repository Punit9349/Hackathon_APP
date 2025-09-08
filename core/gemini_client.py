import os
import google.generativeai as genai

# Get API key from environment
# API_KEY = os.getenv("GEMINI_API_KEY")
API_KEY=""
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not set. Please configure your environment variable.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text