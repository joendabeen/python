num_list = list(range(1, 11))

print(list(map(lambda num: num**2, filter(lambda num: num % 2 == 0, num_list))))
