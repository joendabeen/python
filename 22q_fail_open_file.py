try:
    with open("test11.txt", "r") as f:
        print(f.readline())
except FileNotFoundError:
    print("파일을 여는 중 예외 발생")
except Exception as e:
    print("exception: ", e)
