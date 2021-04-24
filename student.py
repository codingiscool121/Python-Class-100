class Student(object):
    def __init__(self, grade, tri1,tri2,tri3):
        self.grade  = grade
        self.tri1 = tri1
        self.tri2 = tri2
        self.tri3 = tri3
    def gettotal(self):
        total = self.tri1+self.tri2+self.tri3
        grade = self.grade
        return total, grade
soham = Student("A+", 100, 200, 300)
print(soham.gettotal())
