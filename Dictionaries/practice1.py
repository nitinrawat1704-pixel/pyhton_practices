#Add a new key
employee = {
    "name": "Nitin",
    "age": 30,
    "department": "IT",
    "salary": 90000
}
employee["city"] = "mumbai"
print(employee)

#Update a value
employee = {
    "name": "Nitin",
    "age": 30,
    "department": "IT",
    "salary": 90000
}
employee.update({"salary":85000})
for k,v in employee.items():print(k,v)

#Check whether a key exists
employee = {
    "name": "Nitin",
    "age": 30,
    "department": "IT",
    "salary": 90000
}
a=input("enter key to check")
if a in employee.keys():print("found")
else:print("not found")

#Q5. Count frequency of elements
numbers = [10, 20, 10, 30, 20, 10, 40, 30, 20]
d={}
for i in numbers:
  d[i]=(numbers.count(i))
  
print(d)

#Find the highest salary
employees = {
    "Nitin": 90000,
    "Ankit": 85000,
    "Amit": 65000,
    "Priya": 95000,
    "Rahul": 72000
}
a=int(max(employees.values()))
for name,sal in employees.items():
  if a==sal:
   print(name)
   
  else: continue 


#Find employees earning above average salary
employees = {
    "Nitin": 90000,
    "Ankit": 85000,
    "Amit": 65000,
    "Priya": 95000,
    "Rahul": 72000
}
a=int(sum(employees.values())/(len(employees.values())))
print("average is :",a)
print("employee with sal greater than avg:")
for name,sal in employees.items():
  if sal>a:print(name,sal)
  else:continue
