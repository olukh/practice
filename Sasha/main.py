from PIL import Image
import numpy as np
import cv2 as cv

def cropping(img):
    img=np.array(img)
    crop_img=img[0:1023,0:img.shape[1]]
    return crop_img

img =cv.imread('1.jpg')

imgray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgray=cropping(imgray)
#ret1, tresh1=cv.threshold(imgray, 200,255,0)

#contours1,hierarchy=cv.findContours(tresh1,1,2)

#cv.drawContours(img,contours1,-1,(255,255,255),1)
#cv.drawContours(img,contours1,1,(255,255,255),1)

#cnt1=contours1[2]

#cv.drawContours(img,[cnt1],0,(0,255,0),3)

#cv.imshow("Original image", img)
#cv.waitKey(0)
#cv.imwrite('Image.jpg', img)



print(imgray)

imgray[0][imgray.shape[1]-1]=0
imgray[imgray<80]=0
imgray[imgray>140]=0
print(imgray)
im2=Image.fromarray(imgray)

im2.save('Image.jpg')

im2 =cv.imread('Image.jpg')
imgray=cv.cvtColor(im2,cv.COLOR_BGR2GRAY)
cv.imshow('grg',imgray)
(thresh, im_bw) = cv.threshold(im2, 50, 255, cv.THRESH_BINARY)
cv.imshow('grg',im_bw)

ret, thresh = cv.threshold(imgray, 0, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(im_bw,contours,0,(0,255,0),1)
cv.drawContours(im_bw,contours,0,(0,255,0),1)

cnt=contours[4]
cv.drawContours(imgray,[cnt],0,(255,0,0),3)

cv.imshow("Original image", im_bw)
cv.waitKey(0)
