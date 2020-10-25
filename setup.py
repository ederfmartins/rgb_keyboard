from setuptools import setup, find_packages
from codecs import open
from os import path
import os
here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def find_all(folder):
    for (path, _, filenames) in os.walk(folder):
        for filename in filenames:
            yield os.path.join("..", path, filename)


setup(
    name="rgb-keyboard",
    version="1.0.0",
    description="A Project to provide a driver and interface to control keyboard rgb led of ITE 8291 rev 0.02 like Avell laptops",
    entry_points={"console_scripts": [
        "keyboard_light = rgb_keyboard.__main__:main"]},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ederfmartins/rgb_keyboard",
    author="Eder Martins",
    packages=find_packages(),
    package_data={"": list(find_all("rgb_keyboard"))},
    include_package_data=True,
    install_requires=[
        "hid",
        "elevate"
    ],
    project_urls={
        "Bug Reports": "https://github.com/ederfmartins/rgb_keyboard/issues",
        "Source": "https://github.com/ederfmartins/rgb_keyboard",
    },
)
