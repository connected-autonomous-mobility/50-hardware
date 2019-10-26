```
(env2) rainer@rbnano1:~/projects$ uvcdynctrl -f -d video1
[libwebcam] Invalid V4L2 control type encountered: ctrl_id = 0x009A0001, name = 'Camera Controls', type = 6
[libwebcam] Invalid or unsupported V4L2 control encountered: ctrl_id = 0x009A0001, name = 'Camera Controls'
[libwebcam] Unknown V4L2 camera class (UVC) control ID encountered: 0x009A2003 (V4L2_CID_CAMERA_CLASS_BASE + 5891)
[libwebcam] Warning: Unsupported V4L2 control type encountered: ctrl_id = 0x009A2008, name = 'Sensor Mode', type = 5
[libwebcam] Invalid or unsupported V4L2 control encountered: ctrl_id = 0x009A2008, name = 'Sensor Mode'
[libwebcam] Warning: Unsupported V4L2 control type encountered: ctrl_id = 0x009A2009, name = 'Gain', type = 5
[libwebcam] Invalid or unsupported V4L2 control encountered: ctrl_id = 0x009A2009, name = 'Gain'
[libwebcam] Warning: Unsupported V4L2 control type encountered: ctrl_id = 0x009A200A, name = 'Exposure', type = 5
[libwebcam] Invalid or unsupported V4L2 control encountered: ctrl_id = 0x009A200A, name = 'Exposure'
[libwebcam] Warning: Unsupported V4L2 control type encountered: ctrl_id = 0x009A200B, name = 'Frame Rate', type = 5
[libwebcam] Invalid or unsupported V4L2 control encountered: ctrl_id = 0x009A200B, name = 'Frame Rate'
[libwebcam] Invalid V4L2 control type encountered: ctrl_id = 0x009A2064, name = 'Bypass Mode', type = 9
[libwebcam] Invalid or unsupported V4L2 control encountered: ctrl_id = 0x009A2064, name = 'Bypass Mode'
[libwebcam] Invalid V4L2 control type encountered: ctrl_id = 0x009A2065, name = 'Override Enable', type = 9
[libwebcam] Invalid or unsupported V4L2 control encountered: ctrl_id = 0x009A2065, name = 'Override Enable'
[libwebcam] Unknown V4L2 camera class (UVC) control ID encountered: 0x009A2066 (V4L2_CID_CAMERA_CLASS_BASE + 5990)
[libwebcam] Invalid V4L2 control type encountered: ctrl_id = 0x009A2067, name = 'Size Align', type = 9
[libwebcam] Invalid or unsupported V4L2 control encountered: ctrl_id = 0x009A2067, name = 'Size Align'
[libwebcam] Unknown V4L2 camera class (UVC) control ID encountered: 0x009A2068 (V4L2_CID_CAMERA_CLASS_BASE + 5992)
[libwebcam] Unknown V4L2 camera class (UVC) control ID encountered: 0x009A206D (V4L2_CID_CAMERA_CLASS_BASE + 5997)
[libwebcam] Unknown V4L2 camera class (UVC) control ID encountered: 0x009A2082 (V4L2_CID_CAMERA_CLASS_BASE + 6018)
Listing available frame formats for device video1:
Pixel format: YUYV (YUYV 4:2:2; MIME type: video/x-raw-yuv)
  Frame size: 640x480
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 160x120
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 176x144
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 320x176
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 320x240
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 432x240
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 352x288
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 544x288
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 640x360
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 752x416
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 800x448
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 864x480
    Frame intervals: 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 960x544
    Frame intervals: 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1024x576
    Frame intervals: 1/15, 1/10, 2/15, 1/5
  Frame size: 800x600
    Frame intervals: 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1184x656
    Frame intervals: 1/15, 1/10, 2/15, 1/5
  Frame size: 960x720
    Frame intervals: 1/15, 1/10, 2/15, 1/5
  Frame size: 1280x720
    Frame intervals: 1/10, 2/15, 1/5
  Frame size: 1392x768
    Frame intervals: 1/10, 2/15, 1/5
  Frame size: 1504x832
    Frame intervals: 2/15, 1/5
  Frame size: 1600x896
    Frame intervals: 2/15, 1/5
  Frame size: 1280x960
    Frame intervals: 2/15, 1/5
  Frame size: 1712x960
    Frame rates: 5
  Frame size: 1792x1008
    Frame rates: 5
  Frame size: 1920x1080
    Frame rates: 5
Pixel format: MJPG (Motion-JPEG; MIME type: image/jpeg)
  Frame size: 640x480
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 160x120
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 176x144
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 320x176
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 320x240
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 432x240
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 352x288
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 544x288
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 640x360
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 752x416
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 800x448
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 864x480
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 960x544
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1024x576
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 800x600
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1184x656
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 960x720
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1280x720
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1392x768
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1504x832
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1600x896
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1280x960
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1712x960
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1792x1008
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
  Frame size: 1920x1080
    Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5
```
