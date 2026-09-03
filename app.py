import streamlit as st
from core import SyrianCyberAI

st.set_page_config(page_title="Syrian Cyber AI", layout="centered")

# تصميم فاخر ومرعب بلون التيركواز الفلوري والخلفية المظلمة للهكرز
st.markdown("""
<style>
    .reportview-container { background: #0a0f1d; }
    .stTextInput>div>div>input { color: #00ffcc; background-color: #131a30; border-color: #00ffcc; }
    h1 { color: #00ffcc; text-align: center; font-family: 'Courier New', monospace; }
    .stSelectbox>div>div>div { color: #00ffcc; background-color: #131a30; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Syrian Cyber AI ⚡")

password = st.text_input("Password:", type="password")

if password == "syria2026":
    api_key = st.text_input("OpenRouter API Key:", type="password")
    
    if api_key:
        # صندوق اختيار النماذج غير المراقبة والمجانية تماماً لعام 2026
        model_choice = st.selectbox(
            "Select Cyber AI Model (100% Free & Uncensored):",
            [
                "meta-llama/llama-3-8b-instruct:free", 
                "nousresearch/hermes-3-llama-3-8b:free",
                "openchat/openchat-7b:free"
            ]
        )
        
        # تهيئة البوت وتحديث النموذج المختار
        if 'bot' not in st.session_state or st.session_state.current_model != model_choice:
            st.session_state.bot = SyrianCyberAI(api_key, model_choice)
            st.session_state.current_model = model_choice
        
        st.write("---")
        
        command = st.text_input("Enter Cyber Command / Question:")
        
        if command:
            st.write("### 📝 الرد البرمجي اللحظي:")
            
            # تشغيل تأثير البث الحي (Streaming) لكتابة الأكواد فوراً
            with st.spinner("🤖 جاري تحليل واختراق النظام سحابياً..."):
                response_placeholder = st.empty()
                full_response = ""
                
                # استدعاء الدالة السحابية من ملف core.py
                for chunk in st.session_state.bot.execute_cyber_command_stream(command):
                    full_response += chunk
                    response_placeholder.code(full_response, language="python")
