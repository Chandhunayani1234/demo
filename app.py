import streamlit as st
import time

# Title of the app
st.title('Streamlit Notepad with Repeat Feature')

# Text input from the user
user_input = st.text_area("Enter text here:", key="notepad")

# Start and stop buttons
start_button = st.button('Start Repeating')
stop_button = st.button('Stop Repeating')

# Initialize session state
if 'repeat' not in st.session_state:
    st.session_state.repeat = False
    st.session_state.last_repeat_time = 0
    st.session_state.repeated_text = ""

# Function to repeat text
def repeat_text():
    current_time = time.time()
    if current_time - st.session_state.last_repeat_time > 2:  # 2 seconds interval
        st.session_state.last_repeat_time = current_time
        st.session_state.repeated_text = user_input

# Start repeating text
if start_button:
    st.session_state.repeat = True
    st.write("Repeating started...")

# Stop repeating text
if stop_button:
    st.session_state.repeat = False
    st.write("Repeating stopped.")

# Call the repeat_text function if the repeat flag is set
if st.session_state.repeat:
    repeat_text()

# Display the repeated text
if st.session_state.repeated_text:
    st.write("Repeated Text:")
    st.write(st.session_state.repeated_text)

# Use st.experimental_rerun to rerun the script every second if repeating
if st.session_state.repeat:
    time.sleep(1)
    st.experimental_rerun()
