# repair damaged images
import cv2
import matplotlib.pyplot as plt
import numpy as np
damaged_image_path = "D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Capstone Project\Input\dmg_img.png"
damaged_image = cv2.imread(damaged_image_path)
mask_path = "D:\Workspace (VS Code)\College\Slot-B-Computer Vision\Capstone Project\Input\mask.png"
mask = cv2.imread(mask_path, 0)
ret,thresh1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

kernel = np.ones((7,7), np.uint8)
mask1 = cv2.dilate(thresh1, kernel, iterations = 1)
damaged_image = cv2.cvtColor(damaged_image, cv2.COLOR_BGR2RGB)

# use a smaller inpainting radius
output1 = cv2.inpaint(damaged_image, mask1, 3, cv2.INPAINT_TELEA)
output2 = cv2.inpaint(damaged_image, mask1, 3, cv2.INPAINT_NS)

img = [damaged_image,mask,output1, output2]
titles = ['damaged image','Mask', 'TELEA', 'NS']

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.title(titles[i])
    plt.imshow(img[i])
plt.show()