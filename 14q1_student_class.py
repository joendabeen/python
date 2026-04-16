class Student:
    def __init__(self, grade, class_number, name):
        self.grade = grade
        self.class_number = class_number
        self.name = name

    def introduce(self):
        print(
            "안녕하세요? 저는 {}학년 {}반 {}입니다.".format(
                self.grade, self.class_number, self.name
            )
        )


student = Student(1, 2, "김가나")
student.introduce()
