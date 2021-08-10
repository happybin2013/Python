import cx_Oracle as orcCon
from cx_Oracle import DatabaseError
import os
import pandas as pd

#오라클 라이브러리 연결 : 오라클 드라이버 등록과 같음
# 방법 1 : 환경변수에 등록
location = "D:\instantclient_19_11"
os.environ["PATH"] = location + ";" + os.environ["PATH"]

snsData = pd.read_csv('D:\web_workspace\Crawler\순천여행.csv')

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
