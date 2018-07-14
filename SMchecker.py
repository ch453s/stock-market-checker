#----------------------------------------------pip install beautifulsoup4 and pynput ----------------------------------------------------

import bs4 as bs
import urllib.request
from pynput.keyboard import Key, Controller
import time

kp = Controller()

query = input('Enter a stock symbol:  ')
site = urllib.request.urlopen('https://www.investopedia.com/markets/stocks/' + query)
soup = bs.BeautifulSoup(site, 'lxml')

for section in soup.find_all('section'):
    section.extract()
    print(section.text)

    time.sleep(.5)
    kp.press(Key.enter)
    kp.release(Key.enter)
    kp.press(Key.enter)
    kp.release(Key.enter)
    kp.press(Key.enter)
    kp.release(Key.enter)
    kp.press(Key.enter)
    kp.release(Key.enter)
    kp.press(Key.enter)
    kp.release(Key.enter)
    
    



    input(' ')
    input(' ')
    input(' ')
    input(' ')
    input(' ')