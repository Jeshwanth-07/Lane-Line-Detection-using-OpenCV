# To exit press q on keyboard
import cv2
import numpy as np

# Function to apply Canny edge detection
def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny_image = cv2.Canny(blurred, 50, 150)
    return canny_image

# Function to apply region of interest mask
def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(200, height), (1100, height), (550, 250)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

# Function to display lines on the original image
def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
    return line_image

# Load the video file (replace 'your_video_path.mp4' with your video file)
cap = cv2.VideoCapture('test_video.mp4')

while cap.isOpened():
    # Read the next frame from the video
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply Canny edge detection
    canny_image = canny(frame)
    
    # Apply region of interest mask
    cropped_image = region_of_interest(canny_image)
    
    # Detect lines using Hough Transform
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    
    # Display detected lines on the original frame
    line_image = display_lines(frame, lines)
    
    # Combine the line image with the original frame
    result_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    
    # Display the result
    cv2.imshow('Lane Detection', result_image)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
