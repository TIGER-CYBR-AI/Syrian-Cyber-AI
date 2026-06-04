import streamlit as st
import os
import base64
from gtts import gTTS
from core import SyrianCyberAI

st.set_page_config(page_title="Syrian Cyber AI", layout="centered")

# تصميم سيبراني فخم
st.markdown("""
<style>
    .reportview-container { background: #0a0f1d; }
    .stTextInput>div>div>input { color: #00ffcc; background-color: #131a30; border-color: #00ffcc; }
    h1 { color: #00ffcc; text-align: center; font-family: 'Courier New', monospace; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Syrian Cyber AI ⚡")

# بوابة الأمان
password = st.text_input("Password:", type="password")

if password == "syria2026":
    api_key = st.text_input("OpenRouter API Key:", type="password")
    
    if api_key:
        if 'bot' not in st.session_state:
            st.session_state.bot = SyrianCyberAI(api_key)
        
        st.write("---")
        
        avatar_url = "https://giphy.com"
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image(avatar_url, caption="🤖 Syrian Cyber AI Avatar", use_container_width=True)
        
        command = st.text_input("Enter Cyber Command / Question:")
        
        if command:
            with st.spinner("🤖 جاري تحليل الأمر السيبراني..."):
                response_text = st.session_state.bot.execute_cyber_command(command)
            
            # عرض الرد التقني المكتوب
            st.write("### 📝 الرد البرمجي:")
            st.code(response_text, language="python")
            
            # 🔊 حماية برمجية لمنع انهيار ميزة الصوت في حال وجود أخطاء في الرد
            try:
                # تصفية النص من الأكواد لقرائته بشكل صحيح
                voice_text = response_text.split("```")[0] if "```" in response_text else response_text
                # إزالة الرموز الغريبة التي قد تعطّل المكتبة
                voice_text = "".join([c for c in voice_text if c.isalnum() or c.isspace()])
                
                if voice_text.strip():
                    tts = gTTS(text=voice_text[:200], lang='ar', slow=False)  # حد أقصى 200 حرف للصوت
                    tts.save("response.mp3")
                    
                    with open("response.mp3", "rb") as f:
                        audio_bytes = f.read()
                    audio_base64 = base64.b64encode(audio_bytes).decode()
                    audio_html = f'<audio src="data:audio/mp3;base64,{audio_base64}" autoplay>'
                    st.markdown(audio_html, unsafe_allow_html=True)
                    st.success("🔊 تحدث المساعد بنجاح!")
            except Exception as e:
                st.warning("⚠️ لم يتمكن المساعد من النطق بالصوت، ولكن الرد المكتوب متوفر بالأعلى.")

