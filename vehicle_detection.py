import cv2

# Load the Haar Cascade classifier
vehicle_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

# Capture video from file
cap = cv2.VideoCapture('your_video_file.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 1)

        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        out.write(frame)

        cv2.imshow('Vehicle Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
