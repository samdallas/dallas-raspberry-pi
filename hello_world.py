import os
from lib.waveshare_epd import epd7in5_V2
from PIL import Image, ImageDraw, ImageFont
import time

# from: https://medium.com/swlh/create-an-e-paper-display-for-your-raspberry-pi-with-python-2b0de7c8820c

pic_dir = 'pic'

try:
  display = epd7in5_V2.EPD()
  display.init(display.lut_full_update)
  display.Clear(0)

  w = display.height
  h = display.width
  print (w, h)

  image = Image.new('1', (h, w), 255)
  draw = ImageDraw.Draw(image)
  body = ImageFont.truetype(os.path.join(pic_dir, 'RobotoMono-Regular.ttf'), 48)
  draw.text((0, 0), 'Hello World.', font=body, fill=0, align='left')
  display.display(display.getbuffer(image))

  time.sleep(3)
  flower = Image.open('pic/flower.jpg')
  image.paste(flower, (0, 0))
  display.display(display.getbuffer(image))


except IOError as e:
  print(e)
