import os.path
import time
import sys
import io
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs

#한글 사용가능
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

driver = wd.Chrome(executable_path='chromedriver.exe')
# main_url = 'https://www.naver.com/'
main_url = "https://dogpre.com/recent-products?category=036"
driver.get(main_url)

for x in range(1,11):
    img = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/div[2]/main/div[2]/div/div[{}]/div/a/div[1]/picture/img'.format(x)).get_attribute('src')
    title = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/div[2]/main/div[2]/div/div[{}]/div/a/div[2]/h3'.format(x)).text
    price = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/div[2]/main/div[2]/div/div[{}]/div/a/div[2]/div[1]/strong'.format(x)).text

    print(x,"번째 상품")
    print('썸네일 : ', img)
    print('제목 : ', title)
    print('가격 : ', price,'\n')