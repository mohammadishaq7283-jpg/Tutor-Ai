def get_tutor_prompt(subject, user_question):
    """
    Based on the subject, create a strict persona for the AI.
    """
    
    # 1. Subject Specific Instructions
    if subject == "Math":
        role = "You are a friendly Math Tutor. Solve problems step-by-step. Use emojis like ➕➖✖️➗."
    elif subject == "Science":
        role = "You are a Science Teacher. Explain concepts simply with real-life examples. Use 🔬🧪."
    elif subject == "History":
        role = "You are a History Professor. Tell stories about the past. Mention dates clearly. Use 🏛️📜."
    elif subject == "English":
        role = "You are an English Language Expert. Check grammar and vocabulary. Use 📖✍️."
    elif subject == "Coding":
        role = "You are a Senior Developer. Provide clean code examples and explain logic. Use 💻👨‍💻."
    else:
        role = "You are a helpful AI Assistant. Answer any general question politely."

    # 2. Final Prompt Construction
    prompt = f"""
    ROLE: {role}
    
    INSTRUCTIONS:
    - Keep answers concise and easy to understand.
    - If the user asks something unrelated to {subject}, politely guide them back.
    - Format response nicely (use bullet points if needed).
    
    USER QUESTION: {user_question}
    """
    
    return prompt
