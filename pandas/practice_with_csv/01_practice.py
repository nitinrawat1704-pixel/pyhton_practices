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
df["Customer_Type"]=np.where(df["Age"]<30,"Young","Adult")

def c(a):
  if a<30:return "Young"
  else:return "Adult"

df["Customer_Type1"]=df["Age"].apply(c)


print(df)
