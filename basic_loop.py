1.Print numbers from 1 to 10.
2.Print numbers from 10 to 1.
3.Print all even numbers from 1 to 20.
4.Print all odd numbers from 1 to 20.
5.Take two numbers from the user and print all even numbers between them.
6.Take two numbers from the user and print all odd numbers between them.
7.Take a number from the user and print its multiplication table.
8.Find the sum of numbers from 1 to 10.
9.Take two numbers and find the sum of all numbers between them.
10.Take two numbers and print all numbers divisible by 6 between them.
11.Take two numbers and print all numbers that are even and divisible by 6.
12.Take two numbers and print all numbers that are odd and divisible by 3.
13.Find the factorial of a given number.
14.Print the first 10 multiples of a given number.

1
for i in range(1,11,1):print(i)  
  
2
for i in range(10,0,-1):print(i)  
  
3
for i in range(21):
  if i%2==0:print(i)
  
4
for i in range(20): 
  if i%2!=0:print(i)  
  
5
a=int(input("starting no"))
b=int(input("ending no"))
for i in range(a,b+1,1):
  if i%2==0:print(i) 
    
6
a=int(input("starting no"))
b=int(input("ending no"))
for i in range(a,b+1,1):
  if i%2!=0:print(i)  
  
7
a=int(input("enter no to find its table"))
for i in range(1,11,1):
  print(a,"*",i,"=",a*i)  
  
8
c=0
for i in range(1,11,1):
  c=c+i
print(c)  

9
a=int(input("starting no"))
b=int(input("ending no"))
c=0
for i in range(a,b+1,1):
  c=c+i
print(c)   

  
10
a=int(input("starting no"))
b=int(input("ending no"))
for i in range(a,b+1,1):
  if i%6==0:print(i)
  
11
a=int(input("starting no"))
b=int(input("ending no"))
for i in range(a,b+1,1):
  if i%2==0 and i%6==0:
    print(i)
  
12
a=int(input("starting no"))
b=int(input("ending no"))
for i in range(a,b+1,1):
  if i%2!=0 and i%3==0:
    print(i)

13
c=1
a=int(input("enter a no"))
for i in range(1,a+1,1):
  c=c*i
print(c)  

14
a=int(input("enter a no"))
for i in range(1,11,1):
  print(a*i)
  
