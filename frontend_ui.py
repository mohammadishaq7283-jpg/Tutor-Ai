HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>AI Tutor Pro</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-color: #ffffff;
            --text-color: #333333;
            --sidebar-bg: #f4f4f9;
            --card-bg: #f8f9fa;
            --input-bg: #f0f2f5;
            --border-color: #ddd;
            --chat-user: #007bff;
            --chat-ai: #e9ecef;
            --chat-ai-text: #333;
        }

        [data-theme="dark"] {
            --bg-color: #121212;
            --text-color: #e0e0e0;
            --sidebar-bg: #1a1a1a;
            --card-bg: #1e1e1e;
            --input-bg: #2d2d2d;
            --border-color: #444;
            --chat-user: #bb86fc;
            --chat-ai: #333333;
            --chat-ai-text: #fff;
        }

        * { box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background-color: var(--bg-color); color: var(--text-color); margin: 0; padding: 0; display: flex; height: 100vh; overflow: hidden; }
        
        /* SIDEBAR */
        .sidebar {
            width: 260px; background: var(--sidebar-bg); border-right: 1px solid var(--border-color);
            display: flex; flex-direction: column; padding: 10px;
            position: absolute; left: -260px; top: 0; height: 100%; z-index: 1000;
            transition: 0.3s ease; box-shadow: 2px 0 5px rgba(0,0,0,0.1);
        }
        .sidebar.open { left: 0; }
        .sidebar-header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 10px; border-bottom: 1px solid var(--border-color); }
        .new-chat-btn { width: 100%; padding: 10px; margin-top: 10px; background: var(--chat-user); color: white; border: none; border-radius: 5px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 5px; }
        .history-list { flex: 1; overflow-y: auto; margin-top: 10px; }
        .history-item { padding: 10px; border-radius: 5px; cursor: pointer; color: var(--text-color); margin-bottom: 5px; font-size: 14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .history-item:hover { background: var(--card-bg); }
        
        /* MAIN LAYOUT */
        .main-content { flex: 1; display: flex; flex-direction: column; width: 100%; height: 100%; position: relative; }
        
        .header { flex-shrink: 0; padding: 10px 15px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); background: var(--bg-color); z-index: 10; }
        .header-left { display: flex; align-items: center; gap: 15px; }
        .menu-btn { background: none; border: none; font-size: 20px; cursor: pointer; color: var(--text-color); }
        .title { font-weight: bold; font-size: 18px; }
        
        .auth-btn-top {
            padding: 5px 12px; border-radius: 20px; font-size: 14px; font-weight: bold; cursor: pointer; text-decoration: none; border: 1px solid var(--chat-user); display: flex; align-items: center; gap: 5px;
        }
        .btn-signin { background: transparent; color: var(--chat-user); }
        .btn-profile { background: var(--chat-user); color: white; }

        /* SCREENS CONTAINER */
        /* Important: flex: 1 ensures it takes remaining space, overflow: hidden prevents double scroll */
        .screen-container { flex: 1; position: relative; overflow: hidden; display: flex; flex-direction: column; }

        .screen { display: none; width: 100%; height: 100%; overflow-y: auto; padding: 20px; }
        .screen.active { display: block; }
        
        /* SPECIAL FIX FOR CHAT SCREEN LAYOUT */
        #screen-chat.active {
            display: flex;
            flex-direction: column;
            padding: 0; /* Remove padding for chat screen to fit bars */
            overflow: hidden; /* Handle inner scroll instead */
        }

        /* Chat Header */
        .chat-header-bar {
            flex-shrink: 0;
            padding: 10px; background: var(--card-bg); border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between;
        }

        /* Chat History (Scrollable Area) */
        #chat-history { 
            flex: 1; 
            overflow-y: auto; 
            padding: 15px; 
            display: flex; 
            flex-direction: column; 
            gap: 15px; 
            scroll-behavior: smooth;
        }

        /* INPUT AREA (FIXED BOTTOM) */
        .chat-input-area { 
            flex-shrink: 0; /* Never shrink */
            padding: 10px; 
            border-top: 1px solid var(--border-color); 
            display: flex; 
            gap: 10px; 
            background: var(--bg-color); 
            align-items: center; 
        }

        /* Input Wrapper for Camera */
        .input-wrapper { 
            flex: 1; 
            position: relative; 
            display: flex; 
            align-items: center; 
            background: var(--input-bg);
            border-radius: 25px;
            border: 1px solid var(--border-color);
            padding: 0 10px;
        }

        .chat-input-area input { 
            width: 100%; 
            padding: 12px; 
            padding-right: 35px; /* Space for camera icon */
            border: none; 
            background: transparent; 
            color: var(--text-color); 
            outline: none;
            font-size: 16px;
        }
        
        .camera-btn { 
            position: absolute; 
            right: 10px; 
            background: none; 
            border: none; 
            color: #888; 
            font-size: 20px; 
            cursor: pointer; 
            padding: 5px;
        }
        .camera-btn:hover { color: var(--chat-user); }

        .send-btn { 
            width: 45px; height: 45px; 
            background: var(--chat-user); 
            color: white; 
            border: none; 
            border-radius: 50%; 
            cursor: pointer; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            font-size: 18px;
            flex-shrink: 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }

        /* AUTH & DASHBOARD STYLES */
        .auth-box { background: var(--card-bg); padding: 25px; border-radius: 12px; max-width: 400px; margin: 20px auto; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; }
        .auth-box input, .auth-box select { width: 100%; padding: 12px; margin: 8px 0; border-radius: 8px; border: 1px solid var(--border-color); background: var(--input-bg); color: var(--text-color); }
        .btn-primary { width: 100%; padding: 12px; background: #007bff; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        .link { margin-top: 15px; color: #007bff; cursor: pointer; font-size: 14px; }
        .guest-link { margin-top: 10px; color: #888; cursor: pointer; font-size: 14px; text-decoration: underline; }

        .subject-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 20px; max-width: 600px; width: 100%; align-self: center; }
        .subject-card { background: var(--card-bg); padding: 20px; border-radius: 12px; text-align: center; cursor: pointer; border: 1px solid var(--border-color); transition: 0.2s; }
        .subject-card:hover { border-color: #007bff; transform: translateY(-2px); }
        .subject-icon { font-size: 28px; display: block; margin-bottom: 5px; }

        .message { padding: 10px 15px; border-radius: 15px; max-width: 85%; line-height: 1.5; font-size: 15px; }
        .user-msg { align-self: flex-end; background: var(--chat-user); color: white; border-bottom-right-radius: 2px; }
        .ai-msg { align-self: flex-start; background: var(--chat-ai); color: var(--chat-ai-text); border-bottom-left-radius: 2px; }

        .overlay-bg { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 900; display: none; }
        #loading-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); display: none; justify-content: center; align-items: center; flex-direction: column; z-index: 2000; color: white; }
        .spinner { border: 4px solid #f3f3f3; border-top: 4px solid #007bff; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin-bottom: 10px; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    </style>
</head>
<body>

<!-- SIDEBAR -->
<div class="sidebar" id="sidebar">
    <div class="sidebar-header">
        <span style="font-weight:bold;">History</span>
        <button onclick="toggleSidebar()" style="background:none; border:none; font-size:20px; cursor:pointer;">&times;</button>
    </div>
    <button class="new-chat-btn" onclick="startNewChat()">
        <i class="fas fa-plus"></i> New Chat
    </button>
    <div class="history-list" id="history-list"></div>
</div>
<div class="overlay-bg" id="sidebar-overlay" onclick="toggleSidebar()"></div>

<!-- MAIN APP -->
<div class="main-content">
    
    <div class="header">
        <div class="header-left">
            <button class="menu-btn" onclick="toggleSidebar()"><i class="fas fa-bars"></i></button>
            <div class="title">AI Tutor</div>
        </div>
        <div class="header-right" style="display:flex; align-items:center; gap:10px;">
            <div id="top-auth-btn"></div>
            <button class="menu-btn" onclick="toggleTheme()"><i class="fas fa-adjust"></i></button>
        </div>
    </div>

    <!-- LOADING SCREEN -->
    <div id="loading-overlay">
        <div class="spinner"></div>
        <div id="loading-text">Loading...</div>
    </div>

    <div class="screen-container">
        <!-- 1. LOGIN SCREEN -->
        <div id="screen-login" class="screen">
            <div class="auth-box">
                <h2>Welcome</h2>
                <select id="login-lang">
                    <option value="English">English</option>
                    <option value="Urdu">Urdu (اردو)</option>
                    <option value="Hindi">Hindi (हिंदी)</option>
                </select>
                <input type="text" id="login-email" placeholder="Email / Username">
                <input type="password" id="login-pass" placeholder="Password">
                <button class="btn-primary" onclick="handleLogin()">Sign In</button>
                <div class="link" onclick="showScreen('signup')">Create Account</div>
                <div class="guest-link" onclick="continueAsGuest()">Skip & Continue as Guest &rarr;</div>
            </div>
        </div>

        <!-- 2. SIGNUP SCREEN -->
        <div id="screen-signup" class="screen">
            <div class="auth-box">
                <h2>Join AI Tutor</h2>
                <select id="signup-lang">
                    <option value="English">English</option>
                    <option value="Urdu">Urdu</option>
                </select>
                <input type="text" id="signup-name" placeholder="Full Name">
                <input type="email" id="signup-email" placeholder="Email">
                <input type="password" id="signup-pass" placeholder="Password">
                <button class="btn-primary" onclick="handleSignup()">Sign Up</button>
                <div class="link" onclick="showScreen('login')">Have an account? Login</div>
                <div class="guest-link" onclick="continueAsGuest()">Skip & Continue as Guest &rarr;</div>
            </div>
        </div>

        <!-- 3. DASHBOARD -->
        <div id="screen-dashboard" class="screen">
            <div style="text-align: center; margin-top: 20px;">
                <h3>Hello, <span id="user-name-display">Student</span>!</h3>
                <p>What do you want to learn?</p>
            </div>
            
            <div class="subject-grid">
                <div class="subject-card" onclick="startChat('Ask Anything')">
                    <span class="subject-icon" style="color:#f39c12">✨</span><b>Ask Anything</b>
                </div>
                <div class="subject-card" onclick="startChat('Math')"><span class="subject-icon">📐</span>Math</div>
                <div class="subject-card" onclick="startChat('Science')"><span class="subject-icon">🧬</span>Science</div>
                <div class="subject-card" onclick="startChat('History')"><span class="subject-icon">🏛️</span>History</div>
                <div class="subject-card" onclick="startChat('Coding')"><span class="subject-icon">💻</span>Coding</div>
                <div class="subject-card" onclick="startChat('English')"><span class="subject-icon">📖</span>English</div>
            </div>
        </div>

        <!-- 4. CHAT SCREEN (Fixed Layout) -->
        <div id="screen-chat" class="screen">
            <div class="chat-header-bar">
                <div style="display:flex; align-items:center;">
                    <button onclick="showScreen('dashboard')" style="background:none; border:none; font-size:18px; cursor:pointer; margin-right: 10px; color: var(--text-color);"><i class="fas fa-arrow-left"></i></button>
                    <b id="chat-subject-title">Subject</b>
                </div>
                <small id="lang-display" style="color:#888;">En</small>
            </div>
            
            <div id="chat-history"></div>

            <div class="chat-input-area">
                <input type="file" id="camera-input" accept="image/*" capture="environment" style="display: none;" onchange="handleImageSelect()">
                
                <div class="input-wrapper">
                    <input type="text" id="user-msg" placeholder="Type a message..." onkeypress="if(event.key==='Enter') sendMessage()">
                    <button class="camera-btn" onclick="triggerCamera()"><i class="fas fa-camera"></i></button>
                </div>
                <button class="send-btn" onclick="sendMessage()"><i class="fas fa-paper-plane"></i></button>
            </div>
        </div>
    </div>

</div>

<script>
    let currentUser = "Guest";
    let currentLang = "English";
    let isGuest = true;
    let chatSessions = JSON.parse(localStorage.getItem('chatSessions')) || [];

    document.addEventListener("DOMContentLoaded", () => {
        const theme = localStorage.getItem('theme') || 'light';
        document.body.setAttribute('data-theme', theme);

        const savedUser = localStorage.getItem('tutorUser');
        const savedLang = localStorage.getItem('tutorLang');
        
        updateHistoryUI();

        if(savedUser && savedUser !== "Guest") {
            currentUser = savedUser;
            currentLang = savedLang || "English";
            isGuest = false;
            updateUIState();
            showScreen('dashboard');
        } else {
            showScreen('login');
            updateUIState();
        }
    });

    function updateUIState() {
        const authBtn = document.getElementById('top-auth-btn');
        const nameDisplay = document.getElementById('user-name-display');
        nameDisplay.innerText = currentUser;

        if (isGuest) {
            authBtn.innerHTML = `<span class="auth-btn-top btn-signin" onclick="goToLogin()">Sign In</span>`;
        } else {
            authBtn.innerHTML = `<span class="auth-btn-top btn-profile" onclick="if(confirm('Logout?')) logout()"><i class="fas fa-user-circle"></i> ${currentUser}</span>`;
        }
    }

    function continueAsGuest() {
        currentUser = "Guest";
        currentLang = "English";
        isGuest = true;
        updateUIState();
        showScreen('dashboard');
    }

    function loginSuccess(name, lang) {
        showLoading("Signing in...", () => {
            currentUser = name;
            currentLang = lang;
            isGuest = false;
            localStorage.setItem('tutorUser', currentUser);
            localStorage.setItem('tutorLang', currentLang);
            updateUIState();
            showScreen('dashboard');
        });
    }

    function handleLogin() {
        const email = document.getElementById('login-email').value;
        const lang = document.getElementById('login-lang').value;
        if(!email) return alert("Enter ID");
        loginSuccess(email.split('@')[0], lang);
    }

    function handleSignup() {
        const name = document.getElementById('signup-name').value;
        const lang = document.getElementById('signup-lang').value;
        if(!name) return alert("Enter Name");
        loginSuccess(name, lang);
    }

    function logout() {
        localStorage.removeItem('tutorUser');
        currentUser = "Guest";
        isGuest = true;
        updateUIState();
        showScreen('login');
    }

    function goToLogin() { showScreen('login'); }
    function toggleSidebar() { 
        document.getElementById('sidebar').classList.toggle('open');
        const overlay = document.getElementById('sidebar-overlay');
        overlay.style.display = overlay.style.display === 'block' ? 'none' : 'block';
    }
    function toggleTheme() {
        const body = document.body;
        const newTheme = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        body.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
    }
    function showLoading(txt, cb) {
        const ov = document.getElementById('loading-overlay');
        document.getElementById('loading-text').innerText = txt;
        ov.style.display = 'flex';
        setTimeout(() => { ov.style.display = 'none'; cb(); }, 1500);
    }

    function showScreen(id) {
        document.querySelectorAll('.screen').forEach(s => { 
            s.classList.remove('active'); 
            // Important: only hide non-active screens
            if(s.id !== 'screen-'+id) s.style.display = 'none';
        });
        const t = document.getElementById('screen-' + id);
        t.classList.add('active');
        // Important CSS Reset
        t.style.display = (id === 'chat') ? 'flex' : 'block';
    }

    function startNewChat() { toggleSidebar(); showScreen('dashboard'); }
    function startChat(subject) {
        currentSubject = subject;
        document.getElementById('chat-subject-title').innerText = subject;
        document.getElementById('lang-display').innerText = currentLang.substring(0,2);
        let greeting = isGuest ? "Hello Guest!" : `Hello ${currentUser}!`;
        document.getElementById('chat-history').innerHTML = `<div class="message ai-msg">${greeting} I am your <b>${subject}</b> Tutor.</div>`;
        addToHistory(subject);
        showScreen('chat');
    }
    
    function addToHistory(sub) {
        const date = new Date().toLocaleDateString();
        const entry = { subject: sub, date: date, id: Date.now() };
        if(chatSessions.length > 0 && chatSessions[0].subject === sub) return;
        chatSessions.unshift(entry);
        if(chatSessions.length > 10) chatSessions.pop();
        localStorage.setItem('chatSessions', JSON.stringify(chatSessions));
        updateHistoryUI();
    }
    
    function updateHistoryUI() {
        const list = document.getElementById('history-list');
        list.innerHTML = chatSessions.map(s => `<div class="history-item" onclick="startChat('${s.subject}'); toggleSidebar();"><i class="far fa-comments"></i> ${s.subject}</div>`).join('');
    }

    function triggerCamera() { document.getElementById('camera-input').click(); }
    function handleImageSelect() { alert("Image selected! (Image analysis feature coming soon)"); }

    async function sendMessage() {
        const input = document.getElementById('user-msg');
        const text = input.value.trim();
        if(!text) return;
        addMessage(text, 'user-msg');
        input.value = '';
        const loadingId = addMessage("Thinking...", 'ai-msg');
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 15000);
        try {
            const res = await fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ message: text, subject: currentSubject, language: currentLang }),
                signal: controller.signal
            });
            clearTimeout(timeoutId);
            const data = await res.json();
            document.getElementById(loadingId).innerText = data.reply;
        } catch(e) {
            document.getElementById(loadingId).innerText = "⚠️ Network Error.";
        }
    }

    function addMessage(text, cls) {
        const d = document.createElement('div');
        d.className = 'message ' + cls;
        d.innerHTML = text;
        const h = document.getElementById('chat-history');
        h.appendChild(d);
        h.scrollTop = h.scrollHeight;
        return d;
    }
</script>

</body>
</html>
"""
