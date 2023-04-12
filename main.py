import cv2
print("cv2 Imported!")

# img =  cv2.imread(r"C:\Users\Ayush Pujari\Desktop\images.jpg")
# cv2.imshow("Output", img)
# cv2.IMREAD_GRAYSCALE("gray output", img)
# cv2.waitKey(0)

video = cv2.VideoCapture(1)
video.set(3,640)
video.set(4,480)
video.set(10,100)

while True:
    success, img = video.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

