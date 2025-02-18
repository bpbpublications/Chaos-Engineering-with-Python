# simple class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def say_hello(self):
    print("Hello, my name is", self.name, "and I am", self.age, "years old.")

person1 = Person("John", 30)
person1.say_hello()

# inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

def say_hello(self):
    print("Hello, my name is", self.name, "and I am a student with ID", self.student_id)

