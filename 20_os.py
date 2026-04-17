import os

dir(os)

print(os.sep)  # 경로구분자
cur_dir = os.getcwd()  # 현재 작업경로
print(cur_dir)
test_dir = os.path.join(cur_dir, "test")  # 경로 생성
print(test_dir)

print(os.path.exists(test_dir))
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
print(os.path.exists(test_dir))
