import cv2
import numpy as np
img = cv2.imread("E:\\a4.jpg")

#cv2.imshow("a4",img)
#cv2.waitKey()


#print(np.dot(img[..., :3], [1,1, 1]))

#b = img[..., :3]
#print(img[..., :3])
#print(1)

NMS = np.zeros([6, 6])
W2, H2 = NMS.shape
NMS[0, :] = NMS[W2 - 1, :] = NMS[:, 0] = NMS[:, H2 - 1] = 1

print(1)
