num_list = list(range(1, 10))

num_list2 = list(map(lambda x: x**2, num_list))
print(num_list2)

# list comprehension이라는 것을 잊지말 것
# 꼭 대괄호로 감싸야 함
num_list3 = [x**2 for x in num_list]
print(num_list3)

num_list4 = [x**2 for x in range(1, 10)]
print(num_list4)

num_list5 = [
    x**2 for x in num_list if x > 5
]  # 뒤에 오는 조건이 filter와 같은 기능을 함
print(num_list5)

num_list6 = [x**2 for x in range(1, 10) if x % 2 == 0]
print(num_list6)
