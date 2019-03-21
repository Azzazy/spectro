import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

max_rgb = [[], [], []]
for i in range(9):
    img = cv2.imread('pics2/sample 2 flash/pic' + str(i) + '.jpg')

    img = img[400:1100, 1200:1900]

    cv2.imshow("cropped", img)
    cv2.waitKey(0)

    # plt.title('known' + str(i))
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        max_rgb[i].append(np.argmax(hist))
    #     plt.plot(hist, color=col)
    #
    # plt.show()

x = [5000, 2000, 1000, 500, 100, 50, 10, 5, 0][::-1]
r = [i for i in max_rgb[0]]
g = [i for i in max_rgb[1]]
b = [i for i in max_rgb[2]]
# plt.scatter(x, r)
# plt.show()
# plt.scatter(x, g)
# plt.show()
# plt.scatter(x, b)
# plt.show()


# x = [0, 100, 500, 1000, 2000, 5000]
y = b
# inter = interp1d(x, y, kind='cubic')
inter = interp1d(x, y)
xnew = np.arange(0, 5000, 50)
ynew = inter(xnew)
plt.figure()

for i in range(9):
    print y[i], x[i]
plt.plot(x, y, 'x', xnew, ynew)
plt.legend(['Samples', 'Interpolation'], loc='best')
plt.title('Concentration VS Intensity')
plt.xlabel('Concentration (ppm)')
plt.ylabel('Intensity')

# img = cv2.imread('pics/sample4/pic0.jpg')
# img = img[230:850, 130:400]
# pic = [img[550:650, 0:100], img[340:440, 0:100], img[160:260, 0:100], img[0:100, 0:100], img[550:650, 200:300]]
#
# max_rgb_new = [[], [], []]
# for img in pic:
#     color = ('b', 'g', 'r')
#     for i, col in enumerate(color):
#         hist = cv2.calcHist([img], [i], None, [256], [0, 256])
#         max_rgb_new[i].append(np.argmax(hist))
#         plt.plot(hist,color=col)
#
#     plt.title('unknown' + str(i))
#
#     plt.show()


# max_rgb_new = [[], [], []]
# for i in range(2):
#     img = cv2.imread('pics2/sample 5 unknown/pic' + str(i) + '.jpg')
#
#     img = img[350:1050, 1200:2000]
#
#     # cv2.imshow("cropped", img)
#     # cv2.waitKey(0)
#     color = ('b', 'g', 'r')
#     for i, col in enumerate(color):
#         hist = cv2.calcHist([img], [i], None, [256], [0, 256])
#         max_rgb_new[i].append(np.argmax(hist))
#     #     plt.plot(hist, color=col)
#     #
#     # plt.title('unknown' + str(i))
#     #
#     # plt.show()
# # x = inter(max_rgb_new[1])
# x = np.interp(max_rgb_new[1], x, y)
# y = max_rgb_new[1]
# for i in range(2):
#     print y[i], x[i]
# #
# for i in range(2):
#     plt.plot(x, y, 's')
#
plt.show()
