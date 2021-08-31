from selenium import webdriver as wd
import os.path
import io
import sys
import pyautogui as pg

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

options = wd.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = wd.Chrome(executable_path='chromedriver.exe')
#mainurl = 'https://www.coupang.com/np/search?component=&q=%EA%B0%84%EC%8B%9D'
#driver.get('https://www.11st.co.kr/main')
driver.get('https://www.naver.com/')
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/div/input').send_keys('간식')
driver.find_element_by_xpath('//*[@id="search_btn"]')
