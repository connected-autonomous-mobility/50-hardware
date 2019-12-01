# MIT License
# Copyright (c) 2019 JetsonHacks
# See license
# Using a CSI camera (such as the Raspberry Pi Version 2) connected to a
# NVIDIA Jetson Nano Developer Kit using OpenCV
# Drivers for the camera and OpenCV are included in the base image

import cv2

# gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
# Defaults to 1280x720 @ 60fps
# Flip the image by setting the flip_method (most common values: 0 and 2)
# display_width and display_height determine the size of the window on the screen

"""
capture_width=3264, #1280,
capture_height=2464, #720,
display_width=3264, #1280,
display_height=2464, #720,
"""

global IMG_W
global IMG_H
global IMG_NAME 
global RES_NAME
IMG_W=640 #1280
IMG_H=480 #720
#IMG_NAME="calimg_"+str(IMG_W)+"_"+str(IMG_H)+"_"
RES_NAME="_"+str(IMG_W)+"_"+str(IMG_H)+"_"
IMG_NAME="calimg"+RES_NAME

def gstreamer_pipeline(
    capture_width=IMG_W, #160, #1280,
    capture_height=IMG_H, #720,
    display_width=IMG_W, #160, #1280,
    display_height=IMG_H, #120, #720,
    framerate=21, #60,
    flip_method=2,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


def show_camera():
    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    print(gstreamer_pipeline(flip_method=2))
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=2), cv2.CAP_GSTREAMER)
    n_img = 0
    if cap.isOpened():
        window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
        # Window
        while cv2.getWindowProperty("CSI Camera", 0) >= 0:
            ret_val, img = cap.read()
            cv2.imshow("CSI Camera", img)
            # This also acts as
            keyCode = cv2.waitKey(30) & 0xFF
            # Stop the program on the ESC key
            if keyCode == 27:
                break
            if keyCode == 115:
                calimg_name = "./images_calibration/"+IMG_NAME+str(n_img)+".jpg"
                print("saving image: "+calimg_name)

                #calimg_name = "./images_calibration/calimag_160_120_"+str(n_img)+".jpg"
                #calimg_name = "./images_calibration/calimag_"+str(n_img)+".jpg"
                #calimg_name = "./images_street/street_"+str(n_img)+".jpg"
                cv2.imwrite(calimg_name, img)
                n_img += 1
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Unable to open camera")


if __name__ == "__main__":
    show_camera()
