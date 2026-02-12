    async function sendMessage() {
        const input = document.getElementById('user-msg');
        const text = input.value.trim();
        if(!text) return;

        addMessage(text, 'user-msg');
        input.value = '';
        
        // Loading ID save karein
        const loadingId = addMessage("Thinking...", 'ai-msg');

        // Timeout Logic (Agar 15 second tak jawab na aaye)
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 15000); // 15 Seconds Limit

        try {
            const res = await fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ 
                    message: text, 
                    subject: currentSubject,
                    language: currentLang 
                }),
                signal: controller.signal // Signal pass karein
            });
            
            clearTimeout(timeoutId); // Agar jawab aa gaya to timer rok dein
            const data = await res.json();
            document.getElementById(loadingId).innerText = data.reply;
            
        } catch(e) {
            if (e.name === 'AbortError') {
                document.getElementById(loadingId).innerText = "⚠️ Network Timeout. The answer was too long. Please ask a shorter question.";
            } else {
                document.getElementById(loadingId).innerText = "Connection Error. Please try again.";
            }
        }
    }
