set1 = {1, 2, 3}
set1.add(4)
print(set1)

set1.update([4, 5, 6])
print(set1)

set1.remove(5)
print(set1)

set2 = set([0, 1, 2, 3, 4, 5, 6])
set3 = set([4, 5, 6, 7, 8, 9, 10])
# 교집합
print(set2 & set3)
print(set2.intersection(set3))
# 합집합
print(set2 | set3)
print(set2.union(set3))
# 차집합
print(set2 - set3)
print(set2.difference(set3))
