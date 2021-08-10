import time
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver as wd
import sys
import io
import datetime
import pyperclip as pc
from tkinter import *
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import os
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

driver = wd.Chrome(executable_path="chromedriver.exe")
main_url = 'http://www.danawa.com/'

#Cpu 검색
def Cpu(): #cpu중에서 인기 순위 10등까지 순위, 제품명, 가격(시세) 가져오기
    # 카테고리에서 cpu 검색 후 클릭
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # cpu 인기제품에서 제품명,링크 가져오기
    pipl = soup.find_all(class_='prod_item prod_layer')

    print("\n~~~~~~~~~~~다나와 Cpu 인기순위~~~~~~~~~~~")
    k = 1
    #반복시작
    for i in pipl[:5]: #5등까지의 제품
        Cname = str(i.select('div.prod_info > p > a'))
        print("%s등 Cpu: " %k + Cname[158:187]) #제품명
        print("링크 주소: " + i.a.attrs['href']) #제품 링크
        Price = str(i.select('p.price_sect > a > strong')[:1]).replace(',', '')  # 가격 전처리
        Price1 = int(re.findall("\d+", Price)[0])
        print("정품 가격: " + str(Price1) + "원")  # 제품의 정품 가격
        k += 1
        print("=" * 66)
        time.sleep(1)

#Ram 검색
def Ram():
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # cpu 인기제품에서 제품명,링크 가져오기
    pipl = soup.find_all(class_='prod_item prod_layer width_change')

    print("\n~~~~~~~~~~~다나와 Ram 인기순위~~~~~~~~~~~")
    k = 1
    #반복시작
    for i in pipl[:5]: #5등까지의 제품
        Cname = str(i.select('div.prod_info > p > a'))
        print("%s등 Ram: " %k + Cname[158:187]) #제품명
        print("링크 주소: " + i.a.attrs['href']) #제품 링크
        Price = str(i.select('p.price_sect > a > strong')[:1]).replace(',', '')  # 가격 전처리
        Price1 = int(re.findall("\d+", Price)[0])
        print("정품 가격: " + str(Price1) + "원")  # 제품의 정품 가격
        k += 1
        print("=" * 66)

#Board 검색
def Board():
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # cpu 인기제품에서 제품명,링크 가져오기
    pipl = soup.find_all(class_='prod_item prod_layer')

    print("\n~~~~~~~~~~다나와 Board 인기순위~~~~~~~~~~")
    k = 1
    #반복시작
    for i in pipl[:5]: #5등까지의 제품
        Cname = str(i.select('div.prod_info > p > a'))
        print("%s등 Board: " %k + Cname[158:180]) #제품명
        print("링크 주소: " + i.a.attrs['href']) #제품 링크
        Price = str(i.select('p.price_sect > a > strong')[:1]).replace(',','')#가격 전처리
        Price1 = int(re.findall("\d+", Price)[0])
        print("정품 가격: " + str(Price1) + "원")# 제품의 정품 가격
        k += 1
        print("=" * 66)
        time.sleep(1)

#VGA 검색
def VGA():
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # cpu 인기제품에서 제품명,링크 가져오기
    pipl = soup.find_all(class_='prod_item prod_layer width_change')

    print("\n~~~~~~~~~~~다나와 VGA 인기순위~~~~~~~~~~~")
    k = 1
    # 반복시작
    for i in pipl[:5]:  # 5등까지의 제품
        Cname = str(i.select('div.prod_info > p > a'))
        print("%s등 VGA: " % k + Cname[158:206])  # 제품명
        print("링크 주소: " + i.a.attrs['href'])  # 제품 링크
        Price = str(i.select('p.price_sect > a > strong')[:1]).replace(',', '')  # 가격 전처리
        Price1 = int(re.findall("\d+", Price)[0])
        print("정품 가격: " + str(Price1) + "원")  # 제품의 정품 가격
        k += 1
        print("=" * 66)

#SSD 검색
def SSD():
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # cpu 인기제품에서 제품명,링크 가져오기
    pipl = soup.find_all(class_='prod_item prod_layer')

    print("\n~~~~~~~~~~~다나와 SSD 인기순위~~~~~~~~~~~")
    k = 1
    # 반복시작
    for i in pipl[:5]:  # 5등까지의 제품
        Cname = str(i.select('div.prod_info > p > a'))
        print("%s등 SSD: " % k + Cname[158:180])  # 제품명
        print("링크 주소: " + i.a.attrs['href'])  # 제품 링크
        Price = str(i.select('p.price_sect > a > strong')[:1]).replace(',', '')  # 가격 전처리
        Price1 = int(re.findall("\d+", Price)[0])
        print("정품 가격: " + str(Price1) + "원")  # 제품의 정품 가격
        k += 1
        print("=" * 66)
        time.sleep(1)

#HDD 검색
def HDD():
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # cpu 인기제품에서 제품명,링크 가져오기
    pipl = soup.find_all(class_='prod_item prod_layer')

    print("\n~~~~~~~~~~~다나와 HDD 인기순위~~~~~~~~~~~")
    k = 1
    # 반복시작
    for i in pipl[:5]:  # 5등까지의 제품
        Cname = str(i.select('div.prod_info > p > a'))
        print("%s등 HDD: " % k + Cname[158:191])  # 제품명
        print("링크 주소: " + i.a.attrs['href'])  # 제품 링크
        Price = str(i.select('p.price_sect > a > strong')[:1]).replace(',', '')  # 가격 전처리
        Price1 = int(re.findall("\d+", Price)[0])
        print("정품 가격: " + str(Price1) + "원")  # 제품의 정품 가격
        k += 1
        print("=" * 66)
        time.sleep(1)

for cate in range(1,7):
    driver.get(main_url)
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="danawa_header"]/div[2]/div/div[1]/a').click()
    driver.implicitly_wait(1)
    driver.find_element_by_class_name('nav_menu03').click() #컴 노트북 조립pc 누르기
    driver.find_element_by_xpath('//*[@id="categoryExplodeLayer11"]/div[3]/div[1]/ul/li[{}]/a'.format(cate)).click()
    #주요부품 누르기

    # Cpu 검색
    if cate == 1:
        Cpu()
        continue
    elif cate == 2:
        Ram()
        continue

    elif cate == 3:
        Board()
        continue

    elif cate == 4:
        VGA()
        continue

    elif cate == 5:
        SSD()
        continue

    elif cate == 6:
        HDD()
        break
driver.close()

"""
for i in range(1):
    try:

        driver.execute_script('javascript:movePage(%s); return false;' % page)
        print("%s 페이지 이동" % page)
        time.sleep(3)

    except Exception as e1:
        print('오류', e1)

    except Exception as e1:
        print('오류', e1)
    # 위에는 다나와 페이지 넘기는 문장
"""
# 자바스크립트 구동하여 페이지 넘기는 것...



