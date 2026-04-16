dic1 = {}
print(dic1)

dic2 = dict()
print(dic2)

dic3 = {"name": "item", 1: 3.5, False: [1, 2, 3]}
print(dic3)

dic4 = dict(name="김가나", height=160, age=20)
print(dic4)

print()

student = {"name": "김가나", "major": "장난과", "score": 3.5}
print(student["name"])
print(student["score"])
scores = {1: 3.5, 2: 4.0, 3: 4.3, 4: 4.2}
print(scores[1])
print(scores[2])

print()

# 수정, 추가
student["major"] = "컴퓨터짜잔과"
print(student)
student["grade"] = 4
print(student)
scores[2] = "4.5"
print(scores)
scores[5] = 5.0
print(scores)

print()

# 삭제
del student["name"]
print(student)
del scores[1]
print(scores)

print()

# key, value 가져오기
print(
    student.items()
)  # dict_items 객체로 반환 되어서 list로 쓰고 싶다면 아래와 같이 사용
print(list(student.items()))
print(student.keys())
print(list(student.keys()))
print(student.values())
print(list(student.values()))
