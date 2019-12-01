import os
import numpy as np
import cv2

# rbx
global IMG_W
global IMG_H
global IMG_NAME 
IMG_W=640 #1280 #3264 #1280
IMG_H=480 #720 #2464 #720
RES_NAME="_"+str(IMG_W)+"_"+str(IMG_H)
IMG_NAME="calimg"+RES_NAME
# rbx

#camera_matrix = np.load("camera_cal/camera_matrix.npy")
#dist_coeffs = np.load("camera_cal/dist_coeffs.npy")
camera_matrix = np.load("camera_cal/camera_matrix"+RES_NAME+".npy")
dist_coeffs = np.load("camera_cal/dist_coeffs"+RES_NAME+".npy")

new_camera_matrix = np.copy(camera_matrix)
new_camera_matrix[:2, :2] /= 2.

for jpgname in os.listdir("."):
    if not jpgname.endswith(".jpg"):
        continue
    if "undistort" in jpgname:
        continue
    jpg = cv2.imread(jpgname)
    # jpg_undist = cv2.fisheye.undistortImage(jpg[::4, ::4], camera_matrix, D=dist_coeffs, Knew=new_camera_matrix)
    jpg_undist = cv2.fisheye.undistortImage(jpg, camera_matrix, D=dist_coeffs, Knew=new_camera_matrix)
    cv2.imwrite(jpgname+'_undistort.jpg', jpg_undist)
    jpg_undist = cv2.fisheye.undistortImage(jpg, camera_matrix, D=np.zeros(4), Knew=new_camera_matrix)
    cv2.imwrite(jpgname+'_undistort_nodist.jpg', jpg_undist)
    # cv2.imshow('img', jpg_undist)
    # cv2.waitKey()

# cv2.destroyAllWindows()
# cv2.waitKey(1)
