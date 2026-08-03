# List of Hotels
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



# Shopping Cart

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
