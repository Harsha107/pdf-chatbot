import streamlit as st
from chatbot_core import build_qa_chain

st.set_page_config(page_title="PDF Chatbot", layout="wide")
st.title("Chat with your PDF")

qa_chain = build_qa_chain("2021A7PS0203U.pdf")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_input("What would you like to know from the PDF?", key="input")

if question:
    result = qa_chain({
        "question": question,
        "chat_history": st.session_state.chat_history
    })

    st.session_state.chat_history.append((question, result["answer"]))

    for i, (q, a) in enumerate(st.session_state.chat_history[::-1]):
        st.markdown(f"**Question {len(st.session_state.chat_history) - i}:** {q}")
        st.markdown(f"**Answer:** {a}")