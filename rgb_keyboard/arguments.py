import argparse

class Color:

    _COLORS = {
        "red": "#FF0000",
        "green": "#00FF00",
        "blue": "#0000FF",
        "teal": "#00FFFF",
        "purple": "#FF00FF",
        "pink": "#FF0077",
        "yellow": "#FF7700",
        "white": "#FFFFFF",
        "orange": "#FF1C00",
        "olive": "#808000",
        "maroon": "#800000",
        "brown": "#A52A2A",
        "gray": "#808080",
        "skyblue": "#87CEEB",
        "navy": "#000080",
        "crimson": "#DC143C",
        "darkgreen": "#006400",
        "lightgreen": "#90EE90",
        "gold": "#FFD700",
        "violet": "#EE82EE"
    }

    def __init__(self, color: str):
        color = Color._COLORS.get(color, color)
        if color[0] != "#":
            raise ValueError("Should pass a RGB code with pattern #RRGGBB")
        r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)
        self.rgb = [r, g, b]

    @staticmethod
    def choices():
        return Color._COLORS.keys()

class Pattern:
    _PATTERN = {
        "solid":            0x01,
        "breathing":        0x02,
        "wave":             0x03,
        "blinking":         0x12,
        "flow":             0x13,
        # todo paterns have not been verified
        # copied from - https://github.com/rodgomesc/avell-unofficial-control-center working driver for revision 0.03.
        # "random":           0x04,
        # "rainbow":          0x05,
        # "ripple":           0x06,
        # "reactiveripple":   0x07,
        # "marquee":          0x09,
        # "fireworks":        0x11,
        # "raindrop":         0x0A,
        # "aurora":           0x0E,
    }

    def __init__(self, pattern: str):
        self.pattern = Pattern._PATTERN.get(pattern, pattern)

    @staticmethod
    def choices():
        return Pattern._PATTERN.keys()


class UltimateHelpFormatter(
    argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter
):
    pass
