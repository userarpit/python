import cv2

img = cv2.imread("butterfly.png", 1)
print(img.shape)
print(img[0][0][0])
for _ in range(10):
    img[0, _, :] = 0

print(img)
resize_img = cv2.resize(img, (int(img.shape[1] * 3), int(img.shape[0] * 3)))
cv2.imshow("Butter fly", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
