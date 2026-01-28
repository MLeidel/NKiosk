# NKiosk RSS Viewer
**Headlines at your fingertips**

### Runs in Terminal 

Consists of two files: `nkiosk.py` and `nkiosk.lst`

Requires:

        beautifulsoup4==4.14.3
        Requests==2.32.5
        termcolor==3.3.0

Suggested usage:

        xfce4-terminal --geometry=88x50+100+20 -x news.sh &

        news.sh
            cd /p a t h/NKiosk
            python3 nkiosk.pyc

>Any terminal that supports __geometry__ is fine.

---

>
![terminal](images/nkiosk1.png "Runs in terminal")

---

> RSS feed urls stored in separate text file `nkiosk.lst`

>>
    https://www.chicagotribune.com/latest-headlines/feed/
    https://feeds.npr.org/1002/rss.xml
    https://feeds.npr.org/1003/rss.xml
    https://feeds.npr.org/1004/rss.xml
    https://feeds.npr.org/1014/rss.xml
    https://feeds.npr.org/1128/rss.xml
    http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml
    http://rss.nytimes.com/services/xml/rss/nyt/World.xml
    http://rss.nytimes.com/services/xml/rss/nyt/US.xml
    https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en

>You may have from 1 to 98 RSS urls. Store them in the `nkiosk.lst` text file, one line per URL.

---

### Navigation

At the bottom of each page you are prompted for input.  

When you hit:

    ENTER   advances to next rss feed  
    0 - 98  goes to that feed in your list
    99      ends program
    999     prints out your feeds from the `nkiosk.lst` file
    
---

inspired by the book:  
*Automate the Boring Stuff with Python*  
By Al Sweigart
	