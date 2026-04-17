str1 = input("피젯수")
str2 = input("젯수")  # 젯수 -> 0 division by zero exception

try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2
except ValueError:
    print("숫자 입력하삼")
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
except Exception as e:
    print("exception: ", e)
else:
    print("{} / {} = {}".format(num1, num2, result))
finally:
    print("처리 끝")
