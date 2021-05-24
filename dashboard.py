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
# width is 480, height is 800
# when specifying, (across, height)
h = display.height
w = display.width
image = Image.new('1', (w, h), 255)
draw = ImageDraw.Draw(image)
body = ImageFont.truetype(os.path.join(pic_dir, 'RobotoMono-Regular.ttf'), 48)

todoist_key = open("../.env", "r").read().rstrip("\n")

def main():
  try:
    display.init()
    display.Clear()

    show_date()

    todo = get_todo()
    show_items(todo, 0)

    # events = get_events()
    # show_items(events, h-100)

    display.display(display.getbuffer(image))

  except IOError as e:
    print(e)


def show_date():
  draw = ImageDraw.Draw(image)
  current_date = datetime.date.today().strftime('%a %b %d')
  draw.text((500, 425), current_date, font=body, fill=0, align='right')

def show_items(items, x_loc):
  loc = 0
  for i in items[0:8]:
    draw.text((x_loc, loc), i, font=body, fill=0, align='right')
    loc += 50

def get_todo():
  # sort by oldest eventually
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

# def get_events():


if __name__ == '__main__':
  main()
