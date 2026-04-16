for i in range(10):
    print("Hello World!", end=" ")

print()

for i in range(1, 10):
    print("Hello World!", i, end=" ")

print()

for i in range(10, 0, -1):
    print(i, end=" ")

print()

# iterator
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
    print(num, end=" ")

print()

fruits = ("apply", "orange", "grape")
for fruit in fruits:
    print(fruit, end=" ")

print()

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in tuple1:
    print(num, end=" ")

print()

# Multiple Tables
str_count = input("반복할 횟수를 입력하세요: ")
count = int(str_count)

for i in range(count):
    print("Hello, world!", i, end=" ")

print()

for i in range(2):
    for fruit in fruits:
        print(i, fruit, end=" ")
