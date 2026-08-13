1.Create a function that accepts a student dictionary and displays the student's name and marks.
2.Create a function that accepts a dictionary of student marks and returns the highest marks.
3.Create a function that accepts a dictionary of students and marks and returns the number of passed students.
4.Create a function that accepts a product-price dictionary and returns the total price of all products.



1
def display(d):
  for k,v in d.items():
   print(k,v)

2.
def d_hm(d):
  c=max(d.values())
  for k,v in d.items():
    if v==c:
      print(k,v)

3.
def nsp(d):
  c=0
  for k,v in d.items():
    if v>=40:
     c=c+1
    else:continue
  print(c,"no of student passed") 

4.
def sp(d):
  print(sum(d.values())) 


students = {"Nitin": 85, "Rahul": 72, "Shalini": 91, "Ekta": 64, "Sanjay": 78}
display(students)
d_hm(students)
nsp(students)
grocery_cart = {"Apple": 1.50,"Milk": 2.99,"Bread": 2.49,"Eggs": 3.99} 
sp(grocery_cart)
