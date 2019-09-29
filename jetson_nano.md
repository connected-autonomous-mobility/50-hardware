# JETSON NANO
[fact sheet](https://elinux.org/Jetson_Nano)

## 1. [jetson_stats](https://github.com/rbonghi/jetson_stats) 
install: ```sudo -H pip3 install jetson-stats```

use: ```sudo jtop```

```
(env) rainer@rbnano1:~$ jetson_release
 - NVIDIA Jetson NANO/TX1
   * Jetpack 4.2.1 [L4T 32.2.0]
   * CUDA GPU architecture 5.3
 - Libraries:
   * CUDA 10.0.326
   * cuDNN 7.5.0.56-1+cuda10.0
   * TensorRT 5.1.6.1-1+cuda10.0
   * Visionworks 1.6.0.500n
   * OpenCV 4.1.0 compiled CUDA: YES
 - Jetson Performance: inactive
```


## 2. power management
[power management](https://www.jetsonhacks.com/2019/04/10/jetson-nano-use-more-power)

check mode:
```sudo nvpmodel -q```

To set the mode to 5 Watt mode:
```$ sudo nvpmodel -m 1```
<br>
To set it back to 10 Watt mode:
```$ sudo nvpmodel -m 0```

## 3. performance management
```sudo jetson_clocks --show```

## 4. inference samples
installation: ```https://thenewstack.io/tutorial-configure-nvidia-jetson-nano-as-an-ai-testbed/```

using
```
cd ~/projects/jetson-inference/build/aarch64/bin
rainer@rbnano1:~/projects/jetson-inference/build/aarch64/bin$ ./detectnet-camera
```
