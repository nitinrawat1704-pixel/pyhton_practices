student = {'name':'Nitin','age':'29','course':['science','maths','english']}
print(student['course'])
print(student['phone'])     			#gives error 
print(student.get('phone')) 			#returns none instead of showing error
print(student.get('phone','not found')) #returns customized message instead of showing error

add a value to existing dictionary

student = {'name':'Nitin','age':'29','course':['science','maths','english']}
student['phone'] ='8082242161'
print(student)

update dictionary

student = {'name':'Nitin','age':'29','course':['science','maths','english']}
student.update({'name':'jane','age':25})
print(student)

delete specific key/value dictionary

student = {'name':'Nitin','age':'29','course':['science','maths','english']}
del student['course']
print(student)
age = student.pop('age')
print(student)
print(age)

print(student.keys())     #prints all the keys of selected dictionary
print(student.values())   #prints all the values of selected dictionary
print(student.items())    #prints all the key&values in paired of selected dictionary



student = {'name':'Nitin','age':'29','course':['science','maths','english']}
for key, value in student.items():
	print(key,value)				#prints all key and its apired value in loop

