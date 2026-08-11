1.Write a Python program to print "Hello, Python!".
2.Store your name, age, and city in variables and display them.
3.Take two numbers from the user and display their sum.
4.Take two numbers and display their addition, subtraction, multiplication, and division.
5.Write a program to calculate the area of a rectangle.
6.Write a program to calculate the area of a circle.
7.Write a program to convert Celsius into Fahrenheit.
8.Take a student's name and marks and display the details.
9.Write a program to calculate Simple Interest using Principal, Rate, and Time.
10.Write a program to swap the values of two variables.
-----------------Menu-Driven Questions----------------------------

1.Create a menu-driven program for a student:
  1 → Display Student Name
  2 → Display Student Marks
  3 → Display Student Grade
2.Create a menu-driven program for a basic banking system:
  1 → Check Balance
  2 → Deposit
  3 → Withdraw
3.Create a menu-driven program to calculate:
  1 → Area of Rectangle
  2 → Area of Circle
  3 → Area of Square
4.Create a menu-driven program to convert:
  1 → Celsius to Fahrenheit
  2 → Fahrenheit to Celsius




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


1
  n=input("enter name ")
  a=int(input("enter student marks"))


  ch=int(input("1.name\n2.marks\n3.grade"))
  if ch==1:print(n)
  elif ch==2:print(a)
  elif ch==3:
    if a>80:print("A grade")
    elif a>60 and a<80:print("B grade")
    elif a>=80:print("A grade")
    elif a>=60 and a<80:print("B grade")
    elif a>=40 and a<60:print("C grade")
    else:print("fail")
else:print("invalid choice")

2
  print("welcome to bank")
  balance =3000
  ch=int(input("1.balance\n2.deposit\n3.withdrawal"))
  if ch==1:print("your balance is:",balance)
  elif ch==2:
    d=int(input("enter amount"))
    balance=balance+d
    print("you have deposited",d)
    print("your new balance is:",balance)
  elif ch==3:
    w=int(input("enter the withdrawal amount"))
    balance=balance-w
    print("you have withdrawn",w)
    print("your new balance is:",balance)
else:print("invalid entry")

3
  ch=int(input("1.are of rectangle\n2.area of circle\n3.area of square"))
  if ch==1:
    l=int(input("enter length:"))
    w=int(input("enter width:"))  
    print("area of rect is",l*w)
  elif ch==2:
    a=int(input("enter radius:"))
    print("area of circle is",3.14*(a*a))
  elif ch==3:
    l=int(input("enter length:"))
    print("area of square is",l*l)
  else:print("invalid output")   


4
  ch=int(input("1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius"))
  if ch==1:
    c=int(input("enter celcius:"))
    print("Fahrenheit is",(c*1.8)+32)
  elif ch==2:
    f=int(input("enter Fahrenheit:"))
    print("Celcius is",(f-32)/1.8)
  else:print("wrong input") 
