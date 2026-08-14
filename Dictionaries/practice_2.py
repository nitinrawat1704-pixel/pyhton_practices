1. Print the student's name.
2. Print the student's marks.
3. Add a new key called "course".
4. Update the student's marks to 85.
5. Add an "email" key.
6. Remove the "age" key.
7. Print all keys using keys().
8. Print all values using values().
9.Write a Python program to find and print all employees whose salary is greater than ₹85,000.


1. print(student["name"])
2. print(student["marks"])
3. student["course"] = "Sql"
   print(student)
4. student.update({"marks": 85})
   print(student)
5. student["email"]=student["name"]+"@gmail.com"
   print(student)
6.student.pop("age")
  print(student) 
7. for i in student.keys(): print(i)
8. for i in student.values(): print(i)
9.employees = {
    101: {"name": "Nitin", "department": "IT", "salary": 90000},
    102: {"name": "Ankit", "department": "Sales", "salary": 85000},
    103: {"name": "Priya", "department": "Finance", "salary": 95000},
    104: {"name": "Rahul", "department": "IT", "salary": 75000},
    105: {"name": "Sneha", "department": "Finance", "salary": 88000}
}

for k,v in employees.items():
    if v["salary"]>85000:print(v["name"],v["department"])
    else:continue
