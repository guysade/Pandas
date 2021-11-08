class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name + ' was created ')
    def age(Student):
        return Student.age
    _var = 'first'
    __var2 = 'second'
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


x = Student('guy',21)
print(Student.age(x))
x.age = 20
print(Student.age(x))
print(dir(x))
print(x._var)
