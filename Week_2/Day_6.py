#defining the function
def my_fun():
    print('hello.txt')
    
#calling the function
my_fun()

#with parameter
def new_func(fname):
    print(f'{fname}hello.txt')
    
new_func('Abhishek')
new_func('Ankit')

#sum of two number by passing parameters
def sum(num1,num2):
    print(num1 + num2)
sum(1,2)

#default
def my_func(country = 'India'):
    print(f'I am from {country}')

my_func()
my_func('Canada')
my_func('USA')

#return value
def my_func(x):
    return 5*x
print(my_func(5))
print(my_func(3))

#sum of two number by passing parameters find result using return
def sum(num1,num2):
    return num1 + num2
print(sum(5,5))
print(sum(5,9))

def func1(a):
    a[0] = 'new value'
    a[1] = a[1] + 1
args = ['old value', 99]
func1(args)
print(args[0],args[1])

#lambda
print('Lambda Function : ')

#anonymous function
myfunc = lambda i: i * 2
print(myfunc(2))

#more than one defined input
myfunc = lambda x , y : x * y
print(myfunc(3,6))

#At run_time
def func(n):
    return lambda i : i * n
doubler = func(2)
tripler = func(3)
val = 11
print(f"Doubled : {str(doubler(val))}, Tripler : {str(tripler(val))}")
#print(doubler(val))


#Arrays
print("Python Arrays")

#date and time
print('Date and TIme : ')

#impoerting date and time module

# creating Date Objects
# we can use the datetime() class constructor() of the datetime module.
# The datetime() class required three parameter to create date: year, month, day
import datetime

x = datetime.datetime.now()
print(x)

#strftime() method
import datetime
x = datetime.datetime(2022, 6, 18)
print(x.strftime("%B"))

# Python Modules
print("Python Modules : ")

# Create Module
def greeting(name):
    print(f"Hello, {name}")
    person1 = {"name" : "urvashi", 
               "age" : 26, 
               "country" : "India"}    

import my_module
my_module.greeting('Abhishek')


# new example, Variable in Module
import my_module
a = my_module.person1["age"]
print(a)
