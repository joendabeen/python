import random

print(random.random())
print(random.randrange(1, 7))  # 1~6 난수 하나 발생
print(random.randint(1, 7))  # 1~7 난수 하나 발생

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(list1)
print(list1)
print(random.choice(list1))  # 하나를 임의로 선택
print(random.sample(list1, 5))  # 5개의 아이템을 임의로 선택
