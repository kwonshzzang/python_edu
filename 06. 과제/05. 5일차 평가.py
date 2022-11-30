import sqlite3
import re

# 1. 풀이

list = ["I", "study", "python", "language", "!"]

for c in list:
    if len(c) >= 3:
        print(c)

print()

# 2. 풀이

def createTable():
    try:
        conn = sqlite3.connect('my.db')
        print(type(conn))
        sql = 'create table if not exists grade(name varchar(20), kor int, eng int, math int)'
        conn.execute(sql)
        conn.close()
        print('create success')
    except Exception as err:
        print(err)

def insertFormat(name, kor, eng, math):
    try:
        conn = sqlite3.connect('my.db')
        sql =  'insert into grade(name, kor, eng, math) values(?,?,?,?)'
        conn.execute(sql, (name, kor, eng, math))
        conn.commit()
        conn.close()
        print('insert success')
    except Exception as err:
        print(err)

createTable()

# while True:
#     name = input('이름 :')
#     kor = int(input('국어 :'))
#     eng = int(input('영어 :'))
#     math = int(input('수학 :'))
#     insertFormat(name, kor, eng, math)
#     yn = input('계속 입력하시겠습니까(y/n)?')
#     if yn == 'n':
#         break
#
# def selectData():
#     try:
#         conn = sqlite3.connect('my.db')
#         sql = 'select * from grade'
#         cur = conn.cursor()
#         cur.execute(sql)
#         result = cur.fetchall()
#         conn.close()
#         return result
#     except Exception as err:
#         print(err)
#
# print('-'*30)
# print('이름', '국어', '영어', '수학', sep='\t')
# print('-'*30)
#
# result = selectData()
# for n, k, e, m in result:
#     print(n, k, e, m , sep='\t')

# 3. 풀이
s= '192.168.123.240 - - [01/Apr/2016:12:39:00 +0900] "GET /bg-middle.png HTTP/1.1" 200 1918'
# 1)	접속시간(01/Apr/2016:12:39:00) 문자열을 추출하시요.
# 2)	전송파일사이

try:
    match = re.search('\[([\w/:]+)', s)
    print( match.group(1) )
except Exception as err:
    print('not found')

try:
    match = re.search('\d+$', s)
    print(match.group())
except Exception as err:
    print(err)

# 4. 풀이
class Stock:
    def __init__(self, stock_name, stock_code, PER, PBR, profit):
        self.stock_name = stock_name
        self.stock_code = stock_code
        self.PER = PER
        self.PBR = PBR
        self.profit = profit


stock_collections = []
samsung = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
hyundai = Stock('현대자동차', '005380', 8.70, 0.35, 4.27)
lg = Stock('LG전자', '066570', 317.34, 0.69, 1.37)

stock_collections.append(samsung)
stock_collections.append(hyundai)
stock_collections.append(lg)

for i in stock_collections:
    print(i.stock_code, i.PER)

# 5. 풀이
per = ["10.31", "abc", "8.00"]
for i in per:
    try:
        print(float(i))
    except Exception as err:
        print(0)
