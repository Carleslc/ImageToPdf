# ImageToPdf
_Merge images in a single pdf._

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C2VFGD)

## Install

1. Install [Python 3](https://www.python.org/downloads/)

    - (Optional) Use `virtualenv`:

    ```bash
    sudo pip install virtualenv
    virtualenv env
    . env/bin/activate # Bash/Tcsh console
    . env/bin/activate.fish # Fish console
    ```

2. Install dependencies:

    ```bash
    pip install img2pdf
    pip install Wand
    brew install imagemagick
    ```

## Usage

```
usage: convert.py [-h] [--extension EXTENSION] directory

positional arguments:
  directory             directory with images to convert to pdf

optional arguments:
  -h, --help            show this help message and exit
  --extension EXTENSION
                        image extension to convert
```
