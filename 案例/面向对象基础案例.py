"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下。
1.添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
1.1输入学生姓名、语文成绩、数学成绩、英语成绩
1.2检查学生姓名是否已存在，如果学生不存在，再添加(存在则，不添加)
1.3 验证成绩范围(0-100分)
1.4 创建学生对象并添加到系统
2.修改学生成绩:根据输入的学生姓名，修改对应的学生成绩
2.1输入要修改的学生姓名
2.2根据姓名查找该学生，显示该生当前成绩信息
2.3 输入新的语文、数学、英语成绩
2.4更新学生成绩数据
3.删除学生成绩:根据输入的学生姓名，删除对应的学生成绩
4.查询指定学生成绩:根据输入的学生姓名，查找对应的学生成绩，并输出
4.1输出格式为:"姓名:张三|语文:85|数学:90|英语:88|总分:263"
5.展示全部学生成绩:展示出系统中所有学生的成绩
"""


#学生类
class Student :
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english

    def __str__(self):
        return f"姓名:{self.name}|语文:{self.chinese}|数学:{self.math}|英语:{self.english}|总分:{self.chinese+self.math+self.english}"

    #修改学生成绩
    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

#测试
if __name__ == '__main__':
    s1 = Student(name="王三",chinese=40,math=53,english=64)
    print(s1)

    s1.update_score(english=67)
    print(s1)


#教务管理系统类
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []#记录的是在校学生的成绩

    #添加学生成绩
    def add_student(self):
        name=input("请输入学生姓名:")

        #判断学生是否存在,如果存在,则添加失败(不能重复添加)
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在,添加失败")
                return

        chinese=int(input("请输入学生的语文成绩:"))
        if 0<= chinese <=100:
            math=int(input("请输入学生的数学成绩:"))
            if 0<= math <= 100:
                english = int(input("请输入学生的英语成绩:"))
                if 0<= english <= 100:
                    stu = Student(name,chinese,math,english)
                    self.student_list.append(stu)
                    print("学生信息添加成功")
                else:
                    print("成绩必须在0-100之间!")
                    return
            else:
                print("成绩必须在0-100之间!")
                return
        else:
            print("成绩必须在0-100之间!")
            return



    #修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩:{s}")
                change_subjects = input("请输入要修改的科目(仅一门):")
                match change_subjects:
                    case "语文":
                        chinese = int(input("请输入学生语文的成绩:"))
                        if 0<= chinese <= 100:
                            s.update_score(chinese=chinese)
                            print("成绩修改成功!")
                            print(f"修改后的成绩:{s}")
                            return
                        else:
                            return
                    case "数学":
                        math = int(input("请输入学生数学的成绩:"))
                        if 0<= math <= 100:
                            s.update_score(math=math)
                            print("成绩修改成功!")
                            print(f"修改后的成绩:{s}")
                            return
                        else:
                            return
                    case "英语":
                        english = int(input("请输入学生英语的成绩:"))
                        if 0<= english <= 100:
                            s.update_score(english=english)
                            print("成绩修改成功!")
                            print(f"修改后的成绩:{s}")
                            return
                        else:
                            return
                    case _:
                        print("请正确输入科目")
            else:
                print("学生不在系统内,请重新输入")
                return


    #删除学生成绩
    def delete_student(self):
        name=input("请输入要删除的学生姓名:")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("未找到该学生")


    #查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名:")

        for s in self.student_list:
            if s.name == name:
                print(f"学生信息:{s}")
                return
        print("未找到该学生")


    #展示全部学生的成绩
    def list_student(self):
        for s in self.student_list:
            print(s)

    #运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")

        while True:
            print("=============")
            print("1.添加学生")
            print("2.修改学生")
            print("3.删除学生")
            print("4.查询指定学生")
            print("5,查询所有学生")
            print("6.退出系统")
            print("=============")
            choice = int(input())
            match choice:
                case 1:#添加学生
                    self.add_student()
                    input("输入回车继续")
                case 2:#修改学生
                    self.update_student()
                    input("输入回车继续")
                case 3:#删除学生
                    self.delete_student()
                    input("输入回车继续")
                case 4:#查询指定学生
                    self.query_student()
                    input("输入回车继续")
                case 5:#查询所有学生
                    self.list_student()
                    input("输入回车继续")
                case 6:#退出系统
                    print("Bye")
                    break
                case _:
                    print("请输入正确序号")
                    continue

#测试
if __name__ == "__main__":
    edu_management = EduManagement()
    edu_management.run()



