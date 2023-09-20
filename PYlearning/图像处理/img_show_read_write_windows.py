import cv2
img = cv2.imread('1.jpg',1)
cv2.imwrite('2.jpg',img)
cv2.namedWindow('meilv',cv2.WINDOW_NORMAL)
cv2.imshow('meilv',img)
cv2.waitKey(0)
cv2.destroyWindow('meilv')

