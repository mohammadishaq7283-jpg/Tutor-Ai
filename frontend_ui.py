# Is file mein HTML, CSS aur JavaScript hai
# Yeh App ka Chehra (Frontend) hai

HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Tutor Pro</title>
    <style>
        :root {
            --bg-color: #ffffff;
            --text-color: #333333;
            --card-bg: #f8f9fa;
            --chat-user: #007bff;
            --chat-ai: #e9ecef;
            --chat-ai-text: #333;
        }

        [data-theme="dark"] {
            --bg-color: #121212;
            --text-color: #e0e0e0;
            --card-bg: #1e1e1e;
            --chat-user: #bb86fc;
            --chat-ai: #333333;
            --chat-ai-text: #fff;
        }

        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: var(--bg-color); color: var(--text-color); margin: 0; padding: 0; transition: 0.3s; display: flex; justify-content: center; height: 100vh; }
        .container { width: 100%; max-width: 480px; display: flex; flex-direction: column; height: 100%; position: relative; }
        
        /* HEADER */
        .header { padding: 15px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #ddd; }
        .title { font-weight: bold; font-size: 20px; }
        .theme-btn { background: none; border: none; font-size: 20px; cursor: pointer; color: var(--text-color); }

        /* SCREENS */
        .screen { display: none; flex: 1; padding: 20px; overflow-y: auto; }
        .active { display: flex; flex-direction: column; }

        /* AUTH FORMS */
        .auth-box { background: var(--card-bg); padding: 25px; border-radius: 12px; margin-top: 50px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #ccc; background: var(--bg-color); color: var(--text-color); box-sizing: border-box;}
        .btn-primary { width: 100%; padding: 12px; background: #007bff; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        .link { text-align: center; margin-top: 15px; color: #007bff; cursor: pointer; font-size: 14px; }

        /* SUBJECT SELECTION */
        .subject-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px; }
        .subject-card { background: var(--card-bg); padding: 20px; border-radius: 12px; text-align: center; cursor: pointer; border: 2px solid transparent; transition: 0.2s; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .subject-card:hover { border-color: #007bff; transform: translateY(-2px); }
        .subject-icon { font-size: 30px; display: block; margin-bottom: 10px; }

        /* CHAT AREA */
        #chat-history { flex: 1; overflow-y: auto; padding: 10px; display: flex; flex-direction: column; gap: 10px; }
        .message { padding: 10px 15px; border-radius: 15px; max-width: 80%; line-height: 1.4; font-size: 15px; }
        .user-msg { align-self: flex-end; background: var(--chat-user); color: white; border-bottom-right-radius: 2px; }
        .ai-msg { align-self: flex-start; background: var(--chat-ai); color: var(--chat-ai-text); border-bottom-left-radius: 2px; }
        
        .chat-input-area { padding: 10px; border-top: 1px solid #ccc; display: flex; gap: 10px; background: var(--bg-color); }
        .chat-input-area input { margin: 0; }
        .send-btn { width: 50px; background: #007bff; color: white; border: none; border-radius: 8px; cursor: pointer; }

    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <div class="title" id="header-title">AI Tutor</div>
        <button class="theme-btn" onclick="toggleTheme()">🌗</button>
    </div>

    <!-- 1. LOGIN SCREEN -->
    <div id="screen-login" class="screen active">
        <div class="auth-box">
            <h2 style="text-align: center;">Welcome Back</h2>
            <input type="text" id="login-email" placeholder="Email or Username">
            <input type="password" id="login-pass" placeholder="Password">
            <button class="btn-primary" onclick="handleLogin()">Login</button>
            <div class="link" onclick="showScreen('signup')">Don't have an account? Sign Up</div>
        </div>
    </div>

    <!-- 2. SIGNUP SCREEN -->
    <div id="screen-signup" class="screen">
        <div class="auth-box">
            <h2 style="text-align: center;">Create Account</h2>
            <input type="text" id="signup-name" placeholder="Full Name">
            <input type="text" id="signup-email" placeholder="Email">
            <input type="password" id="signup-pass" placeholder="Password">
            <button class="btn-primary" onclick="handleSignup()">Sign Up</button>
            <div class="link" onclick="showScreen('login')">Already have an account? Login</div>
        </div>
    </div>

    <!-- 3. SUBJECT DASHBOARD -->
    <div id="screen-dashboard" class="screen">
        <h3>Choose a Subject 📚</h3>
        <p>What do you want to learn today?</p>
        <div class="subject-grid">
            <div class="subject-card" onclick="startChat('Math')">
                <span class="subject-icon">📐</span> Math
            </div>
            <div class="subject-card" onclick="startChat('Science')">
                <span class="subject-icon">🧬</span> Science
            </div>
            <div class="subject-card" onclick="startChat('History')">
                <span class="subject-icon">🏛️</span> History
            </div>
            <div class="subject-card" onclick="startChat('English')">
                <span class="subject-icon">📖</span> English
            </div>
            <div class="subject-card" onclick="startChat('Coding')">
                <span class="subject-icon">💻</span> Coding
            </div>
            <div class="subject-card" onclick="startChat('General')">
                <span class="subject-icon">🤖</span> Any Topic
            </div>
        </div>
        <div class="link" onclick="logout()" style="margin-top: 30px; color: red;">Logout</div>
    </div>

    <!-- 4. CHAT SCREEN -->
    <div id="screen-chat" class="screen" style="padding: 0; display: none; flex-direction: column;">
        <div style="padding: 10px; background: var(--card-bg); border-bottom: 1px solid #ccc; display: flex; align-items: center;">
            <button onclick="showScreen('dashboard')" style="background:none; border:none; font-size:20px; cursor:pointer; margin-right: 10px; color: var(--text-color);">←</button>
            <b id="chat-subject-title">Subject</b>
        </div>
        
        <div id="chat-history">
            <div class="message ai-msg">Hello! I am your AI Tutor. Ask me anything about this subject!</div>
        </div>

        <div class="chat-input-area">
            <input type="text" id="user-msg" placeholder="Type your question..." onkeypress="if(event.key==='Enter') sendMessage()">
            <button class="send-btn" onclick="sendMessage()">➤</button>
        </div>
    </div>
</div>

<script>
    // --- THEME LOGIC ---
    function toggleTheme() {
        const body = document.body;
        const current = body.getAttribute('data-theme');
        const newTheme = current === 'dark' ? 'light' : 'dark';
        body.setAttribute('data-theme', newTheme);
    }

    // --- NAVIGATION ---
    function showScreen(screenId) {
        document.querySelectorAll('.screen').forEach(s => {
            s.classList.remove('active');
            s.style.display = 'none'; // Force hide
        });
        
        const target = document.getElementById('screen-' + screenId);
        target.classList.add('active');
        
        // Flex fix for chat screen
        if(screenId === 'chat') target.style.display = 'flex';
        else target.style.display = 'block';
    }

    // --- MOCK AUTH (Since Vercel is stateless without DB) ---
    let currentUser = null;

    function handleLogin() {
        const email = document.getElementById('login-email').value;
        if(email) {
            currentUser = email;
            showScreen('dashboard');
        } else alert("Please enter email");
    }

    function handleSignup() {
        const name = document.getElementById('signup-name').value;
        if(name) {
            currentUser = name;
            showScreen('dashboard');
        } else alert("Please enter details");
    }

    function logout() {
        currentUser = null;
        showScreen('login');
    }

    // --- CHAT LOGIC ---
    let currentSubject = "";

    function startChat(subject) {
        currentSubject = subject;
        document.getElementById('chat-subject-title').innerText = subject + " Tutor";
        document.getElementById('chat-history').innerHTML = `<div class="message ai-msg">Hello! I am your <b>${subject}</b> Tutor. Ask me anything!</div>`;
        showScreen('chat');
    }

    async function sendMessage() {
        const input = document.getElementById('user-msg');
        const text = input.value.trim();
        if(!text) return;

        // 1. Add User Message
        addMessage(text, 'user-msg');
        input.value = '';

        // 2. Show Loading
        const loadingId = addMessage("Thinking...", 'ai-msg');

        // 3. Call API
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    message: text,
                    subject: currentSubject,
                    user: currentUser
                })
            });
            const data = await response.json();
            
            // Remove Loading & Add AI Response
            document.getElementById(loadingId).innerText = data.reply;
        } catch(e) {
            document.getElementById(loadingId).innerText = "Error: Could not connect to Tutor.";
        }
    }

    function addMessage(text, className) {
        const div = document.createElement('div');
        div.className = 'message ' + className;
        div.innerHTML = text; // Allow HTML for bolding
        div.id = 'msg-' + Date.now();
        document.getElementById('chat-history').appendChild(div);
        
        // Auto Scroll
        const history = document.getElementById('chat-history');
        history.scrollTop = history.scrollHeight;
        return div.id;
    }
</script>

</body>
</html>
"""
