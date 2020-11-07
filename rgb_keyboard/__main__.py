import argparse
import textwrap
from elevate import elevate
import os

from rgb_keyboard.driver import KeyboardControler

parser = argparse.ArgumentParser(
    description=textwrap.dedent("""Supply at least one of the options [-c|w|s]."""),
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument("-c", "--color", help="Select a single color for all keys. Use #RRGGBB pattern")
parser.add_argument("-w", "--wave", help="Select 4 to 7 colors to generate a wave light pattern. Use a comma separated list with #RRGGBB colors")
parser.add_argument("-s", "--speed", help="Speed of the effect transitions. 1 (fast) to 5 (slow)")

def parse_color(color):
    colors = {
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
    return colors.get(color, color)


def parse_wave(wave_colors):
    wave_colors = [parse_color(color) for color in wave_colors.split(",")]
    return ",".join(wave_colors)


def main():
    parsed = parser.parse_args()
    if parsed.color:
        if not os.geteuid() == 0:
            elevate()
        controler = KeyboardControler()
        controler.solid_color(parse_color(parsed.color))
    elif parsed.wave:
        wave = "#ff0000,#00b400,#0000ff,#ff00ff,#0000FF,#00B4FF,#FF00FF"
        if len(parsed.wave.split(",")) >= 4:
            wave = parse_wave(parsed.wave)
        speed = parsed.speed or 5
        if not os.geteuid() == 0:
            elevate()
        controler = KeyboardControler()
        controler.wave_color(wave, speed)


if __name__ == "__main__":
    main()
