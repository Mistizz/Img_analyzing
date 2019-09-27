import cv2

video_capture = cv2.VideoCapture(1)

while True:
    ret, frame = video_capture.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # キーボード「Q」で終了
        break

video_capture.release()
cv2.destroyAllWindows()