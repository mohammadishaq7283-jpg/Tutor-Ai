from flask import Flask, request, jsonify, render_template_string
from frontend_ui import HTML_CODE

try:
    from tutor_engine import get_ai_response
except ImportError:
    def get_ai_response(msg, sub, lang): return f"Echo ({lang}): {msg}"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/api/chat', methods=['POST'])
def chat_api():
    try:
        data = request.json
        user_message = data.get('message', '')
        subject = data.get('subject', 'General')
        language = data.get('language', 'English') # Default English
        
        # AI ko call karte waqt language bhejen
        ai_reply = get_ai_response(user_message, subject, language)

        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": f"Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()
