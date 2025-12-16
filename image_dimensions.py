import cv2 as cv
import numpy as np
path=r'D:\jio\exp\min oil 60\phi=0.5\17.14 34.3_C001H001S0001\processing\17.14 34.3_C001H001S0001000140.jpg'
image = cv.imread(path, cv.IMREAD_GRAYSCALE)

image.shape

img=cv.imread(path)

def find_coord(event,x,y,flag,params):
    if event==cv.EVENT_FLAG_LBUTTON:
        print(x,',',y)
        font=cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x) +','+ str(y), (x,y), font, 1,(255,0,0))
        cv.imshow("image",img)

if __name__=="__main__":

    img=cv.imread(path)
    cv.imshow("image",img)
    cv.setMouseCallback("image",find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()
