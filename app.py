import streamlit as st
import os
import base64
from gtts import gTTS
from core import SyrianCyberAI  # يستدعي الملف الأول الذي قمنا بتحديثه للتو

st.set_page_config(page_title="Syrian Cyber AI", layout="centered")

# تصميم سيبراني فخم متوافق مع البيئة المظلمة للأمن السيبراني
st.markdown("""
<style>
    .reportview-container { background: #0a0f1d; }
    .stTextInput>div>div>input { color: #00ffcc; background-color: #131a30; border-color: #00ffcc; }
    h1 { color: #00ffcc; text-align: center; font-family: 'Courier New', monospace; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Syrian Cyber AI ⚡")

# 🔑 بوابة الأمان والتحقق للدخول للبرنامج المستقل
password = st.text_input("Password:", type="password")

if password == "syria2026":
    # تم تحديثه هنا ليطلب مفتاح OpenRouter بدلاً من Gemini لتفادي الحظر والرفض
    api_key = st.text_input("OpenRouter API Key:", type="password")
    
    if api_key:
        # استدعاء وبناء كائن الذكاء الاصطناعي من ملف core
        if 'bot' not in st.session_state:
            st.session_state.bot = SyrianCyberAI(api_key)
        
        st.write("---")
        
        # 🎭 عرض المجسم السيبراني التفاعلي (رابط مباشر لصورة متحركة تتناسب مع التصميم المظلم)
        avatar_url = "https://giphy.com"
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(avatar_url, caption="🤖 Syrian Cyber AI Avatar", use_container_width=True)
        
        # 🎙️ واجهة إدخال الأوامر البرمجية والسيبرانية
        command = st.text_input("Enter Cyber Command / Question:")
        
        if command:
            with st.spinner("🤖 جاري تحليل الأمر السيبراني عبر سحابة OpenRouter المفتوحة..."):
                response_text = st.session_state.bot.execute_cyber_command(command)
            
            # عرض الرد التقني المكتوب
            st.write("### 📝 الرد البرمجي:")
            st.code(response_text, language="python")
            
            # 🔊 تحويل الرد إلى صوت مسموع فوراً باللغة العربية
            # نقوم بتصفية النصوص لتجنب قراءة الرموز البرمجية الطويلة صوتياً
            voice_text = response_text.split("```")[0] if "```" in response_text else response_text
            if voice_text.strip():
                tts = gTTS(text=voice_text, lang='ar', slow=False)
                tts.save("response.mp3")
                
                # تشغيل الصوت تلقائياً في خلفية المتصفح بالتزامن مع حركة الواجهة
                with open("response.mp3", "rb") as f:
                    audio_bytes = f.read()
                audio_base64 = base64.b64encode(audio_bytes).decode()
                audio_html = f'<audio src="data:audio/mp3;base64,{audio_base64}" autoplay>'
                st.markdown(audio_html, unsafe_allow_html=True)
                st.success("🔊 تحدث المساعد بنجاح!")
