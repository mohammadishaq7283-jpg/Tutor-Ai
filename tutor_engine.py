import os
from openai import OpenAI
from prompts import get_tutor_prompt

BASE_URL = "https://openrouter.ai/api/v1"

# --- SMART MODEL LIST ---
# Humne 2 models rakhe hain. Agar ek fail hua to code khud doosra use karega.
# 1. Primary: Llama 3.2 3B (Bohot Fast hai - Timeout nahi hoga)
# 2. Backup: Gemini Flash Lite (Agar Llama busy ho)
PRIMARY_MODEL = "meta-llama/llama-3.2-3b-instruct:free"
BACKUP_MODEL = "google/gemini-2.0-flash-lite-preview-02-05:free"

def get_ai_response(user_message, subject, language):
    
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("API_KEY")
    if not api_key:
        return "⚠️ Error: API Key missing in Vercel Settings!"

    system_prompt = get_tutor_prompt(subject, user_message, language)

    # Client setup
    client = OpenAI(base_url=BASE_URL, api_key=api_key)
    
    # Helper function to try a model
    def try_generate(model_name):
        return client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful Tutor. Be concise."},
                {"role": "user", "content": system_prompt}
            ],
            max_tokens=250, # Jawab chhota rakho taake jaldi aaye
            extra_headers={
                "HTTP-Referer": "https://vercel.app", 
                "X-Title": "Tutor AI App",
            },
        )

    # --- ATTEMPT 1: Primary Model ---
    try:
        response = try_generate(PRIMARY_MODEL)
        if response and response.choices:
            return response.choices[0].message.content
    except Exception as e:
        print(f"Primary model failed: {e}")
        # Agar pehla fail ho jaye, to yahan rukna nahi hai...
    
    # --- ATTEMPT 2: Backup Model ---
    try:
        response = try_generate(BACKUP_MODEL)
        if response and response.choices:
            return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Server Error: Both AI models are busy. Please try again in 1 minute."

    return "⚠️ AI is silent."
