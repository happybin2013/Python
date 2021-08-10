import os.path
import time
import sys
import io
from selenium import webdriver as wd
from tkinter import *
import cx_Oracle as orcCon
from cx_Oracle import DatabaseError
import os
import pandas as pd
from bs4 import BeautifulSoup as bs
import tkinter as tk

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 검색어 입력

sname = input("여행지를 입력해주세요: ")
if(os.path.isfile(sname + ".csv")):
    f = open(sname + ".csv","a", encoding="utf-8-sig")
    print("기존 파일에 추가합니다.")
else:
    f = open(sname + ".csv","w", encoding="utf-8-sig")
    #헤더 추가
    f.write("BLOG_NO, B_TITLE, B_NAME, B_THUMB, B_LINK\n")
    print(sname + ".csv 파일이 생성되었습니다.")

options = wd.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = wd.Chrome(executable_path='chromedriver.exe', options=options)
# main_url = 'https://www.naver.com/'
main_url = f"https://search.naver.com/search.naver?where=blog&query={sname}&sm=tab_opt&nso=so%3Ar%2Cp%3A1y"
regNo = '36030B'

st = time.time()
for x in range(10):
    driver.get(main_url)
    #메인에서 1~10번째 블로그까지 정보 추출
    bno = (regNo + str(x+1).zfill(3))
    title = driver.find_element_by_xpath("//*[@id='sp_blog_{}']/div/div/a".format(x+1)).text
    name = driver.find_element_by_xpath('//*[@id="sp_blog_{}"]/div/div/div[1]/div[2]/span/span/span[2]/a'.format(x+1)).text
    imgurl = driver.find_element_by_xpath("//*[@id='sp_blog_{}']/div/a/span/img".format(x+1)).get_attribute('src')
    link = driver.find_element_by_xpath("//*[@id='sp_blog_{}']/div/div/a".format(x+1)).get_attribute("href")
    title = title.replace(","," ")
    name = name.replace(",", " ")

    #출력
    print("\n\n{}.".format(x + 1) + title)
    print("블로그 이름 : " + name)
    print("썸네일 : " + imgurl)
    print("블로그 링크 : " + link)

    driver.get(link)
    driver.switch_to.frame('mainFrame')
    req = driver.page_source
    soup = bs(req,'lxml')
    contents = soup.find_all('strong',class_='se-map-title')

    for no, i in enumerate(contents, 1):
        print("코스정보", no, i.string)

    # 코스정보
    # 코스정보를 하나씩 리스트에 추가시키고
    # 하나씩 꺼내서 태그로 만든다.
    # 블로그 제목: ooo , 링크 : oooo.com , 담겨있는 코스정보 : #ooo #ooo

    # 크롤링 데이터 추가
    f.write(bno + ", " + title + ", " + name + ", " + imgurl + ", " + link + "\n")

et = time.time()
print(f"블로그 크롤링 시간 : {et-st:.2f}초")

f.close()
driver.quit()
time.sleep(5)

location = "D:\instantclient_19_11"
os.environ["PATH"] = location + ";" + os.environ["PATH"]

snsData = pd.read_csv(f'D:\web_workspace\Crawler\{sname}.csv')

# insert 문
try:
    conn = orcCon.connect('c##topping/c##topping@localhost:1521/xe')
    if conn:
        print("오라클 버전 : ", orcCon.version)
        cursor = conn.cursor()
        print("연결되었습니다.")
        print('데이터를 넣는 중입니다.')
        for i,row in snsData.iterrows():
            sql = "INSERT INTO TB_SNS(BLOG_NO, B_TITLE, B_NAME, B_THUMB, B_LINK) VALUES(:1,:2,:3,:4,:5)"
            cursor.execute(sql, tuple(row))
        conn.commit()
        print("성공적으로 진행되었습니다.")
except DatabaseError as e:
    err, = e.args
    print("Oracle-Error-Code:", err.code)
    print("Oracle-Error-Message:", err.message)
finally:
    cursor.close()
    conn.close()
