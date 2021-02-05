import os
from lib.waveshare_epd import epd7in5_V2
from PIL import Image, ImageDraw, ImageFont
import todoist
import datetime
import time

# from: https://medium.com/swlh/create-an-e-paper-display-for-your-raspberry-pi-with-python-2b0de7c8820c
# https://github.com/lemariva/ePaperWidgets/blob/master/e_paper_widget.py

pic_dir = 'pic'
display = epd7in5_V2.EPD()
w = display.height
h = display.width
image = Image.new('1', (h, w), 255)
draw = ImageDraw.Draw(image)
body = ImageFont.truetype(os.path.join(pic_dir, 'RobotoMono-Regular.ttf'), 48)

todoist_key = open("../.env", "r").read().rstrip("\n")

def main():
  try:
    display.init()
    display.Clear()

    draw.text((0, 0), 'Hello World.', font=body, fill=0, align='left')
    display.display(display.getbuffer(image))

    # time.sleep(3)
    # flower = Image.open('pic/flower.jpg')
    # image.paste(flower, (0, 0))
    # display.display(display.getbuffer(image))

    # time.sleep(3)
    display.Clear()

    show_date()
    to_display = get_todo()
    show_todo(to_display)
    display.display(display.getbuffer(image))

  except IOError as e:
    print(e)


def show_date():
  draw = ImageDraw.Draw(image)
  current_date = datetime.date.today().strftime('%a %b %d')
  draw.text((w, h), f'It\'s {current_date}', font=body, fill=0, align='right')

def show_todo(to_display):
  loc = 0
  for i in to_display:
    draw.text((0, loc), i, font=body, fill=0, align='right')
    loc += 50

def get_todo():
  api = todoist.TodoistAPI(todoist_key)
  api.sync()
  life_crap = api.projects.get_data(2223579159)['items']

  today = datetime.datetime.today()
  to_display = []
  for item in life_crap:
    if item['due'] != None:
      if datetime.datetime.strptime(item['due']['date'].split("T")[0], '%Y-%m-%d') <= today:
        to_display.append(item['content'])
  return to_display



if __name__ == '__main__':
  main()