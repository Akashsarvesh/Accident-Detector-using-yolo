# Accident Detection Using YOLO

This project implements an accident detection system using YOLO (You Only Look Once) for object detection and an automated alert system using Twilio. The application is built using Streamlit for easy deployment and interaction.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The aim of this project is to detect accidents in video footage using YOLOv8 for object detection and to send automated alerts using Twilio when an accident is detected. The project is divided into two main modules:

1. **Terrain Safety Detection Module**: Upload a video and run YOLOv8 object detection to identify potential accidents.
2. **Automated Alert System for the Detected Incident**: Send alert messages for detected incidents using Twilio.

## Features

- **Object Detection**: Utilizes YOLOv8 for detecting objects in video footage.
- **Automated Alerts**: Sends SMS alerts using Twilio when an accident is detected.
- **User-Friendly Interface**: Built with Streamlit for easy interaction and deployment.
- **Video Playback**: Displays uploaded videos and detected incidents within the app.

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- OpenCV
- Twilio
- YOLOv8 model file (`accident.pt`)

### Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/your-username/accident-detection-using-yolo.git
    cd accident-detection-using-yolo
    ```

2. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Twilio Credentials**

    Create a `.env` file in the root directory and add your Twilio credentials:

    ```sh
    TWILIO_ACCOUNT_SID=your_account_sid
    TWILIO_AUTH_TOKEN=your_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_phone_number
    RECIPIENT_PHONE_NUMBER=recipient_phone_number
    ```

4. **Download YOLOv8 Model**

    Ensure the YOLOv8 model file (`accident.pt`) is placed in an accessible directory and update the `model_path` variable in the code accordingly.

## Usage

1. **Run the Application**

    ```sh
    streamlit run app.py
    ```

2. **Navigate the Interface**

    - Use the sidebar to navigate between the "Terrain Safety Detection Module" and the "Automated Alert System for the Detected Incident".
    - Upload videos and initiate object detection.
    - View detected incidents and receive alerts.

## File Structure

```sh
accident-detection-using-yolo/
│
├── uploads/                   # Directory for uploaded videos
├── app.py                     # Main application file
├── requirements.txt           # Python dependencies
├── .env                       # Environment file for Twilio credentials
└── README.md                  # Project README file
```

## Future Improvements

- Improve detection accuracy by fine-tuning the YOLO model.
- Add support for real-time video streaming and detection.
- Enhance alert system to include more detailed notifications and multiple communication channels.
- Implement a database to store detected incidents and alert history.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



