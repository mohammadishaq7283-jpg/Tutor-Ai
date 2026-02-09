def get_tutor_prompt(subject, user_question, language):
    """
    Creates the AI persona with Language enforcement.
    """
    
    # Subject Specific Roles
    if subject == "Math":
        role = "Math Tutor. Solve problems step-by-step. Use emojis like ➕➖."
    elif subject == "Science":
        role = "Science Teacher. Explain simply with real-life examples 🧬."
    elif subject == "History":
        role = "History Professor. Tell stories about the past 🏛️."
    elif subject == "Coding":
        role = "Senior Developer. Explain logic and code 💻."
    else:
        # For "Ask Anything" / General
        role = "Professional Education Consultant & Tutor. You can answer ANY educational problem, career advice, or homework help."

    # Final Prompt with Language Rule
    prompt = f"""
    ROLE: You are a {role}
    LANGUAGE INSTRUCTION: You MUST reply in '{language}'.
    
    RULES:
    1. If the language is Urdu/Hindi, use Roman script (e.g., "Kya haal hai") or proper script if requested.
    2. Keep answers educational, polite, and encouraging.
    3. If the question is not about education, politely bring the topic back to learning.
    
    USER QUESTION: {user_question}
    """
    
    return prompt
    
