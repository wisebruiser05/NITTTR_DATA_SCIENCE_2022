# Question 1
"""
Create a Circle class and intialize it with radius. 
Make two methods getArea and getCircumference inside this class.
"""
# Method one
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius * self.radius

    def getCircum(self):
        return 2 * 3.14 * self.radius


c1 = Circle(6)
print(c1.getArea())
print(c1.getCircum())

# Method Two


class Circle:
    def __init__(self, radius):
        self.radius = radius


class childCircle(Circle):
    def getArea(self):
        return 3.14 * self.radius * self.radius

    def getCircum(self):
        return 2 * 3.14 * self.radius


c2 = childCircle(6)
print(c2.getArea())
print(c2.getCircum())


# Question 2
"""
Create a Temperature class. Make two methods :
convertFahrenheit - It will take celsius and will print it into Fahrenheit.
convertCelsius - It will take Fahrenheit and will convert it into Celsius.
"""
class Temprature:
    def convertFahrenheit(self, celcius):
        return (celcius * (9 / 5)) + 32

    def convertCelcius(self, fahrenheit):
        return (fahrenheit - 32) * (5 / 9)


t1 = Temprature()
print(t1.convertFahrenheit(121))
print(t1.convertCelcius(89))


# Question 3
"""
Create a Student class and initialize it with name and roll number. Make methods to :
Display - It should display all informations of the student.
setAge - It should assign age to student
setMarks - It should assign marks to the student.
"""
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks

    def Display(self):
        """
        print("Name of Student : " , self.name , "\nRoll no of Student : " , self.rollno ,
              "\nAge of Student : " , self.age , "\nMarks of Student : " , self.marks)
        print(f"Name : {self.name} \nRoll No : {self.rollno} 
              \nAge : {self.age} \nMarks : {self.marks}")
        """
        print("Name : {0} \nRoll No : {1} \nAge : {2} \nMarks : {3}".format(
            self.name, self.rollno, self.age, self.marks))


s1 = Student("Abhishek", 74)
s1.setAge(20)
s1.setMarks(80)
s1.Display()


# Question 4
"""
Create a Time class and initialize it with hours and minutes.
Make a method addTime which should take two time object and add them. 
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Make a method displayTime which should print the time.
Make a method DisplayMinute which should display the total minutes in the Time. 
E.g.- (1 hr 2 min) should display 62 minute.

"""
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, t2):
        t3 = Time(0, 0)
        t_min = self.minutes + t2.minutes
        if t_min > 60:
            t3.hours = t_min / 60
        t3.minutes = int(t_min - (t3.hours * 60))
        t3.hours = int(t3.hours + t2.hours + self.hours)
        return t3

    def displayTime(self):
        print("Hours : ", self.hours, "Minutes : ", self.minutes)

    def displayMinutes(self):
        print("Minutes : ", ((self.hours * 60) + self.minutes))


a = Time(2, 50)
b = Time(1, 20)
c = Time.addTime(a, b)
c.displayTime()
c.displayMinutes()
