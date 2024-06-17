import numpy as np
import pyautogui
import cv2
import time

# Define the screen resolution and frame rate
screen_width, screen_height = pyautogui.size()
frame_rate = 20.0  # Frames per second

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("screen_recording.avi", fourcc, frame_rate, (screen_width, screen_height))

# Start time
start_time = time.time()

try:
    print("Press Ctrl+C to stop recording...")
    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a NumPy array
        frame = np.array(screenshot)

        # Convert the frame from RGB to BGR (OpenCV format)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        output.write(frame)

        # Delay to match the frame rate
        time.sleep(1 / frame_rate)
except KeyboardInterrupt:
    print("Recording stopped.")
finally:
    # Release the video writer object
    output.release()
    print("Video saved as 'screen_recording.avi'.")


