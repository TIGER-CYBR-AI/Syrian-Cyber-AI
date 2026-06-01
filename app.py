import streamlit as st
import os
import base64
from gtts import gTTS
from core import SyrianCyberAI

st.set_page_config(page_title="Syrian Cyber AI", layout="centered")

# تصميم سيبراني فخم للواجهة والمجسم
st.markdown("""
<style>
    .reportview-container { background: #0a0f1d; }
    .stTextInput>div>div>input { color: #00ffcc; background-color: #131a30; border-color: #00ffcc; }
    h1 { color: #00ffcc; text-align: center; font-family: 'Courier New', monospace; }
</style>
""", unsafe_allow_index=True)

st.title("⚡ Syrian Cyber AI ⚡")

# 🔑 بوابة الأمان للبرنامج المستقل
password = st.text_input("Password:", type="password")

if password == "syria2026":
    api_key = st.text_input("Gemini API Key:", type="password")
    
    if api_key:
        # استدعاء العقل المستقل من ملف core
        if 'bot' not in st.session_state:
            st.session_state.bot = SyrianCyberAI(api_key)
        
        st.write("---")
        
        # 🎭 عرض المجسم السيبراني التفاعلي (صورة متحركة GIF كمحاكاة هولوغرام)
        # يمكنك استبدال الرابط أدناه برابط أي مجسم تفاعلي تريده لاحقاً
        avatar_url = "https://giphy.com"
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image(avatar_url, caption="🤖 Syrian Cyber AI Avatar", use_container_width=True)
        
        # 🎙️ إدخال الأوامر البرمجية والسيبرانية
        command = st.text_input("Enter Cyber Command / Question:")
        
        if command:
            with st.spinner("🤖 التفكير في الأمر السيبراني وتحليله..."):
                response_text = st.session_state.bot.execute_cyber_command(command)
            
            # عرض الرد المكتوب
            st.write("### 📝 الرد البرمجي:")
            st.code(response_text, language="python")
            
            # 🔊 تحويل الرد إلى صوت مسموع فوراً
            tts = gTTS(text=response_text, lang='ar', slow=False)
            tts.save("response.mp3")
            
            # تشغيل الصوت تلقائياً في الخلفية متزامناً مع المجسم
            with open("response.mp3", "rb") as f:
                audio_bytes = f.read()
            audio_base64 = base64.b64encode(audio_bytes).decode()
            audio_html = f'<audio src="data:audio/mp3;base64,{audio_base64}" autoplay>'
            st.markdown(audio_html, unsafe_allow_allow_html=True)
            st.success("🔊 تحدث المساعد بنجاح!")
