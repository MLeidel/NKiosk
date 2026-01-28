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
inx    = 0
nfeeds = len(nurls)  # number of xml urls in nurls list
nitems = 6  # max number of news items to print
wdesc  = 80  # width of description text for console


def display_urls():
    ''' Print the contents of nkiosk.lst '''
    os.system("clear")
    for i, v in enumerate(nurls):
        print(f"{i:02d}: {v}")

def prompt() -> int:
    ''' Get user input for navigation '''
    global inx, nfeeds
    while True:
        cprint("ENTER for next feed, 999 for feeds, 0 - 98, 99 to end: ", 'green', end="")
        stat = input().strip()
        if stat == "":
            inx += 1
            if inx == nfeeds:
                inx = 0
            return inx

        try:
            sub = int(stat)
        except ValueError:
            continue  # ignore non-numeric input

        if sub == 999:
            display_urls()
            continue  # go back to the prompt

        if sub == 99:
            exit(0)  # quit program

        #print(f"sub: {sub} nfeeds: {nfeeds}")
        if sub >= 0 and sub <= nfeeds:
            return sub
        else:
            continue

while True:
    r = requests.get(nurls[inx], timeout=15)
    xx = " -> " + str(inx) + " "

    data = r.text
    soup = BeautifulSoup(data, "xml")  # ready to parse rss

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

    inx = prompt()
