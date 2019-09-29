import cv2
import numpy as np
import math
import sys
from scipy import ndimage

def get_degree(img): # Issue：入力画像のサイズに合わせた閾値になるように、閾値調整
    l_img = img.copy()
    gray_image = cv2.cvtColor(l_img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image,50,150,apertureSize=3)
    #print(edges)
    minLineLength = 100 # 値以上の長さを持つ線の候補が見つかったら、それを線として検出
    maxLineGap = 3 # 点と点の間の間隔が数より小さければ、同一の線とみなす  こっちの閾値の方が影響大
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    #print(lines)
    

    sum_arg = 0
    count = 0
    for line in lines:
        for x1,y1,x2,y2 in line:
            arg = math.degrees(math.atan2((y2-y1), (x2-x1)))
            HORIZONTAL = 0
            DIFF = 20
            #arg != 0を条件に追加し、傾きの平均を0に寄りにくくした。
            if arg != 0 and arg > HORIZONTAL - DIFF and arg < HORIZONTAL + DIFF : 
                sum_arg += arg
                count += 1
    if count == 0:
        return HORIZONTAL
    else:
        return (sum_arg / count) - HORIZONTAL


if __name__ == "__main__":
    read_file = r'C:\Users\eecon\Desktop\test_04.jpg'

    img = cv2.imread(read_file)
    arg = get_degree(img)
    print(arg)
    rotate_img = ndimage.rotate(img, arg)
    cv2.imwrite(r'C:\Users\eecon\Desktop\degree_{}.jpg'.format(arg), rotate_img)