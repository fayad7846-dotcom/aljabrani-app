import streamlit as st
import google.generativeai as genai
import docx

# إعداد واجهة عضو النيابة الجبرني
st.set_page_config(page_title="عضو النيابة الجبرني", layout="wide")
st.title("⚖️ تطبيق عضو النيابة الجبرني")
st.info("مساعد الصياغة القضائية وفق المرشد التطبيقي")

# تفعيل محرك Gemini بمفتاحك
genai.configure(api_key="AIzaSyCkz_Jdoa-Ld8S4GtH5Jc0AVQhvkR8k29M")
model = genai.GenerativeModel('gemini-1.5-flash')

uploaded_file = st.file_uploader("ارفع ملف القضية (Word)", type=["doc", "docx"])

if uploaded_file:
    with st.spinner('⏳ جاري الصياغة القانونية...'):
        doc = docx.Document(uploaded_file)
        text = "\n".join([p.text for p in doc.paragraphs])
        prompt = f"أنت رئيس نيابة يمني. صحح هذا النص واستخرج البيانات وصغ القيد والوصف ومحضر الاطلاع وقائمة الأدلة وفق المرشد والموسوعة: {text}"
        response = model.generate_content(prompt)
        st.markdown(response.text)
