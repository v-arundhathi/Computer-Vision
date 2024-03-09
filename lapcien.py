import cv2
import numpy as np

# Load the image
image=cv2.imread('/Users/arundhathi/Desktop/CV/CVLAB/HOME.jpg',0)

# Create the Laplacian kernel
kernel = np.array([[0, 1, 0],
                   [1, -8, 1],
                   [0, 1, 0]])

# Sharpen the image
sharpened_image = cv2.filter2D(image, cv2.CV_64F, kernel)

# Normalize the pixel values to [0, 255] range
sharpened_image = np.uint8(sharpened_image)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
