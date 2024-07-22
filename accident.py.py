import streamlit as st
import cv2
import tempfile
import os
from twilio.rest import Client
import subprocess

# Function to perform YOLO v8 object detection
def run_yolo(input_video_path, model_path, output_video_path):
    try:
        # Run YOLO command
        yolo_command = f"yolo task=detect mode=predict model={model_path} conf=0.25 source={input_video_path} save=True save_txt=True"
        subprocess.run(yolo_command, shell=True)
    except Exception as e:
        st.error(f"Error during object detection: {e}")

# Function to send alert message
def send_alert(message):
    # Twilio credentials
    TWILIO_ACCOUNT_SID = ""
    TWILIO_AUTH_TOKEN = ""
    TWILIO_PHONE_NUMBER = ""
    RECIPIENT_PHONE_NUMBER = ""

    # Initialize Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )
        st.success(f"Alert message sent: {message.sid}")
    except Exception as e:
        st.error(f"Error sending alert message: {e}")

# Page 1: Terrain Safety Detection Module
def page_terrain_safety_detection():
    st.title("Terrain Safety Detection Module")

    # Create 'uploads' directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    # Upload video file
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4"])
    if uploaded_file is not None:
        # Save uploaded video
        input_video_path = os.path.join('uploads', uploaded_file.name)
        try:
            with open(input_video_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("Video uploaded successfully.")

            # Display uploaded video
            st.video(uploaded_file)
        except Exception as e:
            st.error(f"Error saving uploaded file: {e}")
            return

        # Perform object detection
        if st.button("Run Object Detection"):
            model_path = "D:\\downloadsssss\\accident.pt"

            # Set up progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()

            # Update status message
            status_text.text("Running object detection...")

            # Perform object detection
            run_yolo(input_video_path, model_path, output_video_path=None)  # Pass None for output_video_path

            # Update progress bar and status message on completion
            progress_bar.progress(100)
            status_text.text("Object detection completed successfully.")

# Page 2: Automated Alert System for the Detected Incident
def page_alert_system():
    st.title("Automated Alert System for the Detected Incident")

    # Upload MP4 video file
    uploaded_file = st.file_uploader("Upload the final object detection video", type=["mp4"])

    if uploaded_file is not None:
        # Save the uploaded video to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(uploaded_file.read())
        temp_file.close()

        # Read the video file using OpenCV
        cap = cv2.VideoCapture(temp_file.name)

        # Check if the video file is readable
        if not cap.isOpened():
            st.error("Error: Unable to read the video file.")
            return

        st.success("Video uploaded successfully.")
        
        # Play the video
        st.video(uploaded_file)

        # Initialize variables for frame display
        class_detected = None
        class_count = 0
        frame_count = 0
        alert_frames = []

        # Display frames with continuous detection
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Increment frame count
            frame_count += 1

            # Check for detected class
            # For demonstration, assume the class is detected based on some condition
            # You need to replace this with your actual detection logic
            if frame_count % 5 == 0:  # Simulate detection every 5 frames
                class_detected = "severe" if frame_count % 50 == 0 else "moderate"  # Alternate between severe and moderate
                class_count += 1
            else:
                class_detected = None

            # If the class is detected continuously for 30 frames, break the loop
            if class_count >= 50:
                if len(alert_frames) < 3:  # Capture the last 3 frames where the alert is sent
                    alert_frames.append(frame.copy())

            # Send alert message every 3 frames
            if class_detected is not None and frame_count % 3 == 0:
                message = f"Continuous {class_detected} detected for 3 frames."
                send_alert(message)

        # Release the video capture object
        cap.release()

        # Display the three consecutive final frames where alerts are sent
        st.subheader("Consecutive Final Frames with Alerts")
        for alert_frame in alert_frames:
            st.image(alert_frame, channels="BGR", caption=f"Frame {frame_count-2}")

# Streamlit app
def main():
    pages = {
        "Terrain Safety Detection Module": page_terrain_safety_detection,
        "Automated Alert System for the Detected Incident": page_alert_system
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
