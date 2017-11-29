import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50, 100], [80, 100], 'c', linewidth=5)
# plt.show()
#
# cv2.imwrite('watchgray.png', img)
# Video capturing
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     out.write(frame)
#     cv2.imshow('frame', frame)
#     cv2.imshow('gray', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindows()
#


# Writing on image

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)
cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)
cv2.circle(img, (100, 63), 55, (0, 255, 255), -1)

pts = np.array([[10, 5], [20, 50], [50, 70], [30, 40]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV stuff', (0, 130), font, 1, (200, 255, 255), 5, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
