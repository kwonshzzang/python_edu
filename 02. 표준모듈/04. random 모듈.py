import random

for n in range(5):
    rn = random.randint(1, 5)  # 1 <= 임의의 숫자 <=5
    print(rn)

print('='*30)

my = [1, 2, 3, 4, 5]
random.shuffle(my)
print(my)

s = random.choice(my)
print(s)

print(random.sample(my, 2))
