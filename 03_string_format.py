str1 = "{}".format(10)
print(str1)

str2 = "{}과 {}".format(10, 20)
print(str2)

num1 = 10
num2 = 20
str3 = "{}x{}={}".format(num1, num2, num1 * num2)
print(str3)

age = 20
name = "김가나"

str4 = "이름은 {} 나이는 {}".format(name, age)
print(str4)
str5 = "이름은 {0} 나이는 {1}".format(name, age)
print(str5)
str6 = "이름은 {1} 나이는 {0}".format(age, name)
print(str6)

str7 = "이름은 {:s} 나이는 {:d}".format(name, age)
print(str7)
print("pi = {:f}".format(3.141592))
print("pi = {:10f}".format(3.141592))
print("pi = {:5.2f}".format(3.141592))
print("pi = {:.2f}".format(3.141592))

# string 서식지정자
print("이름은 %s 나이는 %d" % (name, age))
print("이름은 %s 나이는 %5d" % (name, age))
print("이름은 %s 나이는 %05d" % (name, age))
print("pi = %f" % 3.141592)
print("pi = %5.2f" % 3.141592)
print("pi = %.2f" % 3.141592)
