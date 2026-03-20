import streamlit as st

st.title("Vizzy Chatbot")
st.write("Welcome to Vizzy Chat 🚀")

user_input = st.text_input("Type your prompt:")
if user_input:
    st.write(f"You entered: {user_input}")

