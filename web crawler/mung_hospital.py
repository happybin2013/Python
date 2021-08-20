import os.path
import time
import sys
import io
from selenium import webdriver as wd
from tkinter import *
from bs4 import BeautifulSoup as bs

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

f = open("mung_hospital.csv","w", encoding="utf-8")
#헤더 추가
f.write("NO, NAME, ADDRESS\n")
print("mung_hospital.csv 파일이 생성되었습니다.")

options = wd.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = wd.Chrome(executable_path='chromedriver.exe',options=options)

st = time.time()
no2 = 1
for page in range(1,52):
    driver.get(f"https://www.animal.go.kr/front/awtis/shop/hospitalList.do?totalCount=5048&pageSize=100&menuNo=6000000002&&page={page}")
    #메인에서 1~10번째 블로그까지 정보 추출
    for no in range(1,101):
        try:
            name = driver.find_element_by_xpath('/html/body/div/div[5]/div[2]/div[2]/form/div[2]/table/tbody/tr[{}]/td[2]'.format(no)).text
            address = driver.find_element_by_xpath('/html/body/div/div[5]/div[2]/div[2]/form/div[2]/table/tbody/tr[{}]/td[4]'.format(no)).text
            print(no2, "|", name, "|", address)
            # 크롤링 데이터 추가
            f.write(str(no2) + ", " + name + ", " + address + "\n")
            no2 += 1
        except:
            pass

et = time.time()
print(f"블로그 크롤링 시간 : {et-st:.2f}초")

f.close()
driver.quit()