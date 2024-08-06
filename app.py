import streamlit as st
import time

# Title of the app
st.title('Streamlit Notepad with Repeat Feature')

# Text input from the user
user_input = st.text_area("Enter text here:")

# Start and stop buttons
start_button = st.button('Start Repeating')
stop_button = st.button('Stop Repeating')

# Initialize session state
if 'repeat' not in st.session_state:
    st.session_state.repeat = False

# Function to repeat text
def repeat_text():
    while st.session_state.repeat:
        st.write(user_input)
        time.sleep(2)  # Adjust the interval as needed
        # Trigger a rerun by modifying session state
        st.session_state.repeat = not st.session_state.repeat
        st.session_state.repeat = not st.session_state.repeat

# Start repeating text
if start_button:
    st.session_state.repeat = True
    st.write("Repeating started...")
    repeat_text()

# Stop repeating text
if stop_button:
    st.session_state.repeat = False
    st.write("Repeating stopped.")

# Call the repeat_text function if the repeat flag is set
if st.session_state.repeat:
    repeat_text()
