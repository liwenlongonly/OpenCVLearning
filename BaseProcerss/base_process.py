import cv2
import matplotlib.pyplot as plt
import numpy as np


def test():
    _show_img()


def _show_img():
    # 读一个图片并进行显示(图片路径需自己指定)
    lena = cv2.imread("1.jpg")
    cv2.imshow("image", lena)
    cv2.waitKey(0)


def calculate_gray_histogram():
    # 读图
    img = cv2.imread(r'./20201121160553632.png')
    pts = np.array([[20, 10], [10, 27], [20, 44], [40, 44], [50, 27], [40, 10]], np.int32)
    cv2.polylines(img, [pts], True, (0, 0, 255), 1)
    cv2.fillPoly(img, [pts], (255, 255, 255))
    rect = cv2.minAreaRect(pts)  # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
    points = cv2.boxPoints(rect)  # 得到最小外接矩形的四个点坐标
    points = np.int0(points)  # 坐标值取整
    img = cv2.drawContours(img, [points], 0, (0, 0, 255), 2)


    # 选择ROI(感兴趣的区域)
    roi = cv2.selectROI(windowName="original", img=img, showCrosshair=True, fromCenter=False)
    x, y, w, h = roi
    print(roi)

    # 显示ROI并保存图片
    if roi != (0, 0, 0, 0):
        crop = img[y:y + h, x:x + w]

    # 转换成灰度图
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    hist = cv2.calcHist([dst], [0], None, [2], [0, 256])
    print(hist)
    print(hist[0][0] / (hist[0][0] + hist[1][0]))

    cv2.imshow('crop', dst)
    cv2.imwrite('./dogs_and_cats_crop.jpg', dst)
    print('Saved!')

    # 退出
    cv2.waitKey(0)
    cv2.destroyAllWindows()