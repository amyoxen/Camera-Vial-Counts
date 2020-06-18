import cv2 
import numpy as np 
  
# Read image. 
img1 = cv2.imread('te.jpg', cv2.IMREAD_COLOR)
img = img1.copy()
  
# Convert to grayscale. 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Blur using 3 * 3 kernel. 
gray_blurred = cv2.blur(gray, (12, 12)) 
cv2.imwrite("result_gray.png", gray_blurred)  
# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 1, 60, param1 = 60, 
               param2 = 30, minRadius = 30, maxRadius = 70) 

count = 0
# Draw circles that are detected. 
if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        # Draw the circumference of the circle. 
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
  
        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 

        count += 1
        
        img = cv2.putText(img, str(count),(a, b+2), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),2)

cv2.imwrite("result.png", img)
print("Number of vials is " + str(detected_circles.shape[1]))
