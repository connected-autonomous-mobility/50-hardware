# JETSON NANO
[fact sheet](https://elinux.org/Jetson_Nano)

## 1. [jetson_stats](https://github.com/rbonghi/jetson_stats) 
install: ```sudo -H pip3 install jetson-stats```

usage: ```sudo jtop```

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
[installation](https://thenewstack.io/tutorial-configure-nvidia-jetson-nano-as-an-ai-testbed/)

testing
```
cd ~/projects/jetson-inference/build/aarch64/bin
rainer@rbnano1:~/projects/jetson-inference/build/aarch64/bin$ ./detectnet-camera
```

## 5. bluetooth
```
sudo apt-get install jstest-gtk
jstest-gtk
```


## 6. training on Jetson Nano 
[for details please see post at diyrobocar slack channel](https://donkeycar.slack.com/archives/C4HR56WN6/p1569174142082900)

### Hint: drive in chunks of 5 minutes and train approx. 10K images ###


The maximum number of images I was able to train locally using command
```
(env) rainer@rbnano1:~/mycar$ 
time python ~/mycar/manage.py train --tub ~/mycar/data/lg_data/hive_imu_fast_racing \ 
                                    --model ./models/xxx.h5
```
was 9325 using [dataset](https://github.com/connected-autonomous-mobility/20-data)

```~/mycar/data/lg_data/hive_imu_fast_racing```

out of Tawn Kramers dataset collection and took approx. 32 minutes. 

## 20.10.2019
```
time python ~/d2/manage.py train --tub ~/d2/data/lg_data/hive_imu_fast_racing --model ./models/xxx.h5
```


Please not that you need to set the following parameters in the file ```myconfig.py``` and set MAX power:
```
CACHE_IMAGES = False
BATCH_SIZE = 16
```
Activate ```jetson_clocks```
Some screenshots
![](https://github.com/connected-autonomous-mobility/50-hardware/blob/master/images/training_on_jetson_nano.png)
![](https://github.com/connected-autonomous-mobility/50-hardware/blob/master/images/training_on_jetson_number.png)
![](https://github.com/connected-autonomous-mobility/50-hardware/blob/master/images/training_on_jetson_nano_time.png)
![](https://github.com/connected-autonomous-mobility/50-hardware/blob/master/images/training_on_jetson_nano_model_loss.png)

more results

|images | min   | epochs  | remarks     | dataset               | model      |
|-------|-------|---------|-------------|-----------------------|------------|
|10126 | 46     |         |             | hive_imu_fast_racing_2|            |
|12032 | 25     | 16      |             | sim_warehouse_manual  |            |
| 9120 | 33     | 19      | crop_top_50 | athena_rainer_bosch   |Athena_crop50.h5|
|12942 |        |         | crop_top_50 | tub_6_xx              | crash      |
|10542 |        |         | crop_top_50 | tub_16_xx             | crash      |

links
[jetson-inference](https://github.com/dusty-nv/jetson-inference)

## 7. Qt5 installation
[guide](https://devtalk.nvidia.com/default/topic/1056075/jetson-nano-and-qt5/)

## 8. Display X remotely
[guide](https://www.techotopia.com/index.php/Displaying_Ubuntu_Linux_Applications_Remotely_(X11_Forwarding))
```
/etc/ssh/ssh_config:
X11Forward yes
 
ssh -X user@hostname
```
## 9. Remote Jupyter Notebook
[guide](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html)

## 10. Install VSCODE

[guide](https://code.headmelted.com/#linux-install-scripts)

## 11. Install conda

[guide](https://github.com/helmut-hoffer-von-ankershoffen/jetson/blob/master/workflow/deploy/ml-base/src/Dockerfile)

```
wget --quiet -O archiconda.sh https://github.com/Archiconda/build-tools/releases/download/0.2.3/Archiconda3-0.2.3-Linux-aarch64.sh && \
    sh archiconda.sh -b -p /opt/archiconda3 && \
    rm archiconda.sh
```

## 12. TensorRT

```
(env) rainer@rbnano4:~/d2$ python /usr/lib/python3.6/dist-packages/uff/bin/convert_to_uff.py ./models/rb_ufftest.pb


+-----------------------+-------+------+------+--------+
|          part         |  max  | min  | avg  | median |
+-----------------------+-------+------+------+--------+
|       CSICam_rbx      |  2.65 | 0.02 | 0.05 |  0.04  |
|   LocalWebController  |  1.96 | 0.03 | 0.04 |  0.04  |
| PS3JoystickController |  0.63 | 0.02 | 0.04 |  0.04  |
|     ThrottleFilter    |  0.84 | 0.01 | 0.02 |  0.02  |
|     PilotCondition    |  0.09 | 0.01 | 0.01 |  0.01  |
|     RecordTracker     |  0.40 | 0.01 | 0.02 |  0.01  |
|        Mpu6050        |  0.43 | 0.02 | 0.02 |  0.02  |
|      FileWatcher      | 18.45 | 0.05 | 0.25 |  0.07  |
|       DriveMode       |  0.32 | 0.02 | 0.03 |  0.02  |
|        AiLaunch       |  2.50 | 0.01 | 0.02 |  0.02  |
|     AiRunCondition    |  0.23 | 0.01 | 0.01 |  0.01  |
|      PWMSteering      | 38.70 | 1.64 | 2.48 |  1.87  |
|      PWMThrottle      | 20.43 | 1.54 | 2.22 |  1.78  |
+-----------------------+-------+------+------+--------+
terminate called without an active exception
Aborted (core dumped)
(env) rainer@rbnano4:~/d2$ python manage1.py drive --model=./models/rb_ufftest.uff --type='tensorrt_linear'


+-----------------------+-------+------+------+--------+
|          part         |  max  | min  | avg  | median |
+-----------------------+-------+------+------+--------+
|       CSICam_rbx      |  0.12 | 0.03 | 0.04 |  0.04  |
|   LocalWebController  |  0.27 | 0.03 | 0.04 |  0.04  |
| PS3JoystickController |  0.12 | 0.02 | 0.04 |  0.04  |
|     ThrottleFilter    |  0.08 | 0.01 | 0.02 |  0.02  |
|     PilotCondition    |  0.07 | 0.01 | 0.01 |  0.01  |
|     RecordTracker     |  0.08 | 0.01 | 0.01 |  0.01  |
|        Mpu6050        |  0.09 | 0.02 | 0.02 |  0.02  |
|      FileWatcher      |  2.72 | 0.05 | 0.12 |  0.07  |
|       DriveMode       |  0.11 | 0.02 | 0.03 |  0.03  |
|        AiLaunch       |  0.06 | 0.01 | 0.02 |  0.02  |
|     AiRunCondition    |  0.03 | 0.01 | 0.01 |  0.01  |
|      PWMSteering      | 12.55 | 1.65 | 2.37 |  1.89  |
|      PWMThrottle      | 14.20 | 1.56 | 2.17 |  1.81  |
+-----------------------+-------+------+------+--------+
terminate called without an active exception
Aborted (core dumped)
(env) rainer@rbnano4:~/d2$ python manage1.py drive --model=./models/rb_ufftest.h5 


```


## 12. Automagic FanControl

[guide](https://github.com/Pyrestone/jetson-fan-ctl.git)

## 13. PyTorch

[link](https://devtalk.nvidia.com/default/topic/1049071/pytorch-for-jetson-nano-version-1-3-0-now-available/)
```
# not working #
pip3 install numpy torch-1.3.0-cp36-cp36m-linux_aarch64.whl
```
[new](https://zhangtemplar.github.io/pytorch/)

## scipy
```
sudo apt-get install python3-scipy
```
