from dotenv import load_dotenv
load_dotenv()  ## loading all environment variables from .env file


import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# st.title('Gemini Pro')
st.set_page_config(page_title='Gemini Pro')
st.header("Gemini LLM App")

input = st.text_input("Input: ", key='input')
submit = st.button('Submit')


if submit:
    response = get_gemini_response(input)
    st.subheader("Response:")
    st.write(response)