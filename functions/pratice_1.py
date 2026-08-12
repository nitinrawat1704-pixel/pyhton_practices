Q1. Create a function that prints "Hello Python".

Q2. Create a function that accepts a name and prints a welcome message.

Q3. Create a function that accepts two numbers and returns their sum.

Q4. Create a function to calculate the square of a number.

Q5. Create a function to check whether a number is even or odd.

Q6. Create a function to find the greater of two numbers.

Q7. Create a function to calculate the area of a rectangle.

Q8. Create a function to calculate the factorial of a number.

Q9. Create a function that accepts marks and returns Pass or Fail.

Q10. Create a function that accepts marks and returns the student's grade.


1
def p():print("Hello Pyhton")

2
def pn():
  n=input("enter your name")
  print("welcome",p)

3
def add():
  a=int(input("enter first number:"))
  b=int(input("enter second number:"))
  print("sum of two numbers is",a+b)  

4
def square():
  s=int(input("enter  no "))
  print("square of input is: ",s*s)

5
def find_e_o():
  c=int(input("enter a no"))
  if c%2==0:print("even")
  else:print("odd")  

6
def find_greater():
  a=int(input("enter no"))
  b=int(input("enter no"))
  if a>b:print(f"{a} is greater {b}")
  else:print(a,"is greater than ",b)

7
def area_of_rect():
  l=int(input("enter length:"))
  w=int(input("enter width:"))  
  print("area of rect is",l*w)  

8
def factorial():
   a=int(input("enter to find factorial:"))
   c=1
   for i in range(1,a+1,1):
    c=i*c

   print(c," is the factorial") 

9
def pass_or_fail():
  a=int(input("enter sum of marks"))
  if a <=40:print("fail")
  else:print("pass")

10
def check_grade():
  a=int(input("enter marks"))
  if a>80:print("A grade")
  elif a>60:print("B grade")
  elif a>=40:print("C grade")
  else:print("fail")
