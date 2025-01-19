import streamlit as st
from agent import ask_question

st.title("RAG-powered Chatbot with LangChain")

# Input box for questions
user_question = st.text_input("Ask a question:")

if st.button("Submit"):
  if user_question:
    response = ask_question(user_question)
    st.write("Answer:", response)
else:
    st.warning("Please enter a question.")
