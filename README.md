# 👁️ Eye-Controlled Mouse

## 🚀 Overview

Eye-Controlled Mouse is an innovative Python project that allows users to control their computer's mouse cursor using only their eye movements. By leveraging computer vision and machine learning techniques, this application provides a hands-free way to interact with your computer, enhancing accessibility and exploring new modes of human-computer interaction.

## ✨ Features

- 👀 Control mouse cursor with eye movements
- 😉 Click by winking or blinking
- 🖥️ Works across the entire screen
- 🎯 Smooth cursor movement with advanced filtering
- 🔧 Adjustable sensitivity and click settings

## 🛠️ Technologies Used

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed
- A webcam or external camera
- macOS, Windows, or Linux operating system

## 🔧 Installation

1. Clone the repository: 
git clone https://github.com/dsd7888/eye-controlled-mouse.git
2. Navigate to the project directory:
cd eye-controlled-mouse
3. Install the required packages:
pip install -r requirements.txt

## 🎮 Usage

1. Run the main script:
python main.py

2. Position yourself in front of the camera, ensuring your face is clearly visible.

3. Move your eyes to control the mouse cursor.

4. Wink or blink (depending on your settings) to perform a click action.

5. Press 'q' to quit the application.


- `SMOOTHING_FACTOR`: Adjust cursor movement smoothness
- `CLICK_THRESHOLD`: Change the sensitivity for click detection
- `CAMERA_INDEX`: Select a different camera if you have multiple


## 🙏 Acknowledgements

- [MediaPipe](https://github.com/google/mediapipe) for their amazing face mesh solution
- [PyAutoGUI](https://github.com/asweigart/pyautogui) for making mouse control easy
- All open-source contributors whose libraries made this project possible

---

If you found this project interesting, please consider giving it a ⭐️!
