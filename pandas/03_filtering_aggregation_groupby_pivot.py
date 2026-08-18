import pandas as pd

# ------------------------------------------------------------
# Dataset
# ------------------------------------------------------------

# Create the DataFrame
# ...

data = {
    "Order_ID": [
        1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010,
        1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020,
        1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030
    ],
    "Customer_Name": [
        "Amit", "Priya", "Rahul", "Neha", "Vikas", "Sneha", "Arjun", "Pooja",
        "Karan", "Riya", "Ankit", "Meena", "Rohit", "Simran", "Varun",
        "Kavita", "Manish", "Nisha", "Suresh", "Anjali", "Deepak", "Pallavi",
        "Raj", "Swati", "Mohit", "Komal", "Vivek", "Preeti", "Nitin", "Shweta"
    ],
    "City": [
        "Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi", "Pune", "Chennai",
        "Delhi", "Mumbai", "Jaipur", "Delhi", "Pune", "Mumbai", "Chennai",
        "Delhi", "Jaipur", "Mumbai", "Delhi", "Pune", "Chennai", "Delhi",
        "Mumbai", "Pune", "Delhi", "Jaipur", "Mumbai", "Chennai", "Delhi", "Mumbai"
    ],
    "Product": [
        "Laptop", "Mobile", "Headphones", "Laptop", "Tablet", "Mobile",
        "Laptop", "Smartwatch", "Mobile", "Headphones", "Tablet", "Laptop",
        "Mobile", "Smartwatch", "Laptop", "Headphones", "Tablet", "Mobile",
        "Laptop", "Smartwatch", "Headphones", "Mobile", "Laptop", "Tablet",
        "Mobile", "Headphones", "Laptop", "Smartwatch", "Mobile", "Tablet"
    ],
    "Category": [
        "Electronics", "Electronics", "Accessories", "Electronics", "Electronics",
        "Electronics", "Electronics", "Accessories", "Electronics", "Accessories",
        "Electronics", "Electronics", "Electronics", "Accessories", "Electronics",
        "Accessories", "Electronics", "Electronics", "Electronics", "Accessories",
        "Accessories", "Electronics", "Electronics", "Electronics", "Electronics",
        "Accessories", "Electronics", "Accessories", "Electronics", "Electronics"
    ],
    "Quantity": [
        1, 2, 3, 1, 2, 2, 1, 2, 3, 2,
        1, 1, 2, 1, 1, 3, 2, 2, 1, 1,
        2, 3, 1, 2, 2, 3, 1, 2, 3, 1
    ],
    "Unit_Price": [
        55000, 25000, 2000, 60000, 30000, 22000, 58000, 8000, 24000, 2500,
        28000, 52000, 23000, 9000, 65000, 2200, 32000, 21000, 62000, 7500,
        1800, 26000, 57000, 29000, 24000, 2500, 68000, 8500, 22000, 31000
    ],
    "Payment_Mode": [
        "UPI", "Credit Card", "Cash", "UPI", "Debit Card", "UPI",
        "Credit Card", "UPI", "Debit Card", "Cash", "UPI", "Credit Card",
        "UPI", "Debit Card", "Credit Card", "Cash", "UPI", "Debit Card",
        "Credit Card", "UPI", "Cash", "Credit Card", "UPI", "Debit Card",
        "UPI", "Cash", "Credit Card", "UPI", "Debit Card", "Credit Card"
    ],
    "Sales": [
        55000, 50000, 6000, 60000, 60000, 44000, 58000, 16000, 72000, 5000,
        28000, 52000, 46000, 9000, 65000, 6600, 64000, 42000, 62000, 7500,
        3600, 78000, 57000, 58000, 48000, 7500, 68000, 17000, 66000, 31000
    ]
}

import pandas as pd

df=pd.DataFrame(data)

# Q1. Display the first 10 rows of the DataFrame.
# ...
print(df.loc[0:9])

# Q2. Display only the Customer_Name, City, Product, and Sales columns.
# ...
print(df[["Customer_Name","City","Product","Sales"]])

# Q3. Find the total number of orders.
# ...
print(df["Order_ID"].sum())


# Q4. Display all orders where Sales is greater than 50,000.
# ...
print(df[df["Sales"]>50000])

# Q5. Display customers who purchased a Laptop.
# ...
print(df[df["Product"]=="Laptop"])

# Q6. Find the total sales generated from all orders.
# ...
print(df["Sales"].sum())

# Q7. Display orders where Quantity is greater than 2
#     AND Sales is greater than 20,000.
# ...
print(df[(df["Quantity"]>2) & (df["Sales"]>20000)])

# Q8. Find the average sales amount.
# ...
print(df["Sales"].mean().round(2))

# Q9. Display customers from Delhi OR Mumbai.
# ...
print(df[(df["City"]=="Mumbai") | (df["City"]=="Delhi")])


# Q10. Add a new column called Total_Value
#      by multiplying Quantity and Unit_Price.
# ...
df["Total value"]=df["Quantity"]*df["Unit_Price"]
print(df)

# Q11. Find the highest Sales value.
# ...
print(df["Sales"].max())

# Q12. Display all orders where the payment mode is UPI.
# ...
print(df[df["Payment_Mode"]=="UPI"])

# Q13. Find the total sales for each city.
# ...
print(df.groupby("City")["Sales"].sum())

# Q14. Remove the Unit_Price column from the DataFrame.
# ...
df.drop("Unit_Price",axis=1,inplace=True)
print(df)

# Q15. Find the average sales for each product.
# ...
print(df.groupby("Product")["Sales"].mean())

# Q16. Display orders where the customer is not from Delhi.
# ...
print(df[df["City"]!="Delhi"])

# Q17. Find the number of orders for each payment mode.
# ...
print(df.groupby("Payment_Mode")["Order_ID"].count())

# Q18. Rename the column Customer_Name to Customer.
# ...
df.rename({"Customer_Name":"Customer"},axis=1,inplace=True)

# Q19. Find the maximum quantity purchased for each product.
# ...
print(df.groupby("Product")["Quantity"].max())

# Q20. Display orders where the Category is Electronics
#      AND Sales is greater than 40,000.
# ...
print(df[(df["Category"]=="Electronics") & (df["Sales"]>40000)])

# Q21. Find the total sales for each category.
# ...
df.groupby("Category")["Sales"].sum()

# Q22. Remove the Payment_Mode column.
# ...
df.drop("Payment_Mode",axis=1,inplace=True)
print(df)

# Q23. Find the total and average sales for each city.
# ...
df.groupby("City")["Sales"].agg(['sum','mean'])

# Q24. Find the total sales for each City and Product.
# ...
Find the total sales for each City and Product



# Q25. Create a pivot table showing total Sales by City and Product.
# ...
pd.pivot_table(df,values="Sales",index="City",columns="Product",aggfunc="sum")

# Q26. Create a pivot table showing average Sales
#      by Payment Mode and Category.
# ...
pd.pivot_table(df,values="Sales",index="Payment_Mode",columns="Category",aggfunc="mean")


# Q27. Display the order with the highest Sales.
# ...
print(df[df["Sales"]== df["Sales"].max()])

# Q28. Find the total quantity sold for each product.
# ...
print(df.groupby("Product")["Quantity"].sum())

# Q29. Find the average Unit_Price for each category.
# ...
print(df.groupby("Category")["Unit_Price"].mean())


# Q30. Create a pivot table showing the total Quantity purchased
#      by City and Category.
# ...
print(pd.pivot_table(df,values="Quantity",index="City",columns="Category",aggfunc="sum"))
