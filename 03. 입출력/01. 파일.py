def fileWrite1():
    fp = open('test.txt', 'w')
    print(fp)
    print(type(fp))
    fp.write('hello')
    fp.close()

def fileRead1():
    fp = open('test.txt', 'r')
    rd = fp.read()
    fp.close()
    print(rd)

def fileWrite2():
    fp = open('test.txt', 'w')
    print(fp.tell())
    fp.write('hello')
    fp.seek(2)
    print(fp.tell())
    fp.write('korea')
    print(fp.tell())
    fp.close()

def fileRead2():
    fp = open('test.txt', 'r')
    print(fp.tell())
    rd = fp.read(2)
    print(rd)

    fp.seek(1)

    print(fp.tell())
    rd = fp.read(2)
    print(rd)
    print(fp.tell())
    fp.close()

def fileRead3():
    fp = open('test.txt', 'r')
    while True:
        rd = fp.read(2)
        if rd == '':
            break
        print(rd)
    fp.close()

def fileWrite3():
    fp = open('test.txt', 'w')
    fp.write('abc\ndef\nghi')
    fp.close()

def fileRead4():
    fp = open('test.txt', 'r')
    rd = fp.readline()
    print(rd)
    fp.close()

def fileRead5():
    fp = open('test.txt', 'r')
    for n in fp:
        print(n)
    fp.close()

def fileRead6():
    fp = open('test.txt', 'r')
    rd = fp.readlines()
    print(rd)
    rd = [n.strip() for n in rd]
    print(rd)
    fp.close()

def fileWrite4():
    fp = open('test.txt', 'w')
    fp.write('kor\nea')
    fp.close()

# 콘솔 10번코드 개행
# 윈도우 에디터 -> 13, 10
fp = open('test.txt', 'r')
rd = fp.read()
print(len(rd))
print(rd)
fp.close()

# 텍스트 모드 read 01 -> r -- 13, 10