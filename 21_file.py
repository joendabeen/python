with open("test.txt", "r+") as f:
    text = f.read()
    print(text)

with open("test.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

    for line in lines:
        print(line)

# 덮어쓰기 됨
text = "안녕하세요.\n 파이썬\n반갑"
with open("test.txt", "w") as f:
    f.write(text)

texts = ["안녕하세요", "python", "반갑"]
with open("test.txt", "a") as f:
    f.writelines(texts)
