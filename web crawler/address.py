import os.path
import time
import sys
import io
import re
from selenium import webdriver as wd
from tkinter import *
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

driver = wd.Chrome(executable_path='chromedriver.exe')
search = 'https://www.google.com/search?q='

f = open('mung_hospital2.csv', 'r')
rdr = csv.reader(f)
x = 1
for line in rdr:
    time.sleep(1.5)
    search = "".join(line)
    mainurl = f'https://www.google.com/search?q={search}'
    driver.get(mainurl)
    try:
        address = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/div/div[1]').text
        print(x,':', address)
        if x == 500:
            driver.quit()
            break
        else:
            x = x + 1
    except:
        print(x,':', '없음')
        pass
f.close()
