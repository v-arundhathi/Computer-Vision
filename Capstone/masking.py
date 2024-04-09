# create a mask for the damaged image
import cv2
import numpy as np

damaged_image_path = "D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Capstone Project\Input\test2.jpg"
damaged_image = cv2.imread(damaged_image_path)

# create a grayscale mask with the black line highlighted as white
gray_mask = cv2.cvtColor(damaged_image, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray_mask, 0, 255, cv2.THRESH_BINARY_INV)

cv2.imwrite("mask4.png", mask)
# display the mask
# cv2.imshow("mask", mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# save the mask image to a file