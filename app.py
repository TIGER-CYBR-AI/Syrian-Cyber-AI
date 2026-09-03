import streamlit as st
from core import SyrianCyberAI

# إعداد الصفحة وتصميم الـ Cyberpunk بالألوان المضيئة
st.set_page_config(page_title="Syrian Cyber AI", layout="centered")

st.markdown("""
<style>
    body { background-color: #0a0f1d; }
    .reportview-container { background: #0a0f1d; }
    .stTextInput>div>div>input { color: #00ffcc; background-color: #131a30; border-color: #00ffcc; font-family: 'Courier New', monospace; }
    h1 { color: #00ffcc; text-align: center; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00ffcc; }
    .stSelectbox>div>div>div { color: #00ffcc; background-color: #131a30; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Syrian Cyber AI ⚡")

# عرض صورتك الشخصية الرقمية الفريدة كطابع رسمي لا يُنسى للمشروع
# تأكد من رفع صورتك إلى GitHub بنفس المجلد وتسميتها cyber_avatar.png
st.image("cyber_avatar.png", use_container_width=True)

password = st.text_input("Password:", type="password")

if password == "syria2026":
    api_key = st.text_input("OpenRouter API Key:", type="password")
    
    if api_key:
        # قائمة النماذج المجانية تماماً ومنزوعة الرقابة لعام 2026 على OpenRouter
        model_choice = st.selectbox(
            "Select Cyber AI Model (100% Free & Uncensored):",
            [
                "meta-llama/llama-3-8b-instruct:free", 
                "nousresearch/hermes-3-llama-3-8b:free",
                "openchat/openchat-7b:free"
            ]
        )
        
        # تهيئة الذكاء الاصطناعي وتحديث النموذج المختار
        if 'bot' not in st.session_state or st.session_state.current_model != model_choice:
            st.session_state.bot = SyrianCyberAI(api_key, model_choice)
            st.session_state.current_model = model_choice
            
        st.write("---")
        
        # ويدجت المايكروفون الصوتي الذكي (HTML5 Speech API) مجاني ومدمج بالكامل
        st.write("🎙️ *التحكم الصوتي اللحظي:* اضغط على زر المايك وتحدث بأمرك السيبراني:")
        
        st.components.v1.html("""
        <div style="display: flex; gap: 10px; align-items: center;">
            <button id="mic-btn" style="background-color: #131a30; color: #00ffcc; border: 2px solid #00ffcc; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold; font-family: monospace;">
                🎤 ابدأ التحدث بالقرار
            </button>
            <p id="status-text" style="color: #00ffcc; font-family: monospace; margin: 0;">جاهز لاستقبال صوتك الحاد...</p>
        </div>

        <script>
            const btn = document.getElementById('mic-btn');
            const status = document.getElementById('status-text');
            
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (SpeechRecognition) {
                const recognition = new SpeechRecognition();
                recognition.lang = 'ar-SY'; // التعرف على اللهجة السورية والعربية بدقة
                
                btn.onclick = () => {
                    recognition.start();
                    status.innerText = "⚡ جاري الاستماع لصوتك...";
                    btn.style.borderColor = "#ff007f";
                };
                
                recognition.onresult = (event) => {
                    const textResult = event.results[0][0].transcript;
                    status.innerText = "✔️ تم التقاط الأوامر: " + textResult;
                    btn.style.borderColor = "#00ffcc";
                    
                    // إرسال النص الملتقط صوتياً مباشرة إلى حقل إدخال Streamlit
                    window.parent.postMessage({type: 'streamlit:setComponentValue', value: textResult}, '*');
                };
            } else {
                status.innerText = "❌ متصفحك لا يدعم التقاط الصوت المباشر.";
            }
        </script>
        """, height=60)

        # استقبال الأمر النهائي سواء تم نطقه بالمايك أو كتابته يدوياً
        command = st.text_input("Confirm / Type Cyber Command manually:")
        
        if command:
            st.write("### 📝 الرد السيبراني المباشر:")
            response_placeholder = st.empty()
            full_response = ""
            
            with st.spinner("🤖 جاري التفكير والتحليل سحابياً..."):
                # استدعاء البث اللحظي الحرفي من ملف core
                for chunk in st.session_state.bot.execute_cyber_command_stream(command):
                    full_response += chunk
                    response_placeholder.code(full_response, language="python")
