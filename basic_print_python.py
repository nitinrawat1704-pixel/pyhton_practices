Write a Python program to print "Hello, Python!".
Store your name, age, and city in variables and display them.
Take two numbers from the user and display their sum.
Take two numbers and display their addition, subtraction, multiplication, and division.
Write a program to calculate the area of a rectangle.
Write a program to calculate the area of a circle.
Write a program to convert Celsius into Fahrenheit.
Take a student's name and marks and display the details.
Write a program to calculate Simple Interest using Principal, Rate, and Time.
Write a program to swap the values of two variables.

1
print("Hello World") 

2
a=int(input("enter your age:"))
p=input("enter your city")
print("your age is",a,"and your city is",p)

3
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("sum of two numbers is",a+b)

4
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("sum of two numbers is",a+b)
print("sub of two numbers is",a-b)
print("mul of two numbers is",a*b)
print("div of two numbers is",a/b)

5
l=int(input("enter length:"))
w=int(input("enter width:"))
print("area5 of rect is",l*w)

6
a=int(input("enter radius:"))
print("area of circle is",3.14*(a*a))

7
c=int(input("enter celcius:"))
print("Fahrenheit is",(c*1.8)+32)

8
p=input("enter std name")
p=input("enter your city")
print("for",p,"marks is",a)

9
p=int(input("enter principle:"))
r=int(input("enter rate:"))
t=int(input("enter time:"))
print((p*r*t/100), "is your simple intrest")

10
x=int(input("enter varialble for x"))
y=int(input("enter varialble for y"))
print(f"before swap :x={x} , y={y}")
x,y=y,x
print(f"before swap :x={x} , y={y}")
