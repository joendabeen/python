# immutable
student = ("김가나", "감자튀김학과", 3, 17.5, 2.3, True)
print(student)
print(student[0])
# student[0] = "박다라" # immutable error

car = ("tesla", "model3", "red", 600)
print(car)

# range 사용한 생성
range1 = range(10)
tuple1 = tuple(range1)
print(tuple1)
range2 = range(-5, 15, 2)
print(tuple(range2))
