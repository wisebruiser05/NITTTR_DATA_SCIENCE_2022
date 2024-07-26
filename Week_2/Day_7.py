class Myclass:
    x = 5


print(Myclass)

# creating Object
p1 = Myclass()
print(p1.x)

"""
__init__() function is called automatically every time
the class is being used to create a new object
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Abhishek", 21)

print(p1.name)
print(p1.age)

# modify object properties
p1.name = "Baba"
p1.age = 25
print(p1.name)
print(p1.age)

# Delete Object property
del p1.age
# print(p1.age)


"""
Insert a function that print a greeting and execute it on thee p1 object
"""


class Person1:
    def __init__(self, name1, age1):
        self.name1 = name1
        self.age1 = age1

    def myfunc(self):
        print(f"Hello my name is {self.name1}")


p2 = Person1("Abhishek", 23)
p2.myfunc()
"""
self represents the instance of the class by using the "self" keyword we can access
the attributes and method of the class in python.
"""


"""
Self is a convention and not a real python keyword
self is parameter in function and user can use another parameter name in place of it.
But it is advisable to use self because it increases the readability of code
"""


class this_is_car:
    def show(self):
        print("We have used another parameter in place of self")
        """
        print("We have used another" 
              "parameter in place of self")
        """


p3 = this_is_car()
p3.show()


"""
Question 1
Create a Circle class and intialized it with radius. Make two methods getArea and
getCircumference inside the class
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = 3.14 * self.radius * self.radius
        print("Area", area)

    def getCircum(self):
        circum = 2 * 3.14 * self.radius
        print("Circumference : ", circum)


r = Circle(12)
r.getArea()
r.getCircum()

"""
Question 1 using inheritance or child class
Create a Circle class and intialized it with radius. Make two methods getArea and
getCircumference inside the class
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def print_Radius(self):
        print("Radius is ", self.radius)


class childCircle(Circle):
    def getArea(self):
        return 3.14 * self.radius * self.radius

    def getCircum(self):
        return 2 * 3.14 * self.radius


x3 = childCircle(12)
print(x3.getArea())
print(x3.getCircum())

"""
Inheritance
"""
# Inheritance
"""
Without passing the properties in child class
"""


class Person2:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person2):
    pass


"""
Use the pass keyword when you do not wanr to add any other properties or method to the class
"""

x1 = Student("Abhishek", "Yadav")
x1.printname()


"""
passing attributes and adding method to the child class
"""


class Person3:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person3):
    def __init__(self, firstname, lastname, year):
        Person3.__init__(self, firstname, lastname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome : ", self.firstname, self.lastname)


x2 = Student("Abhishek", "Yadav", 2023)
x2.welcome()
print(x2.graduation_year)


"""
Same name but doing different tasks.
It means that one of the mehtods overrides the other
"""


class Rectangle:
    def __init__(self, length, bredth):
        self.length = length
        self.bredth = bredth

    def getArea(self):
        print(self.length * self.bredth, ", is area of Rectangle.")


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)

    def getArea(self):
        print(self.side * self.side, ", is area of Square")


s = Square(4)
r = Rectangle(2, 4)
s.getArea()
r.getArea()
