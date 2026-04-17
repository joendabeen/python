from functools import reduce

num_list = list(range(1, 11))

result = reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 0, num_list))
print(result)
