# Webcam Video Capture with OpenCV

This Python script captures a 10-second video from your webcam using OpenCV and saves it as an MP4 file.

## Prerequisites

- Python
- OpenCV

## Usage

1. Ensure that you have the required libraries installed. You can install them using pip:

```bash
pip install opencv-python numpy
```

2. Clone or download this repository.

3. Run the script:

```bash
python index.py
```

The captured video will be saved in the "uploads" folder with a unique filename.


## Code Explanation
- The script initializes the webcam and gets the frame size.
- It uses a unique video ID to create a VideoWriter for saving the video.
- The code records video for 10 seconds.
- The video is saved in the "uploads" folder.
