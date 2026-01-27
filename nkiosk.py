# nkiosk.py
# format/display RSS feeds in console
# to launch use:
#   gnome-terminal --geometry=88x40+100+100 -e python3 path/nkiosk.py

from bs4 import BeautifulSoup
from termcolor import cprint
import os
import requests, textwrap

List  = open("nkiosk.lst").readlines()  # read in the URLs from file
nurls = [i.strip() for i in List]

nfeeds = len(nurls)  # number of xml urls in nurls list
inx    = 0
nfeeds = len(nurls)  # number of xml urls in nurls list
nitems = 6  # max number of news items to print
wdesc  = 80  # width of description text for console

while True:
#   print(nurls[inx])
  r = requests.get(nurls[inx], timeout=15)
  xx = " - " + str(inx) + " "
  inx += 1
  if inx == nfeeds:
    inx = 0

  data = r.text
#   print(data)
  soup = BeautifulSoup(data, "xml")

  os.system('clear')
  obj = soup.find('title')
  cprint(obj.getText() + xx, 'green', attrs=['bold', 'reverse'])

  item = soup.find_all('item')

  for i in range(0, min(nitems, len(item))):
    ttl = item[i].find('title').getText()
    shoup = BeautifulSoup(ttl, "lxml")
    s = textwrap.fill(shoup.getText(), wdesc)
    cprint(s, 'yellow')
    # Descriptions
    desc = item[i].find('description').getText()
    shoup = BeautifulSoup(desc, "lxml")
    s = shoup.getText()
    print(textwrap.fill(s,wdesc))
    cprint(item[i].find('link').getText(), 'blue')
    print()

  cprint("ENTER for next feed, or 0 - 9 ENTER, or >9 ENTER to end: ", 'green', end="")
  stat = input()
  if stat.strip() != "":
      sub = int(stat.strip())
      if sub >=1 and sub <=9:
          inx = sub
      else:
          exit(0)
