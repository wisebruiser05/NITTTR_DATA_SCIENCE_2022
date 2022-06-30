# Question 1
digit = {'0' : 'Zero',
        '1' : 'One',
        '2' : 'Two',
        '3' : 'Three',
        '4' : 'Four',
        '5' : 'Five',
        '6' : 'Six',
        '7' : 'Seven',
        '8' : 'Eight',
        '9' : 'Nine'}

num = str(input("Enter the number : "))
for i in num:
    x = digit[i]
    print(x,end = " ")
print('/n')


# Question 2
def temperature(celcius):
    fahrenheit = ( 9 / 5 ) * celcius + 32
    print("Converted temperature from celcius into fahrenheit : ", fahrenheit)
temp = int(input("Temperature in Celceius : "))
temperature(temp)


# Question 3
import datetime as dt
val=input("Enter the date in form mm/dd/yyyy : ")
time = dt.datetime.strptime(val, "%m/%d/%Y").date()
result = dt.datetime.strftime(time, "%B/%d/%Y")
print(result)