# Highway Vehicle Detection

This project demonstrates vehicle detection and tracking in a highway traffic video using Python and OpenCV. It processes each video frame, detects vehicles, and tracks their movement by drawing bounding boxes and assigning unique IDs.

## Features
- Vehicle detection from a highway video
- Vehicle tracking across consecutive frames
- Bounding box visualization
- Frame-by-frame video processing

## Technologies Used
- Python
- OpenCV
- NumPy

## Files
- `main.py` – Main script for vehicle detection
- `tracker.py` – Vehicle tracking logic
- `highway.mp4` – Input highway video

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

## Output
The program detects vehicles in the input video, tracks them across frames, and displays the processed video with bounding boxes and tracking IDs.
