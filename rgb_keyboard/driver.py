"""
Driver for RGB LED keyboard backlight controller Integrated Technology Express ITE Device(8291) Rev 0.02.

This device uses a usb connector. So, controling it is just a matter of write the right bytes on device.
"""
import os
from ctypes import create_string_buffer
import hid


class KeyboardControler:
    """
    Controler to configure the RGB keyboard lights. 
    """

    def __init__(self, vendor_id=0x048d, product_id=0xce00):
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.color_flag_prefix = [0x14, 0x00]
        self.color_flag_suffix = [0x00, 0x00]
        self.pattern_flag_prefix = [0x08, 0x02]

    def solid_color(self, rgb: str):
        """
        Lightnning all keys with the same color.

        rgb: str with the selected color. Pattern #RRGGBB where RR, GG, and BB are hexcodes.
        """
        rgb = self._rgb_to_array(rgb)
        # There are 4 regions in the keyboard, for each one we should set the color
        cmds = [
            self.color_flag_prefix + [region] + rgb + self.color_flag_suffix
            for region in range(1, 5)
        ]
        # And define other properties
        fixed_color, speed, intensity = 0x01, 0x05, 0x32
        solid_pattern = self.pattern_flag_prefix + [fixed_color, speed, intensity, 0x08, 0x00, 0x01]
        cmds.append(solid_pattern)
        self._send_command(*cmds)

    def wave_color(self, wave_rgb: str, speed=0x05):
        """
        Lightnning the keyboard with a wave color pattern.

        wave_rgb: str with a list of colors.
        """
        # There are 4-7 regions in the keyboard, for each one we should set a color
        rgbs = [self._rgb_to_array(rgb) for rgb in wave_rgb.split(",")]
        cmds = [
            self.color_flag_prefix + [region] + rgb + self.color_flag_suffix
            for region, rgb in enumerate(rgbs, 1)
        ]
        # And define other properties
        wave_color, intensity = 0x03, 0x32
        pattern = self.pattern_flag_prefix + [wave_color, speed, intensity, 0x08, 0x00, 0x01]
        cmds.append(pattern)
        self._send_command(*cmds)

    def _rgb_to_array(self, rgb):
        if rgb[0] != "#":
            raise ValueError("Should pass a RGB code with pattern #RRGGBB")
        r, g, b = int(rgb[1:3], 16), int(rgb[3:5], 16), int(rgb[5:], 16)
        return [r, g, b]

    def _send_command(self, *cmds):
        with hid.Device(self.vendor_id, self.product_id) as h:
            h.nonblocking = 1
            for cmd in cmds:
                buf = self._c_str(cmd)
                h.send_feature_report(buf)

    def _c_str(self, cmd):
        data = bytearray(cmd)
        buf = create_string_buffer(len(data))
        for n in range(len(data)):
            buf[n] = data[n]
        return buf
