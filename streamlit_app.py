import streamlit as st

# Streamlit UI
st.title("Air D Pollution")
st.write("Monitoring air quality and mask usage in real-time.")

# Initialize session state for video streaming
if 'video_streaming' not in st.session_state:
    st.session_state.video_streaming = False
    st.session_state.stop_event = None

# Create placeholders for buttons
start_button = st.empty()
stop_button = st.empty()

# Manage button actions
if not st.session_state.video_streaming:
    if start_button.button("Start Video Stream"):
        st.session_state.video_streaming = True
        st.session_state.stop_event = Event()

if st.session_state.video_streaming:
    if stop_button.button("Stop Video Stream"):
        st.session_state.video_streaming = False
        if st.session_state.stop_event:
            st.session_state.stop_event.set()
        st.write("Video stream stopped.")

# Display video stream
if st.session_state.video_streaming:
    display_video_stream(st.session_state.stop_event)
