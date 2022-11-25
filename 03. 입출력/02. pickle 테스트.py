# 객체 시리얼라이즈(Serialize)
# 객체 저장(덤프), 하드디스크 -> 메모리 객체(로드)

import pickle

def obWrite():
    my = [10, 20, 30, 40]

    fp = open('ob.dat', 'wb')
    pickle.dump(my, fp)
    fp.close()

# obWrite()

fp = open('ob.dat', 'rb')
rd = pickle.load(fp)
print(rd)
print(type(rd))
fp.close()