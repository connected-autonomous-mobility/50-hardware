# JETSON NANO
[fact sheet](https://elinux.org/Jetson_Nano)

## 1. [jetson_stats](https://github.com/rbonghi/jetson_stats) 
install: ```sudo -H pip3 install jetson-stats```

use: ```sudo jtop```

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
