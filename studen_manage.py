class InvalidInputException(Exception):
    pass


class DuplicatedStudentException(Exception):
    pass


class Student:
    def __init__(self, id, name, sex):
        self.id = id
        self.name = name
        self.sex = sex


class StudentManagement:
    def __init__(self):
        self.student_list = []

    def addStudent(self, student):
        self.student = student
        if not isinstance(student, Student) or not student.id or not student.name or not student.sex:
            raise InvalidInputException("学员信息输入有误")
        for exit_student in self.student_list:
            if exit_student.id == student.id:
                raise DuplicatedStudentException("学号已存在")
        self.student_list.append(student)
        print(f"添加成功，添加的学员信息为：\n学号：{student.id},姓名：{student.name}，性别：{student.sex}")

    def showStudentInfo(self, student_id):
        for student in self.student_list:
            if student.id == student_id:
                print(f"学员信息获取成功，该学员的信息为：学号：{student.id}，姓名：{student.name}，性别{student.sex}")
                return
        print("未找到学员信息")

    def deleteStudent(self, student_id):
        for student in self.student_list:
            if student.id == student_id:
                self.student_list.remove(student)
                print(f"删除成功，删除的学员信息为：学号：{student.id}，姓名：{student.name}，性别{student.sex}\n删除后的学员信息为：")
                self.showAllStudents()
                return
        print("学员不存在")

    def showAllStudents(self):
        if not self.student_list:
            print("暂无学员信息")
        for student in self.student_list:
            print(f"学号：{student.id}，姓名：{student.name}，性别{student.sex}")


if __name__ == "__main__":
    management = StudentManagement()
    print("----------欢迎来到学员信息管理系统----------\n 1.根据学号查看学员信息\n 2.添加学员\n 3.根据学号删除后，查看所有学员信息\n 4.查询当前所有学员的信息\n 5.退出系统")

    while True:
        choice = input("请输入你的选择：")
        if choice == "2":
            try:
                new_student_id = input("请输入学员编号：")
                new_student_name = input("请输入学员姓名：")
                new_student_sex = input("请输入学员性别：")
                new_student = Student(new_student_id, new_student_name, new_student_sex)
                management.addStudent(new_student)
            except (InvalidInputException, DuplicatedStudentException) as e:
                print(e)
        elif choice == "1":
            student_id = input("请输入学员编号：")
            management.showStudentInfo(student_id)
        elif choice == "3":
            student_id = input("请输入学员编号：")
            management.deleteStudent(student_id)
        elif choice == "4":
            management.showAllStudents()
        elif choice == "5":
            print("成功退出系统，欢迎下次使用")
            break
        else:
            print("输入的选项无效")
