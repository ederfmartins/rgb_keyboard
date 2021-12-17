# RGB keyboard controler

Driver for ITE Device(8291) Rev 0.02 to control RGB keyboard ligths in Linux.

> **Note**:
> If your keyboard is ITE Device(8291) **Rev 0.03** use this driver https://github.com/rodgomesc/avell-unofficial-control-center instead.
'''

# How to discover if its the wright driver for me

Find out about your laptop's keyboard model

`sudo hwinfo --short`

It should show the ITE Device(8291) in the keyboard section:

```
keyboard:
                       Integrated Technology Express ITE Device(8291)
  /dev/input/event0    AT Translated Set 2 keyboard
```

There are two revisions for this device (rev 0.02 and rev 0.03). Confirm that this driver is for your device

`sudo hwinfo --keyboard`

```
...
Hardware Class: keyboard
Model: "Integrated Technology Express ITE Device(8291)"
Hotplug: USB
Vendor: usb 0x048d "Integrated Technology Express, Inc."
Device: usb 0xce00 "ITE Device(8291)"
Revision: "0.02" <-----------------------
...
```

# Dependencies

This drive has an external dependency over hid library. So install it first:

```
sudo apt install libhidapi-libusb
```

# Instalation


- Clone the repository
    - `git clone https://github.com/ederfmartins/rgb_keyboard.git`
- Build an installable package
    - `python3 setup.py build`
- Install the package
    - `sudo python3 setup.py install`


# Usage

```
usage: keyboard_light [-h] [-c COLORS] [-p {solid,breathing,wave,blinking,flow}] [-s SPEED] [-i INTENSITY] [-r]

Supply zero or more options [-c|s|i|p|r].
        Examples:
            keyboard_light
            keyboard_light -p solid
            keyboard_light -cred,#FF2200,#FF4400,blue -p wave -i 32 -s 8

optional arguments:
  -h, --help            show this help message and exit
  -c COLORS, --colors COLORS
                        Select colors to generate a light pattern. Use a comma separated list with #RRGGBB colors or {red,green,blue,teal,purple,pink,yellow,white,orange,olive,maroon,brown,gray,skyblue,navy,crimson,darkgreen,lightgreen,gold,violet}. (default: red,white,blue)
  -p {solid,breathing,wave,blinking,flow}, --pattern {solid,breathing,wave,blinking,flow}
                        Pattern of the effect. (default: breathing)
  -s SPEED, --speed SPEED
                        Speed of the effect transitions. 1 (fast) to 8 (slow), 0  is no transition. (default: 5)
  -i INTENSITY, --intensity INTENSITY
                        Intensity of the effect. 0 (low) to 32 (high). (default: 16)
  -r, --no_root_privileges
                        Set argument if no root privileges should be requested. (default: False)
```

# Throbleshooting

On some Ubuntu distributions it was reported some errors on the driver due to permission issues. If even running as root your driver fails with this exception:

```
File "/usr/local/lib/python3.8/dist-packages/hid-1.0.4-py3.8.egg/hid/init.py", line 130, in init
raise HIDException('unable to open device')
hid.HIDException: unable to open device
```
you could be in this situation. As workaroud, you should add a udev rule to force the permission to your user (https://askubuntu.com/questions/15570/configure-udev-to-change-permissions-on-usb-hid-device) to the device that your keyboard is connected (usb adapter). More preciselly, in `/etc/udev/rules.d` add a new conf file, like `50-usb-rgbkeyboard.conf` with the following content:

```  
SUBSYSTEM=="usb", ATTRS{idVendor}=="0x048d", ATTR{idProduct}=="0xce00", MODE="0666"
```

For more details see [#4](/../../issues/4).


# Contributions

Contributions of any kind are welcome. Please follow pep-8 coding style guides.

# This could be usefull

- https://github.com/rodgomesc/avell-unofficial-control-center working driver for revision 0.03.
- https://github.com/kirainmoe/hasee-tongfang-macos/issues/28 discussion about the rev 0.02 for this driver.
