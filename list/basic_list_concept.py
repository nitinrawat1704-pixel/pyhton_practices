list[]

ADD value to list

course=['history','math','science','physics']
course.append('arts')   #[append] will add the value at the last inddex location
print(course)


course=['history','math','science','physics']
course2=['arts','english']
course.insert(0,'arts')   #[insert] will add the value at the desired location but if multiple values are added it will treat them a single list
course.insert(0,course2)
print(course[0])			#[insert] will treat multiple added values in one index(mentioned location) and [extend] function solves that problem


course=['history','math','science','physics']
course2=['arts','english']
course.extend(course2) 		#use when you have multiple values to add to the list
print(course[4])


remove value from list

course=['history','math','science','physics']
course2=['arts','english']
course.extend(course2) 
course.remove('math')  #removes the value
course.pop()          #removes the last value 
print(course)

sorting list

course=['history','science','math','physics']
course.reverse()    		#it [reverses]
course.sort()		 	 	#will [sort] in alpabetical order 
course.sort(reverse = True) #sort in reverse manner 
print(course)

num=[1,2,3,4,5]
print(min(num))
print(max(num))
print(sum(num))


course=['history','science','math','physics']
print(course.index('math'))    # used to find the index of value
print('art' in course)		 # used to check if it exits or not (usefulful for conditions like if or else)



looping

course=['history','science','math','physics']
for i in course:        
	print(i)



course=['history','science','math','physics']
for index,a in enumerate(course):            #[enumerate] helps with giving you value in set with its index(location)
  print(index,a)


course=['history','science','math','physics']
course_str = ' - '.join(course)    
new_str =course_str.split(' - ')
print(course_str)
print(new_str)


