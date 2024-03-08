import cv2
image=cv2.imread('/Users/arundhathi/Downloads/HOME.jpg')
cv2.imshow('original',image)
cv2.waitKey(500)
grayimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayimage',grayimage)
cv2.waitKey(500)
cv2.destroyAllWindows()
