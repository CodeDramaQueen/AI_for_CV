class SchoolMember:
    '''代表学校里的任何成员'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(initialize school_member: {})'.format(self.name))

    def tell(self):
        '''告诉我有关的细节'''
        print('name: "{}" age: "{}"'.format(self.name, self.age), end=' ')

class Teacher(SchoolMember):
    '''代表一位老师'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(initialize teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''代表一位学生'''
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score
        print('(initialize student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('score: "{:d}"'.format(self.score))

t = Teacher('miss huang', 23, 30000)
s = Student('liyu', 24, 100)

print()#打印空白行
members = [t, s]
for member in members:
    #对全体师生
    member.tell()