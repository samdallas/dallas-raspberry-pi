import os
from lib.waveshare_epd import epd7in5b_V2
from PIL import Image, ImageDraw, ImageFont

# from: https://medium.com/swlh/create-an-e-paper-display-for-your-raspberry-pi-with-python-2b0de7c8820c

try:
  display = epd7in5b_V2.EPD()
  display.init(display.lut_full_update)
  display.Clear(0)

  w = display.height
  h = display.width
  print (w, h)

  image = Image.new(mode='I', size=(w, h))
  draw = ImageDraw.Draw(image)
  draw.text((0, 0), 'Hello World.', fill=0, align='left')
  display.display(display.getbuffer(image))

except IOError as e:
  print(e)
