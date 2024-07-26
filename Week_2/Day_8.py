# Error and exception handling

# The try block will generate an exception because x is not defined
try:
    print(x)
except:
    print("An exception occured")

# Print one message if the try block raises a NameError and another for other errors
try:
    print(x)
except NameError:
    print("Variable x is not defined")
# The try block does not generate any error
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
#else part run only the except is not run if except is excuted the else part will not
#if we use final it excecute on both the condition if the except block is executed or not

#The finally block, if specified, will be excuted regardless if the try block raised an error or not
try:
    print(x)
except:
    print("Variable x is not defined")
finally:
    print("the 'try except' is finished")

#take input from the user of two number the divident is 0 and try to handle the divide by zero error    
num1 = int(input("ENter the num1 : "))
num2 = 0

try:
    print(num1 / num2)
except:
    print("Num2 in div is zero")

def this_fail():
    x = 12 / 0
try:
    this_fail()
except ZeroDivisionError as err:
    print('Handling run-time error : ', err)

# type error
a = input("Enter value : ")
b = "ABhishek"

try:
    print(a+b)
except TypeError:
    print("Type Error")
#  Index error
# using list
l = [2,3,4,5,6,67]
try:
    print(l[8])
except IndexError:
    print("Index Error")
# using string
st = "Abhishek"
try:
    print(st[10])
except IndexError:
    print("Index Error")
# Question 1
#
try:
    file = open("file.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File Not Found Error")
    