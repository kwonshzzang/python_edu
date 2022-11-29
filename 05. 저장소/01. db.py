import sqlite3
# my.db 접속 없으면 생성 후 접속 있으면 접속
def createTable():
    try:
        conn = sqlite3.connect('my.db')
        print(type(conn))
        sql = 'create table if not exists student(name varchar(20), age int, birth date)'
        conn.execute(sql)
        conn.close()
    except Exception as err:
        print(err)

def insertData():
    try:
        conn = sqlite3.connect('my.db')
        sql = "insert into student(name, age, birth) values('홍길동', 20, '1989-12-10')"
        conn.execute(sql)
        conn.commit() # insert, delete, update(명령확정)
        conn.close()
        print('insert success')
    except Exception as err:
        print(err)

def insertFormat():
    try:
        conn = sqlite3.connect('my.db')
        sql ="insert into student(name, age, birth) values(?, ?, ?)"
        conn.execute('이순신', 40, '1978-12-31')
        conn.commit() # insert, delete, update(명령확정)
        conn.close()
        print('insert success')
    except Exception as err:
        print(err)

def updateData():
    try:
        conn = sqlite3.connect('my.db')
        # sql = "update student set name = '홍길동', age=23 where name='홍길동'"
        sql = "update student set name=?, age=? where name=?"
        conn.execute(sql, ('이순신1', 45, '이순신'))
        conn.commit() # insert, delete, update(명령확정)
        conn.close()
        print('update success')
    except Exception as err:
        print(err)

def deleteData():
    try:
        conn = sqlite3.connect('my.db')
        sql = "delete from student where name = '이순신1'"
        conn.execute(sql)
        conn.commit() # insert, delete, update(명령확정)
        conn.close()
        print('delete success')
    except Exception as err:
        print(err)

#insertFormat()

def selectData():
    try:
        conn = sqlite3.connect('my.db')
        sql = "select * from student"
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        conn.close()
        print(result)
        for n, a, b in result:
            print(n, a, b)
    except Exception as err:
        print(err)
