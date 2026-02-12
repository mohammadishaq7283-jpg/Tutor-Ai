import os
from openai import OpenAI
from prompts import get_tutor_prompt

# --- CONFIG ---
BASE_URL = "https://openrouter.ai/api/v1"

# --- MODEL SELECTION ---
# Yeh model abhi active hai (Fast & Free)
# Agar yeh bhi band ho jaye, to 'meta-llama/llama-3.2-3b-instruct:free' use karein
MODEL_NAME = "google/gemini-2.0-flash-lite-preview-02-05:free"

def get_ai_response(user_message, subject, language):
    
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("API_KEY")
    if not api_key:
        return "⚠️ Error: API Key missing in Settings!"

    # Prompt generate karna
    system_prompt = get_tutor_prompt(subject, user_message, language)

    try:
        client = OpenAI(base_url=BASE_URL, api_key=api_key)

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful Tutor."},
                {"role": "user", "content": system_prompt}
            ],
            extra_headers={
                "HTTP-Referer": "https://vercel.app", 
                "X-Title": "Tutor AI App",
            },
        )

        if response and response.choices:
            return response.choices[0].message.content
        else:
            return "Thinking... (No response from AI)"

    except Exception as e:
        # Error message ko saaf dikhana
        error_msg = str(e)
        if "404" in error_msg:
            return "⚠️ Model Error: The AI model is currently down. Please update MODEL_NAME in tutor_engine.py."
        return f"Connection Error: {error_msg}"
