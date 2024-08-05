#python
import streamlit as st
import time

# Title of the app
st.title('Streamlit Notepad with Repeat Feature')

# Text input from the user
user_input = st.text_area("Enter text here:")

# Start and stop buttons
start_button = st.button('Start Repeating')
stop_button = st.button('Stop Repeating')

# Session state to manage the repeating text
if 'repeat' not in st.session_state:
    st.session_state.repeat = False

# Start repeating text
if start_button:
    st.session_state.repeat = True
    st.write("Repeating started...")
    
    while st.session_state.repeat:
        st.write(user_input)
        time.sleep(2)  # Adjust the interval as needed
        # To allow UI to update
        st.experimental_rerun()

# Stop repeating text
if stop_button:
    st.session_state.repeat = False
    st.write("Repeating stopped.")


