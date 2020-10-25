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
Usage: keyboard_light [-h] [-c COLOR] [-w WAVE] [-s SPEED]

Supply at least one of the options [-c|w|s].

optional arguments:
  -h, --help            show this help message and exit
  -c COLOR, --color COLOR
                        Select a single color for all keys. Use #RRGGBB pattern
  -w WAVE, --wave WAVE  Select 4 to 7 colors to generate a wave light pattern. Use a comma separated list with #RRGGBB colors
  -s SPEED, --speed SPEED Speed of the effect transitions. 1 (fast) to 5 (slow)
```

# Contributions

Contributions of any kind are welcome. Please follow pep-8 coding style guides.

# This could be usefull

- https://github.com/rodgomesc/avell-unofficial-control-center working driver for revision 0.03.
- https://github.com/kirainmoe/hasee-tongfang-macos/issues/28 discussion about the rev 0.02 for this driver.
