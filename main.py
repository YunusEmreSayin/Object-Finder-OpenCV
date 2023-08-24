import cv2
import numpy as np

image = cv2.imread(r"data\cars.jpg")
# The image to scan our template

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Converting the full image to gray for matchTemplate Proccess

template = cv2.imread(r"data\cars-template.jpg", 0)
# The image we will try to find in full image

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
# Getting the result with matchTemplate Process

_, _, _, max_loc = cv2.minMaxLoc(result)
# Getting location of most successful result from process

top_left = max_loc
# Defining the starting point of rectangle

print(max_loc)

width, height = template.shape[::-1]
# Getting width and height values of result

bottom_right = (top_left[0] + width, top_left[1] + height)
# Defining the end point of rectangle

cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
# drawing rectangle

cv2.imshow('object found', image)
cv2.waitKey(0)
# Show image method and waiting for a key pressed

cv2.destroyAllWindows()
# After key pressed all windows will be destroyed
