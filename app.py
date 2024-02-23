import streamlit as st
import ollama
import time


def llm_model():
    prompt = st.chat_input("Ask anything")

    if prompt:
        with st.chat_message("user"):
            st.write(prompt)
            
        with st.spinner("Progess..."):
            result = ollama.chat(model="gemma", messages=[{"role":"user", "content":prompt}])
            response = result["message"]["content"]
            
            st.write(response)

def main():
    llm_model()

if __name__ == "__main__":
    main()
    
    