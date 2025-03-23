# Jump Height Estimation Using MediaPipe
Real-time jump height estimation using MediaPipe and OpenCV. Tracks vertical hip displacement to count jumps and measure height in centimeters.

## Proposed Method
The system uses MediaPipe Pose to detect body landmarks and track the vertical movement of the hips during jumps. Key steps in the process include:
- Extracting hip landmarks to determine the mid-hip position.
- Measuring vertical displacement from a baseline hip position to detect jumps.
- Calculating jump height using pixel-to-centimeter conversion.
- Counting the number of jumps and displaying the latest jump height in real time.

## Possible Changes in Future
- Implementing flight time calculation for height estimation.
- Improving calibration for more accurate pixel-to-centimeter conversion.
- Adding visual feedback, such as overlays or graphs, to display jump metrics.
- Enhancing multi-person tracking to handle group exercises.

## Requirements
- python==3.10.10
- mediapipe==0.10.21
- opencv-python

## Installation
1. Clone the repository:
```bash
git clone https://github.com/NihalThomas/jump-height-estimation-using-MediaPipe.git
cd jump-height-estimation-using-MediaPipe
```
2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

## Usage
Run the script to start real-time jump detection:
```bash
python jump_height_estimation.py
```
Press **'q'** to quit the video feed.

## Key Citations
- [Pose landmark detection guide - Google AI](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker)  
- [Human Pose Estimation Using MediaPipe Pose and Optimization Method Based on a Humanoid Model](https://www.mdpi.com/2076-3417/13/4/2700)  
