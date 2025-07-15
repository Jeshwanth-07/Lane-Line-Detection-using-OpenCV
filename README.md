
Lane Line Detection using OpenCV:
This project is a simple yet powerful implementation of a lane detection system built with Python and OpenCV. It processes a road video frame-by-frame, detects lane lines using image processing techniques, and overlays the results in real-time. This is a great starting point for those interested in autonomous driving, computer vision, or just learning how to manipulate video with OpenCV.

What It Does:
-->Converts each video frame to grayscale and applies Gaussian blur to reduce noise.
-->Uses Canny edge detection to highlight strong edges (potential lane lines).
-->Applies a region of interest (ROI) mask to focus only on the part of the frame where lanes usually appear.
-->Uses Hough Line Transform to detect straight lines that likely represent lane markers.
-->Overlays the detected lane lines back onto the original video frame for visualization.

Demo Use-Case:
You can use this with any front-facing road video recorded from a moving vehicle. It's a basic simulation of how real-world driver-assistance systems begin processing visual lane data.

Technologies Used:
-->Python 3.x
-->OpenCV
-->NumPy

Why This Project:
This project helped me understand how simple image processing techniques can be chained together to achieve useful real-world results. Lane detection is one of the foundational tasks in self-driving car systems, and this project offers insight into how such systems begin to interpret the road.

How to Run:
Install dependencies:
pip install opencv-python numpy

Clone the repository and run the Python script:
  python lane_detection.py
  
Make sure to replace 'test_video.mp4' in the script with the path to your own road video.

Possible Improvements:
This is a basic version and can be improved in many ways:
-->Smoothing/joining multiple line segments into a single lane line.
-->Detecting curved lanes using polynomial fitting.
-->Handling shadows, different lighting conditions, or lane colors.
-->Integrating with steering control logic (for simulation).
