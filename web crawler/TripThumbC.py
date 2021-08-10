import os.path
from time import sleep
import sys
import io
from future.backports.datetime import time
from selenium import webdriver as wd
from selenium.webdriver.support.ui import Select
from tkinter import *
from bs4 import BeautifulSoup as bs

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

options = wd.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")

driver = wd.Chrome(executable_path='chromedriver.exe', options=options)
main_url = 'https://api.visitkorea.or.kr/search/commonList.do'

driver.get(main_url)
# 관광지 typeid_12
# 음식점 typeid_39
# 레포츠 typeid_28
driver.find_element_by_id('contenttypeidAll').click()
driver.find_element_by_id('typeid_28').click()

# 지역선택
sleep(0.5)
driver.find_element_by_xpath('//*[@id="selectDiv"]/table/tbody/tr[3]/td/select[1]').click()
Select(driver.find_element_by_xpath('//*[@id="selectDiv"]/table/tbody/tr[3]/td/select[1]')).select_by_visible_text('전라남도')

# 시군구
sleep(1)
driver.find_element_by_xpath('//*[@id="selectDiv"]/table/tbody/tr[3]/td/select[2]').click()
Select(driver.find_element_by_xpath('//*[@id="selectDiv"]/table/tbody/tr[3]/td/select[2]')).select_by_visible_text('여수시')

# 검색버튼 클릭
driver.find_element_by_id('search').click()

#인기순으로 보기
driver.find_element_by_id('arrange').click()
Select(driver.find_element_by_id('arrange')).select_by_value('READCOUNT')
driver.find_element_by_id('arrangeView').click()

# 관광 음식점 50개씩
# 레포츠 20개씩
driver.find_element_by_id('numOfPage').click()
Select(driver.find_element_by_id('numOfPage')).select_by_value('10')
driver.find_element_by_id('numOfPageView').click()

# 보기 버튼 클릭
driver.find_element_by_id('AllView').click()

# 체크박스 기본만 남기고 해제
# driver.find_element_by_id('intro').click()
# driver.find_element_by_id('detail').click()

# 이미지 크롤링
f = open("여수레포츠썸네일" + ".csv", "w", encoding="ANSI")
f.write("TRIP_THUMB" + "\n")
driver.implicitly_wait(3)
x = 0
while x != 10:
    try:
        imgurl = driver.find_element_by_xpath("//*[@id='content']/div[2]/ul/li[{}]/div[1]/p/img".format(x + 1)).get_attribute('src')
        if imgurl != 'https://api.visitkorea.or.kr/static/images/common/noImage.gif':
            print(imgurl)
            f.write(imgurl + "\n")
        elif imgurl == 'https://api.visitkorea.or.kr/static/images/common/noImage.gif':
            imgurl = "noImage"
            print(imgurl)
            f.write(imgurl + "\n")
        x = x + 1
        print(x)
    except:
        imgurl = "noImage"
        print(imgurl)
        f.write(imgurl + "\n")
        x = x + 1
        print(x)
        continue
# //*[@id="content"]/div[2]/ul/li[1]/div[1]/p/img 1번사진
# //*[@id="content"]/div[2]/ul/li[2]/div[1]/p/img 2번 사진

# imgUrl = driver.find_element_by_xpath('/html/body/div/div/section/section[2]/div[2]').get_attribute('src')
# print(imgUrl)
print("썸네일csv 생성 완료")
driver.quit()
