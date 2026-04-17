def add(x, y):
    return x + y


f = lambda x, y: x + y

print(add(1, 2))
print(f(1, 2))

f = lambda x: x if x % 3 == 0 else 0
print(f(3))
print(f(4))

print()

nums1 = [1, 2, 3, 4, 5]


# map
def pow(x):
    return x**2


f = lambda x: x**2

print(list(map(pow, nums1)))
print(list(map(f, nums1)))
print(list(map(lambda x: x**2, nums1)))

print()

nums2 = [6, 7, 8, 9, 10]
print(list(map(lambda x, y: x * y, nums1, nums2)))
