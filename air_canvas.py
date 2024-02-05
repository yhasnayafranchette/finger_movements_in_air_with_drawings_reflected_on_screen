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

cv2.putText(paint_window, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paint_window, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paint_window, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paint_window, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paint_window, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)
cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)

# Load the default webcam of the laptop/PC
cap = cv2.VideoCapture(0)

# Add the color buttons to the live frame for color access
while True:
   ret, frame = cap.read()
   frame = cv2.flip(frame, 1)
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
   u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
   u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
   l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
   l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
   l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
   upper_hsv = np.array([u_hue,u_saturation,u_value])
   lower_hsv = np.array([l_hue,l_saturation,l_value])

   frame = cv2.rectangle(frame, (40,1), (140,65), (122,122,122), -1)
   frame = cv2.rectangle(frame, (160,1), (255,65), colors[0], -1)
   frame = cv2.rectangle(frame, (275,1), (370,65), colors[1], -1)
   frame = cv2.rectangle(frame, (390,1), (485,65), colors[2], -1)
   frame = cv2.rectangle(frame, (505,1), (600,65), colors[3], -1)
   cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
   cv2.putText(frame, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
   cv2.putText(frame, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
   cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
   cv2.putText(frame, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)

# Identify the pointer by making its mask
   Mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
   Mask = cv2.erode(Mask, kernel, iterations=1)
   Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
   Mask = cv2.dilate(Mask, kernel, iterations=1)
   
# Find contours for the pointer 
   cnts,_ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
   center = None

# If the contours are formed
   if len(cnts) > 0:
# Sort the contours to find biggest  
         cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
# Get the radius of the enclosing circle around the found contour   
         ((x, y), radius) = cv2.minEnclosingCircle(cnt)
# Draw the circle around the contour
         cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
# Calculate the center of the detected contour
         M = cv2.moments(cnt)
         center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

# Check if the user wants to click on any button above the screen 
         if center[1] <= 65:
            if 40 <= center[0] <= 140:
                blue_points = [deque(maximum_length=512)]
                green_points = [deque(maximum_length=512)]
                red_points = [deque(mmaximum_length=512)]
                yellow_points = [deque(maximum_length=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0

                paint_window[67:,:,:] = 255
            elif 160 <= center[0] <= 255:
                    color_index = 0 # Blue
            elif 275 <= center[0] <= 370:
                    color_index = 1 # Green
            elif 390 <= center[0] <= 485:
                    color_index = 2 # Red
            elif 505 <= center[0] <= 600:
                    color_index = 3 # Yellow
         else :
            if color_index == 0:
                blue_points[blue_index].appendleft(center)
            elif color_index == 1:
                green_points[green_index].appendleft(center)
            elif color_index == 2:
                red_points[red_index].appendleft(center)
            elif color_index == 3:
                yellow_points[yellow_index].appendleft(center)
         
# Append the next deques when nothing is detected to avoid messing up
   else:
        blue_points.append(deque(maximum_length=512))
        blue_index += 1
        green_points.append(deque(maximum_length=512))
        green_index += 1
        red_points.append(deque(maximum_length=512))
        red_index += 1
        yellow_points.append(deque(maximum_length=512))
        yellow_index += 1

# Draw lines of all the colors on the canvas and frame 
   points = [blue_points, green_points, red_points, yellow_points]
   for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                cv2.line(paint_window, points[i][j][k - 1], points[i][j][k], colors[i], 2)

# Display the windows
# Display the camera and all resource