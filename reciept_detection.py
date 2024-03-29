import cv2
import numpy as np

image = r'C:\Users\eecon\Desktop\degree.jpg'

input_original_data = image # 画像読み取り
img = cv2.imread(input_original_data)
h, s, gray = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))

size = (3, 3)
blur = cv2.GaussianBlur(gray, size, 0) # 平滑化

lap = cv2.Laplacian(blur, cv2.CV_8UC1) # 勾配検出

ret2, th2 = cv2.threshold(lap, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 二値化

kernel = np.ones((3, 20), np.uint8)
closing = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel) # モルフォロジー変換

kernel = np.ones((3, 3), np.uint8)
dilation = cv2.dilate(closing, kernel, iterations = 1) # クロージング
erosion = cv2.erode(dilation, kernel, iterations = 1)

lap2 = cv2.Laplacian(erosion, cv2.CV_8UC1) # 勾配検出

contours, hierarchy = cv2.findContours(lap2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 矩形
min_area = img.shape[0] * img.shape[1] * 1e-4
tmp = img.copy()
if len(contours) > 0:
    for i, contour in enumerate(contours):
        rect = cv2.boundingRect(contour)
        if rect[2] < 10 or rect[3] < 10:
            continue
        area = cv2.contourArea(contour)
        if area < min_area:
            continue
        cv2.rectangle(tmp, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), (0, 255, 0), 2)

cv2.imwrite(r'C:\Users\eecon\Desktop\capture_0.jpg', tmp)