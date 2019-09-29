import cv2

filename = r'C:\Users\eecon\Desktop\test_03.jpg'
img = cv2.imread(filename, 0) # 画像の読み込み

threshold = 100 # 閾値の設定

ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_OTSU) # 二値化(閾値100を超えた画素を255にする。)

# 二値化画像の表示
#cv2.imwrite(r'C:\Users\eecon\Desktop\img_binary', img_thresh)
cv2.imshow("img_th", img_thresh)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite(r'C:\Users\eecon\Desktop\img_binary.jpg', img_thresh)

