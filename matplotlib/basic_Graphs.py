--------------------------line chart-------------------------------------

import matplotlib.pyplot as plt
player=["Haland","Neymar","Messi","Ronaldo"]
goals=[10,50,65,150]



plt.title("Goals per player")                   #Title display
plt.xlabel("player")                            #X axis display
plt.ylabel("goals")                             #Y axis display

plt.plot(player,goals)                          #.plot for ploting line graph
#plt.plot(player,goals,marker="*")              #upgrade 1
#plt.plot(player,goals,marker="*",color="blue") #upgrade 2
plt.show()

-----------
data = {

    "Order_ID": [1001, 1002, 1003, 1004, 1005,

                 1006, 1007, 1008, 1009, 1010,

                 1011, 1012, 1013, 1014, 1015,

                 1016, 1017, 1018, 1019, 1020],

    "Customer_Name": [

        "Rahul", "Priya", "Amit", "Sneha", "Rohit",

        "Neha", "Vikram", "Anjali", "Karan", "Pooja",

        "Arjun", "Meena", "Suresh", "Kavita", "Manish",

        "Riya", "Deepak", "Simran", "Naveen", "Asha"

    ],

    "Gender": [

        "Male", "Female", "Male", "Female", "Male",

        "Female", "Male", "Female", "Male", "Female",

        "Male", "Female", "Male", "Female", "Male",

        "Female", "Male", "Female", "Male", "Female"

    ],

    "Age": [25, 29, 34, 27, 31, 24, 42, 30, 28, 36,

            26, 33, 45, 22, 38, 28, 32, 26, 40, 35],

    "City": [

        "Delhi", "Mumbai", "Pune", "Delhi", "Jaipur",

        "Mumbai", "Pune", "Delhi", "Hyderabad", "Jaipur",

        "Delhi", "Mumbai", "Pune", "Delhi", "Hyderabad",

        "Jaipur", "Mumbai", "Pune", "Delhi", "Hyderabad"

    ],

    "Category": [

        "Electronics", "Clothing", "Electronics", "Grocery", "Clothing",

        "Electronics", "Grocery", "Electronics", "Clothing", "Grocery",

        "Electronics", "Clothing", "Electronics", "Grocery", "Clothing",

        "Electronics", "Grocery", "Clothing", "Electronics", "Grocery"

    ],

    "Product": [

        "Laptop", "Jeans", "Mobile", "Rice", "Shirt",

        "Headphones", "Oil", "Tablet", "T-Shirt", "Sugar",

        "Mouse", "Saree", "Monitor", "Tea", "Shoes",

        "Keyboard", "Biscuits", "Jacket", "Printer", "Flour"

    ],

    "Quantity": [1, 2, 1, 5, 3, 2, 4, 1, 4, 6,

                 2, 1, 1, 3, 1, 2, 10, 1, 1, 5],

    "Price": [55000, 2500, 22000, 600, 1200,

              1800, 750, 18000, 900, 500,

              700, 3500, 15000, 450, 2800,

              1200, 50, 4200, 12000, 550],

    "Discount": [10, 5, 8, 0, 10, 5, 0, 12, 5, 0,

                 5, 10, 8, 0, 15, 5, 0, 10, 12, 0],

    "Payment_Mode": [

        "UPI", "Card", "UPI", "Cash", "Card",

        "UPI", "Cash", "Card", "UPI", "Cash",

        "UPI", "Card", "UPI", "Cash", "Card",

        "UPI", "Cash", "Card", "UPI", "Cash"

    ],

    "Order_Date": [

        "2025-01-05", "2025-01-07", "2025-01-10", "2025-01-12",

        "2025-01-15", "2025-01-18", "2025-01-20", "2025-01-22",

        "2025-01-25", "2025-01-28", "2025-02-02", "2025-02-05",

        "2025-02-08", "2025-02-10", "2025-02-13", "2025-02-15",

        "2025-02-18", "2025-02-20", "2025-02-23", "2025-02-25"

    ],

    "Rating": [5, 4, 5, 4, 3, 5, 4, 5, 3, 4,

               4, 5, 4, 3, 5, 4, 4, 5, 3, 4]

}

import pandas as pd
df=pd.DataFrame(data)
df.groupby("City")["Price"].sum().plot() #using group by

df.pivot_table(values="Sales",index="City",columns="Gender",aggfunc="sum").plot() #using pivot table
------------------------------bar chart--------------------------------

import matplotlib.pyplot as plt
player=["Haland","Neymar","Messi","Ronaldo"]
goals=[10,50,65,150]

plt.title("Goals per player")
plt.xlabel("player")
plt.ylabel("goals")

plt.bar(player,goals,color="blue")         #.bar for ploting bar chart
plt.show()


-----------------
data = {

    "Order_ID": [1001, 1002, 1003, 1004, 1005,

                 1006, 1007, 1008, 1009, 1010,

                 1011, 1012, 1013, 1014, 1015,

                 1016, 1017, 1018, 1019, 1020],

    "Customer_Name": [

        "Rahul", "Priya", "Amit", "Sneha", "Rohit",

        "Neha", "Vikram", "Anjali", "Karan", "Pooja",

        "Arjun", "Meena", "Suresh", "Kavita", "Manish",

        "Riya", "Deepak", "Simran", "Naveen", "Asha"

    ],

    "Gender": [

        "Male", "Female", "Male", "Female", "Male",

        "Female", "Male", "Female", "Male", "Female",

        "Male", "Female", "Male", "Female", "Male",

        "Female", "Male", "Female", "Male", "Female"

    ],

    "Age": [25, 29, 34, 27, 31, 24, 42, 30, 28, 36,

            26, 33, 45, 22, 38, 28, 32, 26, 40, 35],

    "City": [

        "Delhi", "Mumbai", "Pune", "Delhi", "Jaipur",

        "Mumbai", "Pune", "Delhi", "Hyderabad", "Jaipur",

        "Delhi", "Mumbai", "Pune", "Delhi", "Hyderabad",

        "Jaipur", "Mumbai", "Pune", "Delhi", "Hyderabad"

    ],

    "Category": [

        "Electronics", "Clothing", "Electronics", "Grocery", "Clothing",

        "Electronics", "Grocery", "Electronics", "Clothing", "Grocery",

        "Electronics", "Clothing", "Electronics", "Grocery", "Clothing",

        "Electronics", "Grocery", "Clothing", "Electronics", "Grocery"

    ],

    "Product": [

        "Laptop", "Jeans", "Mobile", "Rice", "Shirt",

        "Headphones", "Oil", "Tablet", "T-Shirt", "Sugar",

        "Mouse", "Saree", "Monitor", "Tea", "Shoes",

        "Keyboard", "Biscuits", "Jacket", "Printer", "Flour"

    ],

    "Quantity": [1, 2, 1, 5, 3, 2, 4, 1, 4, 6,

                 2, 1, 1, 3, 1, 2, 10, 1, 1, 5],

    "Price": [55000, 2500, 22000, 600, 1200,

              1800, 750, 18000, 900, 500,

              700, 3500, 15000, 450, 2800,

              1200, 50, 4200, 12000, 550],

    "Discount": [10, 5, 8, 0, 10, 5, 0, 12, 5, 0,

                 5, 10, 8, 0, 15, 5, 0, 10, 12, 0],

    "Payment_Mode": [

        "UPI", "Card", "UPI", "Cash", "Card",

        "UPI", "Cash", "Card", "UPI", "Cash",

        "UPI", "Card", "UPI", "Cash", "Card",

        "UPI", "Cash", "Card", "UPI", "Cash"

    ],

    "Order_Date": [

        "2025-01-05", "2025-01-07", "2025-01-10", "2025-01-12",

        "2025-01-15", "2025-01-18", "2025-01-20", "2025-01-22",

        "2025-01-25", "2025-01-28", "2025-02-02", "2025-02-05",

        "2025-02-08", "2025-02-10", "2025-02-13", "2025-02-15",

        "2025-02-18", "2025-02-20", "2025-02-23", "2025-02-25"

    ],

    "Rating": [5, 4, 5, 4, 3, 5, 4, 5, 3, 4,

               4, 5, 4, 3, 5, 4, 4, 5, 3, 4]

}

import pandas as pd
df=pd.DataFrame(data)
df.groupby(["City","Gender"])["Price"].sum().plot(kind="bar")  #groupby

df.groupby("City").agg(
    sum_s=("Price","sum"),
    count_gender=("Gender","count")                   
).plot(kind="bar")
----------------------------------h bar------------------------------------

import matplotlib.pyplot as plt
player=["Haland","Neymar","Messi","Ronaldo"]
goals=[10,50,65,150]

plt.title("Goals per player")
plt.xlabel("player")
plt.ylabel("goals")

plt.barh(player,goals,color="blue")         #.barh for ploting horizontal bar chart
plt.show()


-------------------------------Scatter plot-----------------------------------

import matplotlib.pyplot as plt
tree=[100,200,350,600]
pollution=[100,50,20,5]

plt.title("trees vs pollution")
plt.xlabel("no of trees")
plt.ylabel("pollution")
plt.grid()                                                 #for more defined background for graph


plt.scatter(tree,pollution,marker="*",color="purple")       #.scatter for ploting scatter plot chart
plt.show()

-------------------------------Histogram----------------------------------------------

import matplotlib.pyplot as plt
exp=[3,2,3,1,3,5,3,2,1,2,3,5,4]
plt.hist(exp,bins=5)                                       #.hist for histogram 
plt.show()

--------------------------pie chart----------------------------------------------------

import matplotlib.pyplot as plt
player=["Haland","Neymar","Messi","Ronaldo"]
goals=[10,50,65,150]

plt.pie(goals,labels=player)                             #.pie for pie chart (here column that consists no will come first then the column will be second with "labels=" )
#plt.pie(goals,labels=player,autopct="%1.1f%%") upgrade    (to see percentage)
plt.show()


-----------------------------Box plot-----------------------
import matplotlib.pyplot as plt

goals=[10,50,65,1500]

plt.ylabel("No of goals")                                       #to find outliner
plt.boxplot(goals)
plt.show()



import matplotlib.pyplot as plt

sales_sal = [10000, 20000, 150000, 30000]
hr_sal = [25000, 35000, 45000, 6000]

plt.boxplot([sales_sal, hr_sal], labels=["Sales", "HR"])

plt.show()
