import streamlit as st
st.title("My Simple App")
st.write("Welcome to my simple Streamlit app!")
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("hello ", name)