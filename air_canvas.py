# Air Canvas using OpenCV | Python | Air Painting | Draw in Air | With Code
# https://youtu.be/Tjb7da9FSB4?si=gpPzgVFVokV3xrvL

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
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

# Kernel to be used for dilation purpose 
kernel = np.ones((5,5),np.uint8)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color_index = 0

# Create the Canvas setup
paint_window = np.zeros((471,636,3)) + 255
paint_window = cv2.rectangle(paint_window, (40,1), (140,65), (0,0,0), 2)
paint_window = cv2.rectangle(paint_window, (160,1), (255,65), colors[0], -1)
paint_window = cv2.rectangle(paint_window, (275,1), (370,65), colors[1], -1)
paint_window = cv2.rectangle(paint_window, (390,1), (485,65), colors[2], -1)
paint_window = cv2.rectangle(paint_window, (505,1), (600,65), colors[3], -1)

# Load the default webcam of the laptop/PC
# Add the color buttons to the live frame for color access
# Identify the pointer by making its mask
# Find contours for the pointer 
# Draw lines of all the colors on the canvas and frame 
# Display the windows
# Display the camera and all resources