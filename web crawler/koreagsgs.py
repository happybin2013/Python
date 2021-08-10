import os.path
import time
import sys
import io
from selenium import webdriver as wd
from tkinter import *

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 검색어 입력
sname = input("여행지를 입력해주세요: ")
if(os.path.isfile(sname + "구석구석.csv")):
    f = open(sname + ".csv","a", encoding="utf-8-sig")
    print("기존 파일에 추가합니다.")
else:
    f = open(sname + "구석구석.csv","w", encoding="utf-8-sig")
    #헤더 추가
    f.write("BLOG_NO, B_TITLE, B_THUMB, 썸네일\n")
    print(sname + "구석구석.csv 파일이 생성되었습니다.")

options = wd.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")

driver = wd.Chrome(executable_path='chromedriver.exe', options=options)
# main_url = 'https://www.naver.com/'

st = time.time()

main_url = f"https://korean.visitkorea.or.kr/search/search_list.do?keyword={'강릉'}"
driver.get(main_url)
for x in range(10):

    #메인에서 1~10번째 블로그까지 정보 추출
    try:
        title = driver.find_element_by_xpath("//*[@id='listBody']/ul/li[{}]/div[2]/div[1]".format(x+1)).text
        imgurl = driver.find_element_by_xpath("//*[@id='listBody']/ul/li[{}]/div[1]/a/img".format(x+1)).get_attribute('src')
        name = driver.find_element_by_xpath("//*[@id='listBody']/ul/li[{}]/div[2]/div[2]/p".format(x + 1)).text
        title = title.replace(","," ")
        name = name.replace(",", " ")
    except:
        continue
    #출력
    print("\n\n{}.".format(x + 1) + title)
    print("썸네일 : " + imgurl)
    print("글쓴이: " + name)

    # 크롤링 데이터 추가
    f.write(title + ", " + name + ", " + imgurl + "\n")
et = time.time()
print(f"구석구석 크롤링 시간 : {et-st:.2f}초")

driver.quit()