# Create a dictionary containing 5 students and their marks. Find the student with the highest marks.

s={"nitin":80,"rahul":90,"shalini":100,"remi":30,"aura":20,}
c=max(s.values())
for n,m in s.items():
  if m==c:print(n)
  else:continue


# Create a dictionary containing student names and marks. Count how many students failed

s={"nitin":80,"rahul":90,"shalini":100,"remi":30,"aura":20,}
c=0
f=0
for i in s.values():
  if i>40:
    c=c+1
  else:f=f+1  
print(c)  
print(f)

# Create a dictionary containing 5 products and their prices. Find the most expensive product.

l={"tea":200,"coffee":300,"coke":220,"matcha":400,"yebra mate":330}
c=max(l.values())
for i,p in l.items():
  if p==c:print(i)
  else:continue


#Create a dictionary containing employee names and salaries. Find the highest salary.

s={"nitin":8000,"rahul":9000,"shalini":1000,"remi":3000,"aura":20000,}
print(max(s.values())).


#Create a dictionary of products and prices. Calculate the total value of all products.

l={"tea":200,"coffee":300,"coke":220,"matcha":400,"yebra mate":330}
print(sum(l.values()))


#Create a dictionary containing city names and temperatures. Find the city with the highest temperature.

weather_data = {
    "Mumbai": 32.5,
    "Delhi": 38.2,
    "Bengaluru": 28.0,
    "Chennai": 35.4,
    "Kolkata": 33.1
}

m=max(weather_data.values())
for i,p in weather_data.items():
  if p==m:print(i)
  else:continue
