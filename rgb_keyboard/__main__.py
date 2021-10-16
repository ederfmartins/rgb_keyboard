import argparse
import textwrap
from elevate import elevate
import os

from rgb_keyboard.driver import KeyboardControler
from rgb_keyboard.arguments import Color, Pattern


parser = argparse.ArgumentParser(
    description=textwrap.dedent(
        """Supply zero or more options [-c|s|i|p|r].
            Exsamples:
                keyboard_light
                keyboard_light -p solid
                keyboard_light -cred,#FF2200,#FF4400,blue -p wave -i 32 -s 8
        """),
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument("-c", "--colors",
                    help=f"Select colors to generate a light pattern. "
                         f"Use a comma separated list with #RRGGBB colors or {{{','.join(Color.choices())}}}.",
                    default="red,white,blue")
parser.add_argument("-p", "--pattern",
                    help="Pattern of the effect.",
                    default="breathing",
                    choices=Pattern.choices())
parser.add_argument("-s", "--speed",
                    help="Speed of the effect transitions. 1 (fast) to 8 (slow), 0  is no transition.",
                    default=5, type=int)
parser.add_argument("-i", "--intensity",
                    help="Intensity of the effect. 0 (low) to 32 (high).",
                    default=16, type=int)
parser.add_argument("-r", "--no-root", dest='root', action='store_false',
                    help="Do not use root privileges.",
                    default=True)

def main():
    parsed = parser.parse_args()
    colors = [Color(color) for color in parsed.colors.split(",")]
    colors = _expand_colors_to(colors, 7)
    pattern = Pattern(parsed.pattern)

    if not os.geteuid() == 0 and parsed.root:
        elevate()

    KeyboardControler().send_args(colors, pattern, parsed.intensity, parsed.speed)

def _expand_colors_to(colors: list[Color], to: int):
    # repeat colors until there are amount of colors
    number_of_suplied_colors = len(colors)
    number_of_expanded_colors = 0
    expanded_colors = []
    while len(expanded_colors) < to:
        expanded_colors.append(colors[number_of_expanded_colors % number_of_suplied_colors])
        number_of_expanded_colors += 1
    return expanded_colors

if __name__ == "__main__":
    main()
