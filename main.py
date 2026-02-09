from flask import Flask, request, jsonify, render_template_string
from frontend_ui import HTML_CODE
# Baad mein hum tutor_engine import karenge
# from tutor_engine import get_ai_response 

app = Flask(__name__)

# --- ROUTES ---

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/api/chat', methods=['POST'])
def chat_api():
    try:
        data = request.json
        user_message = data.get('message', '')
        subject = data.get('subject', 'General')
        
        # --- ABHI KE LIYE DUMMY REPLY (Jab tak engine na ban jaye) ---
        # Next step mein hum isay AI se connect karenge
        ai_reply = f"Thinking about '{user_message}' in context of {subject}..."
        
        # Real connection next step mein:
        # ai_reply = get_ai_response(user_message, subject)

        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()
