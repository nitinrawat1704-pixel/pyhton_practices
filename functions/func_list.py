1. Create a function that accepts a list and returns its length.

2. Create a function that accepts a list and returns the sum of all elements.

3. Create a function that accepts a list and returns the maximum value.

4. Create a function that accepts a list of marks and returns the number of passed students.
   Assume marks >= 40 means passed.

5. Create a function that accepts a list of marks and returns the number of failed students.
   Assume marks < 40 means failed.

6. Create a function that accepts a list and returns a new list containing only even numbers.

     
1     
def l(a):
  print(len(a))
marks=[10,20,3,5,6]
l(marks)


2
def sl(a):
  print(sum(a))
marks=[10,20,3,5,6]
sl(marks)


3
def mv(a):
  print(max(a))
marks=[10,20,3,5,6]
mv(marks)


4
def sp(a):
  c=0
  for i in a:
    if i>=40:
      c=c+1
    else:continue  
  print(c," passed")    

l=[10,50,65,88,35]
sp(l)  


5
def sf(a):
  c=0
  for i in a:
    if i<40:
      c=c+1
    else:continue  
  print(c,"failed")    


6
l=[10,50,65,88,35]
sf(l) 


def el(a):
  nl=[]
  for i in a:
    if i%2==0:
      nl=nl+[i]
    else:continue
  print("even list is: ",nl)    

l=[10,50,65,88,35]
el(l)
