import os
from lib.waveshare_epd import epd7in5_V2
from PIL import Image, ImageDraw, ImageFont
from datetime import date
import time

# from: https://medium.com/swlh/create-an-e-paper-display-for-your-raspberry-pi-with-python-2b0de7c8820c

pic_dir = 'pic'
display = epd7in5_V2.EPD()
w = display.height
h = display.width
image = Image.new('1', (h, w), 255)
draw = ImageDraw.Draw(image)
body = ImageFont.truetype(os.path.join(pic_dir, 'RobotoMono-Regular.ttf'), 48)

def main():
  try:
    display.init()
    display.Clear()

    draw.text((0, 0), 'Hello World.', font=body, fill=0, align='left')
    display.display(display.getbuffer(image))

    time.sleep(3)
    flower = Image.open('pic/flower.jpg')
    image.paste(flower, (0, 0))
    display.display(display.getbuffer(image))

    time.sleep(3)
    show_date()

  except IOError as e:
    print(e)


def show_date():
  draw = ImageDraw.Draw(image)
  current_date = date.today().strftime('%a %b %d %Y')
  draw.text((0, 0), f'It\'s {current_date}', font=body, fill=0, align='left')
  display.display(display.getbuffer(image))


if __name__ == '__main__':
  main()