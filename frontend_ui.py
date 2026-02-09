# HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Tutor Pro</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --bg-color: #ffffff;
            --text-color: #333333;
            --card-bg: #f8f9fa;
            --input-bg: #ffffff;
            --border-color: #ddd;
            --chat-user: #007bff;
            --chat-ai: #e9ecef;
            --chat-ai-text: #333;
        }

        [data-theme="dark"] {
            --bg-color: #121212;
            --text-color: #e0e0e0;
            --card-bg: #1e1e1e;
            --input-bg: #2d2d2d;
            --border-color: #444;
            --chat-user: #bb86fc;
            --chat-ai: #333333;
            --chat-ai-text: #fff;
        }

        body { font-family: 'Segoe UI', sans-serif; background-color: var(--bg-color); color: var(--text-color); margin: 0; padding: 0; transition: 0.3s; display: flex; justify-content: center; height: 100vh; }
        .container { width: 100%; max-width: 480px; display: flex; flex-direction: column; height: 100%; }
        
        /* HEADER */
        .header { padding: 15px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); }
        .title { font-weight: bold; font-size: 20px; }
        .theme-btn { background: none; border: none; font-size: 20px; cursor: pointer; color: var(--text-color); }

        /* SCREENS */
        .screen { display: none; flex: 1; padding: 20px; overflow-y: auto; }
        .active { display: flex; flex-direction: column; }

        /* AUTH FORMS */
        .auth-box { background: var(--card-bg); padding: 25px; border-radius: 12px; margin-top: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; }
        input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid var(--border-color); background: var(--input-bg); color: var(--text-color); box-sizing: border-box;}
        
        .btn-primary { width: 100%; padding: 12px; background: #007bff; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px; font-size: 16px; }
        
        /* SOCIAL BUTTONS */
        .divider { margin: 20px 0; font-size: 14px; color: #888; display: flex; align-items: center; justify-content: center; }
        .divider::before, .divider::after { content: ""; flex: 1; border-bottom: 1px solid var(--border-color); margin: 0 10px; }
        
        .social-btn { width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--card-bg); color: var(--text-color); cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; font-weight: 500; transition: 0.2s; }
        .social-btn:hover { background-color: var(--border-color); }
        .google-icon { color: #DB4437; }
        .github-icon { color: var(--text-color); }

        .link { margin-top: 15px; color: #007bff; cursor: pointer; font-size: 14px; }

        /* SUBJECTS */
        .subject-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px; }
        .subject-card { background: var(--card-bg); padding: 20px; border-radius: 12px; text-align: center; cursor: pointer; border: 2px solid transparent; transition: 0.2s; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .subject-card:hover { border-color: #007bff; transform: translateY(-2px); }
        .subject-icon { font-size: 30px; display: block; margin-bottom: 10px; }

        /* CHAT */
        #chat-history { flex: 1; overflow-y: auto; padding: 10px; display: flex; flex-direction: column; gap: 10px; }
        .message { padding: 10px 15px; border-radius: 15px; max-width: 80%; line-height: 1.4; font-size: 15px; }
        .user-msg { align-self: flex-end; background: var(--chat-user); color: white; border-bottom-right-radius: 2px; }
        .ai-msg { align-self: flex-start; background: var(--chat-ai); color: var(--chat-ai-text); border-bottom-left-radius: 2px; }
        
        .chat-input-area { padding: 10px; border-top: 1px solid var(--border-color); display: flex; gap: 10px; background: var(--bg-color); }
        .send-btn { width: 50px; background: #007bff; color: white; border: none; border-radius: 8px; cursor: pointer; }

    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <div class="title">🎓 AI Tutor Pro</div>
        <button class="theme-btn" onclick="toggleTheme()"><i class="fas fa-adjust"></i></button>
    </div>

    <!-- 1. LOGIN SCREEN -->
    <div id="screen-login" class="screen active">
        <div class="auth-box">
            <h2>Welcome Back</h2>
            <input type="text" id="login-email" placeholder="Email Address">
            <input type="password" id="login-pass" placeholder="Password">
            <button class="btn-primary" onclick="handleLogin('email')">Sign In</button>
            
            <div class="divider">OR CONTINUE WITH</div>
            
            <button class="social-btn" onclick="handleLogin('Google')">
                <i class="fab fa-google google-icon"></i> Google
            </button>
            <button class="social-btn" onclick="handleLogin('GitHub')">
                <i class="fab fa-github github-icon"></i> GitHub
            </button>

            <div class="link" onclick="showScreen('signup')">New here? Create Account</div>
        </div>
    </div>

    <!-- 2. SIGNUP SCREEN -->
    <div id="screen-signup" class="screen">
        <div class="auth-box">
            <h2>Create Account</h2>
            <input type="text" id="signup-name" placeholder="Full Name">
            <input type="email" id="signup-email" placeholder="Email Address">
            <input type="password" id="signup-pass" placeholder="Create Password">
            <button class="btn-primary" onclick="handleSignup()">Sign Up</button>
            
            <div class="link" onclick="showScreen('login')">Already have an account? Login</div>
        </div>
    </div>

    <!-- 3. DASHBOARD -->
    <div id="screen-dashboard" class="screen">
        <h3>Hi, <span id="user-name-display">Student</span>! 👋</h3>
        <p>Choose a subject to start learning:</p>
        <div class="subject-grid">
            <div class="subject-card" onclick="startChat('Math')"><span class="subject-icon">📐</span>Math</div>
            <div class="subject-card" onclick="startChat('Science')"><span class="subject-icon">🧬</span>Science</div>
            <div class="subject-card" onclick="startChat('History')"><span class="subject-icon">🏛️</span>History</div>
            <div class="subject-card" onclick="startChat('Coding')"><span class="subject-icon">💻</span>Coding</div>
            <div class="subject-card" onclick="startChat('English')"><span class="subject-icon">📖</span>English</div>
            <div class="subject-card" onclick="startChat('General')"><span class="subject-icon">🤖</span>Ask Anything</div>
        </div>
        <div class="link" onclick="logout()" style="color: #dc3545; margin-top: 30px;">Logout</div>
    </div>

    <!-- 4. CHAT -->
    <div id="screen-chat" class="screen" style="padding: 0; display: none; flex-direction: column;">
        <div style="padding: 10px; background: var(--card-bg); border-bottom: 1px solid var(--border-color); display: flex; align-items: center;">
            <button onclick="showScreen('dashboard')" style="background:none; border:none; font-size:18px; cursor:pointer; margin-right: 10px; color: var(--text-color);"><i class="fas fa-arrow-left"></i></button>
            <b id="chat-subject-title">Subject Tutor</b>
        </div>
        
        <div id="chat-history"></div>

        <div class="chat-input-area">
            <input type="text" id="user-msg" placeholder="Ask a question..." onkeypress="if(event.key==='Enter') sendMessage()">
            <button class="send-btn" onclick="sendMessage()"><i class="fas fa-paper-plane"></i></button>
        </div>
    </div>
</div>

<script>
    // --- THEME ---
    function toggleTheme() {
        const body = document.body;
        const newTheme = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        body.setAttribute('data-theme', newTheme);
    }

    // --- NAVIGATION ---
    function showScreen(id) {
        document.querySelectorAll('.screen').forEach(s => { s.classList.remove('active'); s.style.display = 'none'; });
        const t = document.getElementById('screen-' + id);
        t.classList.add('active');
        t.style.display = (id === 'chat') ? 'flex' : 'block';
    }

    // --- AUTH LOGIC ---
    let currentUser = "Student";

    function handleLogin(provider) {
        if(provider === 'email') {
            const email = document.getElementById('login-email').value;
            if(!email) return alert("Please enter email");
            currentUser = email.split('@')[0];
        } else {
            // Social Login Simulation
            currentUser = provider + " User";
        }
        document.getElementById('user-name-display').innerText = currentUser;
        showScreen('dashboard');
    }

    function handleSignup() {
        const name = document.getElementById('signup-name').value;
        if(!name) return alert("Please enter name");
        currentUser = name;
        document.getElementById('user-name-display').innerText = currentUser;
        showScreen('dashboard');
    }

    function logout() {
        showScreen('login');
    }

    // --- CHAT LOGIC ---
    let currentSubject = "";

    function startChat(subject) {
        currentSubject = subject;
        document.getElementById('chat-subject-title').innerText = subject;
        document.getElementById('chat-history').innerHTML = `<div class="message ai-msg">Hello! I am your <b>${subject}</b> Tutor. Ask me anything!</div>`;
        showScreen('chat');
    }

    async function sendMessage() {
        const input = document.getElementById('user-msg');
        const text = input.value.trim();
        if(!text) return;

        addMessage(text, 'user-msg');
        input.value = '';
        const loadingId = addMessage("Thinking...", 'ai-msg');

        try {
            const res = await fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ message: text, subject: currentSubject })
            });
            const data = await res.json();
            document.getElementById(loadingId).innerText = data.reply;
        } catch(e) {
            document.getElementById(loadingId).innerText = "Error connecting to AI.";
        }
    }

    function addMessage(text, cls) {
        const d = document.createElement('div');
        d.className = 'message ' + cls;
        d.innerHTML = text;
        d.id = 'msg-' + Date.now();
        const h = document.getElementById('chat-history');
        h.appendChild(d);
        h.scrollTop = h.scrollHeight;
        return d.id;
    }
</script>

</body>
</html>
"""
