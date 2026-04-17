max_value = max(1, 30, 50)
print(max_value)

min_value = min(1, 30, 50)
print(min_value)

max_str = min("AAC", "ABC", "ACC")
print(max_str)

min_str = max("AAC", "ABC", "ACC")
print(min_str)

length = len("안녕하세요")
print(length)

# eval() 별로 권장하는 방법은 아님
result = eval("10 + 20 + 30 + 40")
print(result)

result = eval("not 40 > 50")
print(result)

list = [2, 5, 5, 3, 9, 1]
print(sorted(list))

# 객체의 고유 아이디 그러나 자주 사용하지는 않음
str1 = "안녕하세요"
str_id = id(str1)
print(str_id)

list_id = id([1, 2, 3, 4, 5])
print(hex(list_id))
print(oct(list_id))

print(type(3.14))
print(type([1, 2, 3, 4, 5]))

print(abs(-5))
