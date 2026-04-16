items = [1, 3, "Hello", 5.6, False, 89, "World!"]

scores = [30, 40, 50, 60, 10220412]
print(scores[-1])

# scores[5] = 400   # out of range

# append(), insert()
# 둘 다 새로 추가 됨
scores.append("HI")
scores.insert(8, 23)  # list index를 넘어가면 맨 뒤에 추가함
print(scores)

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9, 10]

print(list1 + list2)  # list 결합
print(list2 + list1)
print(list1 * 3)  # 기존 list를 3번 반복한 list
print(list2 * 3)

# len()
print(len(scores))

# slice
numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10]
numbers1 = numbers[0:4]
print(numbers1)
print(numbers[:4])
print(numbers[7:11])
print(numbers[7:])
print(numbers[:])

# range([start], stop, [step])
# start default 0, step default 1

r1 = range(1, 10, 1)
r2 = range(10, 1)
r3 = range(10, 0, -1)

list1 = list(range(10))
print(list1)
list2 = list(range(1, 10))
print(list2)
list3 = list(range(1, 10, 2))
print(list3)
list4 = list(range(10, 0, -1))
print(list4)
