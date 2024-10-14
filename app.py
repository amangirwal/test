import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

# Text Input
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

# Slider
age = st.slider("How old are you?", 0, 100, 25)
st.write(f"You are {age} years old.")
