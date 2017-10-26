class Student:
    def __init__(self, name, stu_id):
        self.name = name
        self.stu_id = stu_id

    def find_name(self):
        return self.name

    def __lt__(self, other):
        return self.stu_id < other.stu_id

    def __str__(self):
        return "<"+self.name+", "+str(self.stu_id)+">"

    def __repr__(self):
        return str(self)

class Student_15(Student):
    def __lt__(self, other):
        return self.stu_id > other.stu_id


stu1 = Student("Tom", 100)
stu2 = Student("Peter", 101)
stu3 = Student("Bob", 105)
stu4 = Student("Amy", 109)
list_stu = [stu3, stu2, stu4, stu1]
print(list_stu)
list_stu.sort()
print(list_stu)

bstu1 = Student_15("Tom", 200)
bstu2 = Student_15("Peter", 201)
bstu3 = Student_15("Bob", 205)
bstu4 = Student_15("Amy", 209)
list_bstu = [bstu3, bstu2, bstu4, bstu1]
print(list_bstu)
list_bstu.sort()
print(list_bstu)