import cv2
import glob

x = 770
y2 = 360
y1 = 464

neck_width = []
time = []

folPath = r'D:\jio\exp\min oil 60\phi=0.5\17.14 34.3_C001H001S0001\processing'

# pattern=r'C:\Users\user\Desktop\New folder (2)\phi=0.1\8\*.jpg'
filePaths = list(glob.glob(folPath + r"\*"))
# filePaths=glob.glob(pattern)

for filePath in filePaths:

    image = cv2.imread(filePath)

    if image is None:
        print(f"Error: Unable to load image at {filePath}")
    else:

        blur = cv2.GaussianBlur(image, (5, 5), 2)

        blur2 = cv2.GaussianBlur(blur, (5, 5), 2)

        blur3 = cv2.GaussianBlur(blur2, (5, 5), 2)

        kernelSize = 5

        medianBlur = cv2.medianBlur(blur3, kernelSize)
        # low_threshold=50
        # high_threshold=150

        low_threshold = 10
        high_threshold = 20

        edges = cv2.Canny(medianBlur, low_threshold, high_threshold)
        blurred_image = cv2.GaussianBlur(edges, (5, 5), 0)

        _, otsu_thresholded_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # cv2.imshow("Otsu Thresholded Image", otsu_thresholded_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # otsu_thresholded_image[134,1100] = 0
        max_pixel = -1

        for i in range(y1 - y2 + 1):
            pixel = otsu_thresholded_image[y2 + i, x]

            if pixel > max_pixel:
                max_pixel = pixel
                k = y2 + i

    # print('pixel_value= ',k)
    z = 250 / (y1 - y2)

    distance = (y1 - k) * z
    # if distance!=195:
    # neck_width.append(distance)
    # else :
    # neck_width.append(None)
    neck_width.append(distance)

q = 0
for i in neck_width:
    q += 1

q