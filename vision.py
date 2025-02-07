from dotenv import load_dotenv
load_dotenv()  ## loading all environment variables from .env file


import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input, image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text
    
# st.title('Gemini Pro')
st.set_page_config(page_title='Gemini Pro')
st.header("Gemini LLM App")

input = st.text_input("Input: ", key='input',value="describe image")


uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button('Submit')
if submit:
    response = get_gemini_response(input, image)
    st.subheader("Response:")
    st.write(response)