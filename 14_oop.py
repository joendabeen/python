class Person:
    # static 변수는 class 내부에 선언
    count = 0

    def __init__(self, n, a):
        self.hi = "Hello"
        self.name = n
        # python이라서 가능한 비교 연산                                                                                                                                                                                                                                                                 방법
        if 0 <= a <= 20:
            self.__age = a
        else:
            age = 0

    def info(self):  # 캡슐화
        return self.__age

    def inc_age(self):
        self.__age += 1

    def hello(self):
        print("{} {}".format(self.hi, self.name))
        print("당신은 {}살".format(self.__age))


person = Person("김가나", 13)
person.hello()
person.inc_age()
person.hello()
# print(person.__age) # error 비공개 속성
# person1 = Person()
# person1.hello()

print()


# 정적 메서드
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


print(Math.add(1, 2))
print(Math.sub(100, 29))
