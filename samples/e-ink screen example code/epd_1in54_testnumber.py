#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd1in54_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback


# Drawing on the image
logging.info("1.Drawing on the image...")
image = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
draw.text((8, 12), '100', font = font, fill = 255)
#The first parameter is a tuple of coordination of character, 
#the second parameter is the font and last one is set the color.