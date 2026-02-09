import os
from openai import OpenAI
from prompts import get_tutor_prompt

# --- CONFIG ---
BASE_URL = "https://openrouter.ai/api/v1"
MODEL_NAME = "stepfun/step-3.5-flash:free" # Ya koi bhi free model

def get_ai_response(user_message, subject):
    """
    Connects to AI API to get tutor response.
    """
    
    # 1. Check API Key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "⚠️ Error: API Key missing in Settings!"

    # 2. Get Prompt
    system_prompt = get_tutor_prompt(subject, user_message)

    try:
        # 3. Call AI
        client = OpenAI(
            base_url=BASE_URL,
            api_key=api_key,
        )

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a professional tutor."},
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
