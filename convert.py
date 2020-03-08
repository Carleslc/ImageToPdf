#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import argparse
import img2pdf
import wand.image

def set_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="directory with images to convert to pdf")
    parser.add_argument("--extension", help="image extension to convert", default='')
    args = parser.parse_args()

def files(dir, extension=''):
    for file in os.listdir(dir):
        path = os.path.abspath(dir + '/' + file)
        if os.path.isfile(path) and file.endswith(extension):
            yield path

def removeAlpha(image_path):
    with wand.image.Image(filename=image_path) as img:
        if img.alpha_channel:
            print('Removing alpha: ' + image_path)
            img.alpha_channel = 'remove'
            img.background_color = wand.image.Color('white')        
            img.save(filename=image_path)

if __name__ == "__main__":
    set_args()

    if not os.path.isdir(args.directory):
        print(args.directory + ' is not a directory!')
        exit()

    image_paths = sorted(list(files(args.directory, args.extension)))
    for image_path in image_paths:
        removeAlpha(image_path)

    path = os.path.abspath(args.directory + '.pdf')

    imgpdf = img2pdf.convert(image_paths)

    with open(path, "wb") as f:
        f.write(imgpdf)

    print('DONE: ' + path)