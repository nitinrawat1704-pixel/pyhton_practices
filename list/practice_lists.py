# List of Hotels  $$Basic list function$$
hotels = ["Taj", "Oberoi", "Radisson", "Hyatt", "Marriott"]

# 1. Display the complete list of hotels.
  for i in hotels:print(i)

# 2. Add "ITC" at the end of the list.
  hotels.append('ITC')
  for i in hotels: print(i)

# 3. Insert "Le Meridien" at index 2.
  hotels.insert(2,"Le Meridien")
 for i in hotels: print(i)
   
# 4. Remove "Hyatt" from the list.
  hotels.remove('Hyatt')
  for i in hotels: print(i)

# 5. Remove the last hotel and display it.
  hotels.pop()
  for i in hotels: print(i)

# 6. Find the index of "Radisson". 
  print(hotels.index("Radisson"))

# 7. Add another "Taj" and count how many times it appears.
  print(hotels.count('Taj'))
# 
8. Sort the hotels alphabetically.
  hotels.sort()
  print(hotels)
  
# 9. Reverse the hotel list.
  hotels.sort(reverse = True)
  print(hotels)
  
# 10. Copy the list into another variable and display both lists.
  old=hotels
  print(old)

#11 show value of hotel with it index.
for index,i in enumerate(hotels)
  print(index,i)


# Shopping Cart $$list with adding,removing and fetching index values $$

cart = ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse"]

 -------------------------------------------------------

# 1. Display all products.
print(cart)
# 2. Find the total number of products in the cart.
print(len(cart))
# 3. Check whether "Keyboard" exists in the cart.
if "Keyboard" in cart:print("found")
else:print("not found")
# 4. Remove the first occurrence of "Mouse".
cart.remove("Monitor")
print(cart)
# 5. Add "Headphones" and "Webcam".
cart.extend(["Headphones","Webcam"])
print(cart)
# 6. Display the first and last products.
print(cart[0],cart[-1])
# 7. Count how many times "Mouse" appears.
print(cart.count('Mouse'))
# 8. Sort the products alphabetically.
cart.sort()
print(cart)
# 9. Create a backup copy of the cart.
back_up=cart
print(back_up)
# 10. Empty the cart.
cart.clear()
print(cart)


#fruit cart $$List using loop$$
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
----------------------------------------------------------------
 

# 1. Display all fruits using a loop.
for i in fruits:print(i)
# 2. Print only the fruit "Mango".
for i in fruits:
  if i =='Mango':print(i)
  else:
      continue
# 3. Print all fruits except "Banana".
for i in fruits:
  if i=="Banana":
    continue
  else:print(i) 

# 4. Print fruits whose name length is greater than 5.
for i in fruits:
  if len(i)>5:print(i)
  else:
      continue
# 5. Print "Available" if the fruit is "Apple", otherwise print "Not Apple".
if "Apple" in fruits:print("Available") 
else:print("Not Available") 



------------------------------------------
$$List using loop$$
marks = [45, 78, 32, 90, 65]

------------------------------------ 

# 1. Display all marks.
print(marks)
# 2. Print only passing marks (>=35).
for i in marks:
  if i>=35:print(i)
  else:continue 
# 3. Print only failing marks (<35).
for i in marks:
  if i<35:print(i)
  else:continue 
# 4. Print "Excellent" if marks are greater than 80.
for i in marks:
  if i>80:print("Excellent")
  else:continue   
# 5. Count how many students passed
count=0
for i in marks:
  if i>=35:
    count+=1
  else:continue 
print(count,"student has passed")


-------------------------------------------------------------------
$$slicing$$
cities = ("Delhi", "Mumbai", "Chennai", "Jaipur", "Pune")

------------------------------------------------------------------- 

# 1. Display all cities.
print(cities)
# 2. Display the first city.
print(cities[0])
# 3. Display the last city.
print(cities[-1])
# 4. Display cities from index 1 to 3.
print(cities[0:3])
# 5. Check whether "Delhi" is present.
if "Delhi" in cities:print('found')
else:print('not found')
# 6. Find the index of "Jaipur".
print(cities.index('Jaipur'))
# 7. Display the total number of cities.
print(len(cities))
# 8. Display each city using a loop.
for i in cities:print(i)
# 9. Print only cities having more than 5 letters.
for i in cities:
  if len(i)>5:print(i)
  else:continue
# 10. Print "Metro City" if the city is Delhi or Mumbai.
for i in cities:
  if i =='Delhi' or i=='Mumbai':print("metro city")
  else:print("non metro city")

---------------------------------------
$$Arithmetic function with list$$
marks = (78, 45, 89, 92, 67, 45)

-------------------------

# 1. Display all marks.
print(marks)
# 2. Display the highest mark.
print(max(marks))
# 3. Display the lowest mark.
print(min(marks))
# 4. Count how many times 45 appears.
print(marks.count(45))
# 5. Find the index of 92.
print(marks.index(92))
# 6. Display only passing marks (>=35).
for i in marks:
  if i>=35:print(i)
  else:continue 
# 7. Count students scoring above 75.
c=0
for i in marks:
  if i >75:
    c+=1 
  else:continue 
print(c,"people has marks more than 75") 
# 8. Display marks greater than 80.
for i in marks:
  if i>80:print(i)
  else:continue
# 9. Display the total number of marks.
print(sum(marks))
# 10. Display all marks using a loop.
for i in marks:print(i)
