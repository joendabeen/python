num_list1 = [x**2 for x in range(1, 11)]
print(num_list1)

num_list2 = [x for x in range(1, 21) if x % 2 == 0]
print(num_list2)

num_list3 = [x for x in range(1, 21) if x % 3 == 0]
print(num_list3)

num_list4 = [x**2 for x in range(1, 21) if x % 5 == 0]
print(num_list4)

# 데이터 개수가 x 값의 개수 * y 값의 개수가 됨
num_list5 = [x + y for x in range(1, 5) for y in range(1, 3)]
print(num_list5)
