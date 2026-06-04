import streamlit as st
from core import SyrianCyberAI

st.set_page_config(page_title="Syrian Cyber AI", layout="centered")

st.markdown("""
<style>
    .reportview-container { background: #0a0f1d; }
    .stTextInput>div>div>input { color: #00ffcc; background-color: #131a30; border-color: #00ffcc; }
    h1 { color: #00ffcc; text-align: center; font-family: 'Courier New', monospace; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Syrian Cyber AI ⚡")

password = st.text_input("Password:", type="password")

if password == "syria2026":
    api_key = st.text_input("OpenRouter API Key:", type="password")
    
    if api_key:
        if 'bot' not in st.session_state:
            st.session_state.bot = SyrianCyberAI(api_key)
        
        st.write("---")
        
        command = st.text_input("Enter Cyber Command / Question:")
        
        if command:
            with st.spinner("🤖 جاري معالجة الأمر..."):
                response_text = st.session_state.bot.execute_cyber_command(command)
            
            st.write("### 📝 الرد البرمجي:")
            st.code(response_text, language="python")

