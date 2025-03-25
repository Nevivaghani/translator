import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:5000/translate" 

st.title("Language Translator")

text_input = st.text_area("Enter text to translate:")
source_lang = st.text_input("Source Language (e.g., en, es, fr)", "en")
target_lang = st.text_input("Target Language (e.g., en, es, fr)", "fr")

if st.button("Translate"):
    if text_input:
        response = requests.post(BACKEND_URL, json={
            "text": text_input,
            "source_lang": source_lang,
            "target_lang": target_lang
        })
        
        if response.status_code == 200:
            translated_text = response.json().get("translated_text")
            st.success("Translated Text:")
            st.write(translated_text)
        else:
            st.error("Translation failed. Try again.")
    else:
        st.warning("Please enter text to translate.")

