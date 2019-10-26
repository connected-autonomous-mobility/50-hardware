[execute bluetoothctl without sudo](https://stackoverflow.com/questions/48279646/bluetoothctl-no-default-controller-available)

Here are the steps that worked for me by modifying the bluez config and the run without sudo:
```
Create a "bluetooth" group which will be granted with <allow send_destination="org.bluez"/> on bluez's d-bus config
$ sudo groupadd bluetooth

Open the config in /etc/dbus-1/system.d/bluetooth.conf with your favorite text editor

e.g.
$ sudo vi /etc/dbus-1/system.d/bluetooth.conf

Add/append the following lines below in /etc/dbus-1/system.d/bluetooth.conf


<policy group="bluetooth">
<allow send_destination="org.bluez"/>
</policy>

Save your changes.

Add your login user to "bluetooth" group

$ sudo usermod -a -G bluetooth <loginuser>

Reboot the system.

Then try to use "bluetoothctl" without sudo

$ bluetoothctl
[bluetooth]# show
```
