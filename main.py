from flask import Flask, request, jsonify, render_template_string
import sys
import traceback

# --- FLASK SETUP ---
app = Flask(__name__)

# --- DEBUG LOADING ---
# Hum check karenge ke doosri files sahi hain ya nahi
engine_status = "OK"
loading_error = ""

try:
    from frontend_ui import HTML_CODE
except Exception as e:
    loading_error += f"Frontend Error: {str(e)}\n"

try:
    from tutor_engine import get_ai_response
except Exception as e:
    engine_status = "ERROR"
    loading_error += f"Engine Import Error: {str(e)}\n{traceback.format_exc()}\n"

# --- ROUTES ---

@app.route('/')
def home():
    # Agar loading mein error aya tha, to wo screen par dikhao
    if loading_error:
        return f"""
        <div style="background:#ffebee; color:#c62828; padding:20px; font-family:monospace;">
            <h2>⚠️ System Crash Error</h2>
            <p>App start nahi ho saki kyunki files mein error hai:</p>
            <pre>{loading_error}</pre>
            <p>Please check your files on GitHub.</p>
        </div>
        """
    return render_template_string(HTML_CODE)

@app.route('/api/chat', methods=['POST'])
def chat_api():
    if engine_status == "ERROR":
        return jsonify({"reply": "⚠️ Server Error: Tutor Engine file is broken. Check logs."}), 500

    try:
        data = request.json
        user_message = data.get('message', '')
        subject = data.get('subject', 'General')
        language = data.get('language', 'English')
        
        # Asli AI Call
        ai_reply = get_ai_response(user_message, subject, language)
        return jsonify({"reply": ai_reply})

    except Exception as e:
        # Agar chalti hui chat mein error aaye
        error_msg = f"Runtime Error: {str(e)}"
        print(error_msg)
        return jsonify({"reply": f"⚠️ {error_msg}"}), 500

if __name__ == '__main__':
    app.run()
