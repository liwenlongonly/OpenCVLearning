import cv2


def test():
    _show_img()


def _show_img():
    # 读一个图片并进行显示(图片路径需自己指定)
    lena = cv2.imread("1.jpg")
    cv2.imshow("image", lena)
    cv2.waitKey(0)
