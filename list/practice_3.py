1.Create a list of 10 student names and display the first five students.

std=["nitin","james","nathan","rahul","chloe","julie","hamza","Harley","Shalini","Ekta"]
print(std[0:4])
for i in range(0,5,1):
   print(std[i])

2.Create a list of student marks and count how many students scored above 80.
m=[100,80,55,32,65,12,95,65]  
c=0
for i in m:
   if i>80:c=c+1
   else:continue
print(c)  

3.Create a list of marks and count how many students scored between 40 and 60.
m=[100,80,55,32,65,12,95,65]  
c=0
for i in m:
   if i>=40 and i<=60 :c=c+1
   else:continue
print(c)  

4.Given a list of marks, find the second-highest mark.

m=[100,80,55,32,65,12,95,65,100]  #method1
m.sort()
print(m[-2])

print(m)                           #method2 (effective considering highest value is repeated)
c=set(m)
print(c)
nl=list(c)
nl.sort()
print(nl)
print(nl[-2],"2nd highest no")

5.Given a list of numbers, count how many numbers are even and odd.
m=[100,80,55,32,65,12,95,65,100]  
e=0
o=0
for i in m:
  if i%2==0:
    e=e+1
  else:o=o+1  
print(e," no of even")
print(o," no of odd")    

6.Given a list of numbers, create a new list containing numbers greater than 50.
m=[100,80,55,32,65,12,95,65,100] 
n=[]
for i in m:
  if i>50:
    n=n+[i]
  else:continue
print(n)    

7.Given a list of numbers, create a new list containing only even numbers.
m=[100,80,55,32,65,12,95,65,100] 
n=[]
for i in m:
  if i%2==0:
    n=n+[i]
  else:continue
print(n)


8.Given a list of student marks, create two lists:
pass_students
fail_students
m=[100,80,55,32,65,12,95,65,100] 
p=[]
f=[]
for i in m:
  if i>40:
    p=p+[i]
  else:f=f+[i]  
print(p)
print(f) 
