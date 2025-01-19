import streamlit as st
from agent import get_response

st.title("AI Agent with LangChain and Gemini")

# User input
user_input = st.text_input("Ask a question:")

if st.button("Submit"):
    if user_input:
        response = get_response(user_input)
        st.write("Response:", response)
    else:
        st.warning("Please enter a question.")
