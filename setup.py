import io
import os

from setuptools import setup, find_packages


def read(*names, **kwargs):
    """Read a file."""
    content = ''
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8'),
    ) as open_file:
        content = open_file.read().strip()
    return content


PACKAGE = 'conversor_divisor'
NAME = 'conversor_divisor'
DESCRIPTION = 'software for converting and splitting medias'
AUTHOR = __import__(PACKAGE).__author__
AUTHOR_EMAIL = 'haddleytrindade@gmail.com'
URL = 'https://github.com/hadtrindade/conversor-e-divisor'
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license='MIT',
    keywords='GUI for converting and splitting medias using ffmpeg and mp4box',
    url=URL,
    description=DESCRIPTION,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=read('requirements.txt'),
    extras_require={'dev': read('requirements_dev.txt')},
    packages=find_packages(
        exclude=[
            'tests',
            'dist',
            'build',
        ]
    ),
    include_package_data=True,
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'conversor-divisor=conversor_divisor.app:start_app',
        ],
    },
    setup_requires=['setuptools>=38.6.0'],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Framework :: Pytest',
    ],
    zip_safe=False,
    platforms='any',
)
