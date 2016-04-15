import cv2

# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html

img = cv2.imread('H_line_1.png')

blur = cv2.GaussianBlur(img, (11,11), 2)

cv2.imwrite('gblur_opencv.png', blur)

