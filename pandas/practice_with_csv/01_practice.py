import pandas as pd
df=pd.read_csv("/content/OnlineShop.csv")
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)


# Level 1 — Select Columns

# 1.	Display only the Customer_Name column.
print(df["Customer_Name"])

# 2.	Display only the Product and Price columns.
print(df[["Product","Price"]])

# 3.	Display Customer_Name, City, Product, and Price.
print(df[["Customer_Name","City","Product","Price"]])

# 4.	Display the first 10 rows with only Product, Category, and Price.
print(df[["Product","Category","Price"]].head(10))

# 5.	Display Order_ID, Payment_Mode, and Order_Status.
print(df[["Order_ID","Payment_Mode","Order_Status"]])



# Level 2 — Add New Columns

# 6.	Create a new column Total_Amount using: Quantity × Price
df["Total"]=df["Quantity"]*df["Price"]

# 7.	Create a column Discount and give every customer a 10% discount.
df["Discount"]=df["Total"]*0.10
# print(df)

# 8.	Create Final_Amount after deducting the discount.
df["Final Amount"]=df["Total"]-df["Discount"]
print(df)

# 9.	Create a column Tax calculated at 18% of Total_Amount.
df["Tax"]=df["Total"]*0.18
print(df)

# 10.	Create a column Customer_Type:
# •	Age < 30 → "Young"
# •	Age >= 30 → "Adult"


import numpy as np
df["Customer_Type"]=np.where(df["Age"]<30,"Young","Adult")  #using numpy

def c(a):                                                    #using def
  if a<30:return "Young"
  else:return "Adult"

df["Customer_Type1"]=df["Age"].apply(c)


print(df)

# Level 3 — Remove Columns

# 11.	Delete the Gender column.
df=df.drop("Gender",axis=1) 

# 12.	Delete the Payment_Mode column.
df=df.drop("Payment_Mode",axis=1) 

# 13.	Delete both Gender and Age.
df=df.drop(["Gender","Age"],axis=1)

# 14.	Delete Order_Status and Payment_Mode.
df=df.drop(["Order_Status","Payment_Mode"],axis=1)

# 15.	Create a new DataFrame without the Order_ID column.

df.drop(["Order_ID column"],axis=1,inplace=True)

print(df)

# Level 4 — Filter Rows
# 16.	Display customers whose Age is greater than 30.
print(df[df["Age"]>30])

# 17.	Display customers from Delhi.
print(df[df["City"]=="Delhi"])

# 18.	Display customers from Mumbai.
print(df[df["City"]=="Mumbai"])

# 19.	Display products whose Price is greater than ₹10,000.
print(df[df["Price"]>10000])

# 20.	Display orders where Quantity is greater than 2.
print(df[df["Quantity"]>2])

# 21.	Display all Female customers.
print(df[df["Gender"]=="Female"])

# 22.	Display all Male customers.
print(df[df["Gender"]=="Male"])

# 23.	Display orders having status Delivered.
print(df[df["Order_Status"]=="Delivered"])

# 24.	Display orders having status Cancelled.
print(df[df["Order_Status"]=="Cancelled"])

# 25.	Display orders paid using UPI.
print(df[df["Payment_Mode"]=="UPI"])

# Level 5 — Filter Rows + Columns

# 26.	Display Customer_Name, Product, and Price for customers from Delhi.
print(df[df["City"]=="Delhi"] [["Customer_Name","Product","Price"]])

# 27.	Display Customer_Name, City, and Product where Age > 35.
print(df[df["Age"]>35][["Customer_Name","City","Product"]])

# 28.	Display Product, Quantity, and Price where Price > 5000.
print(df[df["Price"]>5000][["Product","Quantity","Price"]])

# 29.	Display Customer_Name, Product, and Order_Status for Cancelled orders.
print(df[df["Order_Status"]=="Cancelled"][["Customer_Name","Product","Order_Status"]])

# 30.	Display Customer_Name, Product, and Price for Female customers.
print(df[df["Gender"]=="Female"][["Customer_Name","Product","Price"]])

#Level 6 — Multiple Conditions

# 31.	Find customers who are from Delhi AND Age > 30.
print(df[(df['City']=="Delhi") &(df['Age']>30)])

# 32.	Find customers who are from Mumbai OR Pune.
print(df[(df['City']=="Mumbai") | (df['City']=="Pune")])

# 33.	Find products where Price > 10,000 AND Category = Electronics.
print(df[(df["Price"]>10000) & (df["Category"]=="Electronics")])

# 34.	Find customers where Age > 30 AND Gender = Female.
print(df[(df["Age"]>30) & (df["Gender"]=="Female")])

# 35.	Find orders where Quantity >= 2 AND Price > 2000.
print(df[(df["Quantity"]>=2) & (df["Price"]>2000)])

# 36.	Find orders where Order_Status = Delivered AND Payment_Mode = UPI.
print(df[(df["Order_Status"]=="Delivered") & (df["Payment_Mode"]=="UPI")])

# 37.	Find customers from Delhi AND Mumbai using the appropriate Pandas technique.
print(df[df['City'].isin(["Mumbai","Delhi"])])

# 38.	Find Electronics products with price between ₹5,000 and ₹30,000.
print(df[(df['Category']=="Electronics") & (df['Price'].between(5000,30000))])

#Level 7 — Slightly Advanced Filtering

39.	Display all customers whose city is either Delhi, Mumbai, or Bangalore.
print(df[df["City"].isin(["Mumbai","Delhi","Banglore"])])

# 40.	Display all products whose category is Fashion or Electronics.
print(df[df["Product"].isin(["Fashion","Electronics"])])

# 41.	Find customers whose age is between 25 and 35.
print(df[df["Age"].between(25,35)])

# 42.	Find products whose price is between ₹2,000 and ₹10,000.
print(df[df["Age"].between(2000,10000)])

#43.	Find all orders that are not Delivered.
print(df[df["Order_Status"]!="Delivered"])

#44.	Find all customers whose payment mode is not Cash.
print(df[df["Payment_Mode"]!="Cash"])

#45.	Find all Female customers from Delhi or Mumbai.
print(df[(df["Gender"]=="Female") & (df["City"].isin(["Delhi","Mumbai"]))])
