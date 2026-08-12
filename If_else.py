1.Check whether a number is positive or negative.
2.Check whether a number is even or odd.
3.Check whether a person is eligible to vote.
4.Find the greater of two numbers.
5.Check whether a student has passed or failed. Passing marks are 40.
6.Check whether a number is divisible by 5.
7.Check whether a person is eligible for a driving license.
8.Display a grade based on the student's marks:
  80–100 → A
  60–79 → B
  40–59 → C
  Below 40 → Fail
9.Check whether a given year is a leap year.
10.Create a simple calculator using +, -, *, and /.

1
c=int(input("enter a no"))
if c<0:print("negative")
else:print("positive")

2
c=int(input("enter a no"))
if c%2==0:print("even")
else:print("odd")
  
3
a=int(input("enter age"))
if a>=18:print("eligible")
else:print("not eligible")
  
4
a=int(input("enter no"))
b=int(input("enter no"))
if a>b:print(f"{a} is greater {b}")
else:print(a,"is greater than ",b)
  
5
a=int(input("enter marks"))
if a>40:print("pass")
else:print("fail")

6
c=int(input("enter a no"))
if c%5==0:print("divisible")
else:print("not divisible")

7
a=int(input("enter age"))
if a>=21:print("eligible")
else:print("not eligible")

8
a=int(input("enter marks"))
if a>80:print("A grade")
elif a>60:print("B grade")
elif a>=40:print("C grade")
else:print("fail")


9
a=int(input("enter year"))
if (a%4==0 and a%100!=0) or (a%400==0):print("leap year")
else:print("not leap year")

10
a=int(input("enter 1st no "))
b=int(input("enter 2nd no"))
ch=int(input("1.add\n2.sub\n3.mul\n4.div"))
if ch==1:print(a+b)
elif ch==2:print(a-b)
elif ch==3:print(a*b)
elif ch==4:print(a/b)
