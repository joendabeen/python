ages = [18, 19, 39, 12, 43, 13, 21, 25]


def adult_func(age):
    if age >= 19:
        return True
    else:
        return False


for age in filter(adult_func, ages):
    print(age)

print()

age_list = []
for age in filter(lambda age: age >= 19, ages):
    age_list.append(age)
print(age_list)
