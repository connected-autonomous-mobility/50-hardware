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

## 5. data
```
(env) rainer@rbnano1:~/mycar/data$ for i in $(find . -maxdepth 1 -type d) ; do echo -n $i": " ; (find $i -type f | wc -l) ; done | sort
.: 142000
./tub_16_19-03-10: 21085
./tub_18_19-03-10: 20435
./tub_36_19-04-13: 18273
./tub_6_19-03-09: 25885
./tub_64_19-06-15: 6841
./tub_66_19-06-15: 6841
./tub_67_19-06-15: 6841
./tub_68_19-06-15: 6841
./tub_69_19-06-15: 6841
./tub_9_19-03-09: 22117
```

## 6. training on Jetson Nano 
[for details please see post at diyrobocar slack channel](https://donkeycar.slack.com/archives/C4HR56WN6/p1569174142082900)

The maximum number of images I was able to train locally using command
```
(env) rainer@rbnano1:~/mycar$ 
time python ~/mycar/manage.py train --tub ~/mycar/data/lg_data/hive_imu_fast_racing \ 
                                    --model ./models/xxx.h5
```
was 9325 using dataset of Tawn Kramer

```~/mycar/data/lg_data/hive_imu_fast_racing```

and took ca. 32 minutes. 

Please not that you need to set the following parameters in the file ```myconfig.py``` and set MAX power:
```
CACHE_IMAGES = False
BATCH_SIZE = 16
```
Some screenshots
![](https://github.com/connected-autonomous-mobility/50-hardware/blob/master/images/training_on_jetson_nano.png)
![](https://github.com/connected-autonomous-mobility/50-hardware/blob/master/images/training_on_jetson_number.png)
![](https://github.com/connected-autonomous-mobility/50-hardware/blob/master/images/training_on_jetson_nano_time.png)
![](https://github.com/connected-autonomous-mobility/50-hardware/blob/master/images/training_on_jetson_nano_model_loss.png)
