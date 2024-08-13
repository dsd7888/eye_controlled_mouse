import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Disable PyAutoGUI's failsafe to include edges
pyautogui.FAILSAFE = False
cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize Google's MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Get screen size
screen_w, screen_h = pyautogui.size()

# Check if camera opened successfully
if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

# For smoothing
smoothing = 7
prev_coords = []

# For click cooldown
last_click_time = 0
click_cooldown = 1.0  # seconds

def smooth_coords(x, y):
    prev_coords.append((x, y))
    if len(prev_coords) > smoothing:
        prev_coords.pop(0)
    return np.mean(prev_coords, axis=0)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Flip the frame horizontally for a later selfie-view display else it will be inverted
    frame = cv2.flip(frame, 1)
    
    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the image and find facial landmarks
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Eye movement for cursor
            for id, lm in enumerate(face_landmarks.landmark[474:478]):#right eye landmark
                x, y = int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = np.interp(x, (0, frame.shape[1]), (0, screen_w))
                    screen_y = np.interp(y, (0, frame.shape[0]), (0, screen_h))
                    
                    smooth_x, smooth_y = smooth_coords(screen_x, screen_y)
                    pyautogui.moveTo(smooth_x, smooth_y)

            # Blink detection for clicking (left eye landmark)
            left_eye = [face_landmarks.landmark[145], face_landmarks.landmark[159]]
            if (left_eye[0].y - left_eye[1].y) < 0.004:
                current_time = time.time()
                if current_time - last_click_time > click_cooldown:
                    pyautogui.click()
                    last_click_time = current_time

            # Draw circles for left eye landmarks
            for lm in left_eye:
                x, y = int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])
                cv2.circle(frame, (x, y), 3, (0, 255, 255))

    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
