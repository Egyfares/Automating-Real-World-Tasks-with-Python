#!/usr/bin/env python3


import os
from PIL import Image


# open images

for i in os.listdir("images/"):
    if i != '.DS_Store':
        im = Image.open(os.path.join("images/",i))
        im = im.rotate(-90)
        im = im.resize((128,128))
        im = im.convert("RGB")
        im.save (os.path.join("/opt/icons/", i + ".jpeg"))
