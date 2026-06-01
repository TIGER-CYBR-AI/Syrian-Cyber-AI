import os
import json
import google.generativeai as genai

class SyrianCyberAI:
    def __init__(self, api_key):
        # الاتصال السحابي بالذكاء الاصطناعي
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.system_prompt = "أنت Syrian Cyber AI، وكيل أمن سيبراني مستقل ذكي جداً. مهمتك الحماية، فحص الثغرات، والتنفيذ بطلب مسبق."
        self.memory_file = "cyber_memory.json"
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_memory(self):
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.memory, f, ensure_ascii=False, indent=4)

    def execute_cyber_command(self, command):
        full_prompt = f"{self.system_prompt}\nالذاكرة السابقة: {self.memory}\nالأمر الحالي: {command}"
        response = self.model.generate_content(full_prompt)
        
        # حفظ ما تم تعلمه وتنفيذه في الذاكرة المستقلة
        self.memory.append({"command": command, "response": response.text})
        self.save_memory()
        return response.text
