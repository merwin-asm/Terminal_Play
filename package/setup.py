from setuptools import setup, find_packages
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.26'
DESCRIPTION = "Play videos on your terminal; Works on windows as well as linux;The video played will also have color and sound :)"

# Setting up
setup(
    name="terminalplay",
    version=VERSION,
    author="Merwin JD",
    license='MIT',
    author_email="merwin@fbi.ac",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
        project_urls = {
        "Bug Tracker": "https://github.com/merwin-asm/Terminal_Play/issues",
    },
    url='https://github.com/merwin-asm/Terminal_Play',

    install_requires=['moviepy',
          'playsound',
          'rich',
          'sty',
          'opencv-python'],
    keywords=['terminalplay', 'play videos', "terminal"],
      platforms= ["windows","linux"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
