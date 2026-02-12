import os
from openai import OpenAI
from prompts import get_tutor_prompt

# --- CONFIG ---
BASE_URL = "https://openrouter.ai/api/v1"

# Updated Model (DeepSeek R1 - Free Version)
MODEL_NAME = "deepseek/deepseek-r1:free"

def get_ai_response(user_message, subject, language):
    """
    Connects to AI API to get tutor response.
    """
    
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
        return f"Connection Error: {str(e)}"
