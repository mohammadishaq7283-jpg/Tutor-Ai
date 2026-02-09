from flask import Flask, request, jsonify, render_template_string
from frontend_ui import HTML_CODE

# Import Engine safely
try:
    from tutor_engine import get_ai_response
except ImportError:
    def get_ai_response(msg, sub): return f"Echo: {msg} (Engine Missing)"

app = Flask(__name__)

# --- ROUTES ---

@app.route('/')
def home():
    # Frontend HTML serve karna
    return render_template_string(HTML_CODE)

@app.route('/api/chat', methods=['POST'])
def chat_api():
    try:
        data = request.json
        user_message = data.get('message', '')
        subject = data.get('subject', 'General')
        
        # Call AI Engine
        ai_reply = get_ai_response(user_message, subject)

        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": f"Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()
