g = 10

def fn():
    global g # 글로벌 변수
    g = 100

fn()

print('g=', g)