import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(page_title="Ultra AI Chatbot", page_icon="⚡", layout="centered")

st.title("⚡ Ultra-Fast AI Chatbot")
st.write("Powered by Groq & Llama 3 - Faster than ChatGPT & Gemini!")

# Initialize Groq client securely using user's API Key
api_key = st.text_input("Enter your Groq API Key:", type="password")

if api_key:
    client = Groq(api_key=api_key)
    
    # Select model
    model_name = "llama-3.1-70b-versatile" # Ultra fast and accurate model

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("What would you like to know?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response from Groq
        with st.chat_message("assistant"):
            with st.spinner("Thinking at lightning speed..."):
                try:
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        model=model_name,
                    )
                    response = chat_completion.choices[0].message.content
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(e)
else:
    st.warning("Please enter your Groq API Key above to start chatting.")
                          
