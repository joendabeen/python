def hello():
    print("Hello World")


hello()

print()


# 가변 매개변수가 있는 함수
# 가변 매개변수에는 *을 붙임
# 가변 매개변수는 하나만 사용 가능하고 마지막에만 위치 가능
def hello4(greeting, *names):
    for name in names:
        print(greeting, name)


hello4("hi", "가나", "다라", "마바", "사아")

print()


# 함수 호출시 매개변수명을 사용
def function(first, second, third):
    return first + second + third


print(function(3, 5, 7))
print(function(first=3, second=5, third=7))
print(function(second=5, third=7, first=3))

print()


# 매개변수의 기본값
def function1(first=1, second=3, third=5):
    return first + second + third


print(function1())
print(function1(1, 2))
print(function1(second=1))

print()


def function2(first, second, third=5):
    return first + second + third


print(function2(1, second=5))
print(function2(second=5, first=1))

print()


# 반환형이 콜렉션일 때 unpacking
# 여러개 반환
def function3():
    return 1, "Hello", True


a, b, c = function3()
print(
    a,
    b,
    c,
)
a = function3()
print(a, type(a))

print()


# list를 반환했을 때
def ret_list():
    return [1, 2]


l = ret_list()
print(l)
n1, n2 = ret_list()
print(n1, n2)
n1, _ = ret_list()
print(n1)
