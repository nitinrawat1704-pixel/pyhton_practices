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
# 8. Sort the hotels alphabetically.
# 9. Reverse the hotel list.
# 10. Copy the list into another variable and display both lists.

