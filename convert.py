#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import os
import argparse
import img2pdf

def set_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="directory with images to convert to pdf")
    parser.add_argument("--extension", help="image extensions to convert", default='')
    args = parser.parse_args()

def files(dir, extension=''):
    for file in os.listdir(dir):
        path = os.path.abspath(f'{dir}/{file}')
        if os.path.isfile(path) and file.endswith(extension):
            yield path

if __name__ == "__main__":
    set_args()

    if not os.path.isdir(args.directory):
        print(f'{args.directory} is not a directory!')
        exit()

    image_paths = sorted(list(files(args.directory, args.extension)))
    path = os.path.abspath(args.directory + '.pdf')

    with open(path, "wb") as f:
        f.write(img2pdf.convert(image_paths))

    print(f'DONE: {path}')