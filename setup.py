from setuptools import setup, find_packages


def read(filename):
    return [requirement.strip() for requirement in open(filename).readlines()]


PACKAGE = "ui_conversor_divisor"
NAME = "ui_conversor_divisor"
DESCRIPTION = "software for converting and splitting videos"
AUTHOR = __import__(PACKAGE).__author__
AUTHOR_EMAIL = "haddleytrindade@gmail.com"
URL = "https://github.com/hadtrindade/conversor-e-divisor"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    keywords="GUI for converting and splitting video using ffmpeg and mp4box",
    url=URL,
    description=DESCRIPTION,
    packeges=find_packages(
        exclude=[
            "tests",
            "dist",
            "build",
            "FFmpeg",
            "MP4Box",
            "conversor_divisor",
        ]
    ),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    classifiers=[
        "Environment :: GUI",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Framework :: Pytest",
    ],
    zip_safe=False,
)
