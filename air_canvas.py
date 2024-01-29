# Computer Vision Project | Air Canvas | Project with code and best for resume | Python OpenCV Project
# https://youtu.be/eHgvMAwfODw?si=bPUW9INCQsJAn799

# Import Libraries
import numpy as np
import cv2
from collections import deque

# Make function for trackbar 
def set_values(x):
   print("")

# Create trackbars for marker color adjustments
cv2.named_window("Color detectors")
cv2.create_trackbar("Upper Hue", "Color detectors", 153, 180,set_values)
cv2.create_trackbar("Upper Saturation", "Color detectors", 255, 255,set_values)
cv2.create_trackbar("Upper Value", "Color detectors", 255, 255,set_values)
cv2.create_trackbar("Lower Hue", "Color detectors", 64, 180,set_values)
cv2.create_trackbar("Lower Saturation", "Color detectors", 72, 255,set_values)
cv2.create_trackbar("Lower Value", "Color detectors", 49, 255,set_values)

# Create arrays to handle color points of different colors
blue_points = [deque(maximum_length=1024)]
green_points = [deque(maximum_length=1024)]
red_points = [deque(maximum_length=1024)]
yellow_points = [deque(maximum_length=1024)]

# Indexes to mark the points in particular arrays of specific colour
# Kernel to be used for dilation purpose 
# Create the Canvas setup
# Load the default webcam of the laptop/PC
# Add the color buttons to the live frame for color access
# Identify the pointer by making its mask
# Find contours for the pointer 
# Draw lines of all the colors on the canvas and frame 
# Display the windows
# Display the camera and all resources