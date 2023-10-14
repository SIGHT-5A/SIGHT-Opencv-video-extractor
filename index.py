import cv2
import time
import os
import uuid

# Create the "uploads" folder if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Initialize the camera capture
camera = cv2.VideoCapture(0)

# Get the frame size of camera
frame_size = None
while True:
    ret, frame = camera.read()
    frame_size = list(frame.shape)  
    #The frame shape will be in form (breadth, length, no. of channels)
    break;

# We want frame size as length * breadth
del frame_size[2]
frame_size.reverse()

# Set video codec and create VideoWriter
video_id = uuid.uuid4()
cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('uploads/video_{}.mp4'.format(video_id), cv2_fourcc, 24, tuple(frame_size))
print(video_id)

# For demo we will record videos in 10 sec frame
start_time = time.time()
while True:
    print(time.time() - start_time)
    ret, frame = camera.read()
    video.write(frame)
    
     # Check if 30 seconds have passed
    if time.time() - start_time >= 10:
        # Sve the video writer
        video.release()
        break

# Release the webcam and VideoWriter
camera.release()
# Close all OpenCV windows
cv2.destroyAllWindows()