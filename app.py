import streamlit as st
from groq import Groq

st.set_page_config(page_title="Ultra AI Chatbot", page_icon="🤖")

st.title("⚡ Ultra-Fast AI Chatbot")
st.write("Powered by Groq & Llama 3")

# API Key input securely
api_key = st.text_input("Enter your Groq API Key:", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        # Sabse stable aur active model
        model_name = "llama-3.1-8b-instant"

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
                        st.error(f"API Error: {e}")
    except Exception as e:
        st.error(f"Connection Error: {e}")
else:
    st.warning("Please enter your Groq API Key above to start chatting.")
    
