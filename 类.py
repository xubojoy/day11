#Author:xubojoy

class Person(object):
    def __init__(self,name):
        self.name = name
    def get_details(self):
        return self.name


class Student(Person):
    def __init__(self, name, branch, year):
        super(Student, self).__init__(name)
        self.branch = branch
        self.year = year

    def get_details(self):
        return '{} studies {} and is in {} year.'.format(self.name, self.branch, self.year)

class Teacher(Person):
    def __init__(self, name, papers):
        super(Teacher, self).__init__(name)
        self.papers = papers

    def get_details(self):
        return '{} teaches {}'.format(self.name, ','.join(self.papers))



person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())