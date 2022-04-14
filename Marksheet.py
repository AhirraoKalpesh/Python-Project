from collections import OrderedDict
from operator import getitem


class student:
    dict1 = {}
    dict2 = {}
    n = int(input("Enter No. of Students: "))

    def get_info(self):
        for i in range(1, student.n+1):
            self.name, self.roll_no, self.m1, self.m2, self.m3 = input(
                "Enter Values: ").split(" ")
            self.total = int(self.m1)+int(self.m2)+int(self.m3)
            self.per = self.total/300
            self.per1 = ("{:.2f}".format(self.per*100))
            self.per2 = float(self.per1)
            # print(self.per2)
            # print(type(self.per2))
            student.dict1 = dict({self.roll_no: {"name": self.name, "m1": self.m1,
                                                 "m2": self.m2, "m3": self.m3, "total": self.total, "per": self.per2}})
            student.dict2.update(student.dict1)

    def dist(self):
        c1, c2, c3, c4 = 0, 0, 0, 0
        for i, j in student.dict2.items():
            for k, m in j.items():
                if k == "per":
                    if m >= 75:
                        c1 += 1
                    elif m >= 60 and m < 75:
                        c2 += 1
                    elif m >= 35 and m < 60:
                        c3 += 1
                    elif m < 35:
                        c4 += 1
                    else:
                        pass
        print("\nStudents with distinction = ", c1)
        print("Students with first class = ", c2)
        print("Student with pass class = ", c3)
        print("Students who failed = ", c4)

    def sort_roll(self):
        l1 = [(k, v) for k, v in student.dict2.items()]

        def fun(e):
            return e[0]

        l1.sort(key=fun)

        self.dict3 = dict(l1)
        print(f"Roll No\t\tName\t\tSub1\t\tSub2\t\tSub3\t\tTotal\t\tPercentage")
        for i, j in self.dict3.items():
            print(i, "\t\t", end=" ")
            for k, m in j.items():
                print(m, "\t\t", end=" ")
            print()

    def sort_name(self):
        self.res = OrderedDict(
            sorted(student.dict2.items(), key=lambda x: getitem(x[1], "name")))
        self.dict4 = dict(self.res)
        # print(self.dict4)
        print(f"Roll No\t\tName\t\tSub1\t\tSub2\t\tSub3\t\tTotal\t\tPercentage")
        for i, j in self.dict4.items():
            print(i, "\t\t", end=" ")
            for k, m in j.items():
                print(m, "\t\t", end=" ")
            print()

    def sort_per(self):
        self.res = OrderedDict(
            sorted(student.dict2.items(), key=lambda x: getitem(x[1], "per")))
        self.dict4 = dict(self.res)
        # print(self.dict4)
        print(f"Roll No\t\tName\t\tSub1\t\tSub2\t\tSub3\t\tTotal\t\tPercentage")
        for i, j in self.dict4.items():
            print(i, "\t\t", end=" ")
            for k, m in j.items():
                print(m, "\t\t", end=" ")
            print()

    def show(self):
        print(f"Roll No\t\tName\t\tSub1\t\tSub2\t\tSub3\t\tTotal\t\tPercentage")
        for i, j in student.dict2.items():
            print(i, "\t\t", end=" ")
            for k, m in j.items():
                print(m, "\t\t", end=" ")
            print()
        student.dist(self)


stu = student()
# stu.get_info()


ans = 'Y'
print("1.Add\n2.Show\n3.Sort By Roll No.\n4.Sort By Name\n5.Sort By Percentage")

while ans == 'Y':
    ch = int(input("Enter your choice: "))
    if ch == 1:
        stu.get_info()
    elif ch == 2:
        stu.show()
    elif ch == 3:
        stu.sort_roll()
    elif ch == 4:
        stu.sort_name()
    elif ch == 5:
        stu.sort_per()
    else:
        print("Wrong choice")
    ans = input("Do you want to continue: ")
