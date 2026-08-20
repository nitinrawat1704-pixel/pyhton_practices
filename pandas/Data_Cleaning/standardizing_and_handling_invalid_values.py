import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Priya", "Unknown", "Neha", "Vikas", "Sneha", "Arjun", "Pooja"],
    "City": ["Delhi", "Mumbai", "Unknown", "Pune", "Mumbai", "Delhi", "Error", "Chennai"],
    "Department": ["Sales", "HR", "Sales", "Unknown", "Sales", "HR", "IT", "N/A"],
    "Age": [25, 30, "Unknown", 35, 24, "Error", 32, "N/A"],
    "Salary": [30000, "Unknown", 38000, 55000, "Error", 42000, 50000, "N/A"],
    "Sales": [50000, 30000, "Unknown", 40000, 55000, 25000, "Error", "Not Available"]
}

#step 1 standarization

df=pd.DataFrame(data)
df["City"].value_counts()  #here there are 2 name for missing data named as error or unknow 

df["City"]=df["City"].replace("Error","Unknown") #narrow it down to one name

df["City"].value_counts()

#do same for every columns which has this kind of situation

df["Department"]=df["Department"].replace("N/A","Unknown") 

df["Age"]=df["Age"].replace(["Error","N/A"],"Unknown")  #multiple column change to one name

df["Salary"]=df["Salary"].replace(["Error","N/A"],"Unknown")

df["Sales"]=df["Sales"].replace(["Error","Not Available"],"Unknown")

#convert to numeric

#now it'll make sense to change the data type according to column data 
#for ex- age,salary and sales column contains number so its better to change them into no data type
print(df.dtypes)
df["Age"]=pd.to_numeric(df["Age"],errors="coerce")
df["Salary"]=pd.to_numeric(df["Salary"],errors="coerce")
df["Sales"]=pd.to_numeric(df["Sales"],errors="coerce")

print(df.dtypes)

#"unknown"has turned to null
#now that the column is in numeric form we can fill null values with average value of it column data
print(df)

df["Age"]=df["Age"].fillna(df["Age"].mean().round())


df["Salary"]=df["Salary"].fillna(df["Salary"].mean().round())


df["Sales"]=df["Sales"].fillna(df["Sales"].mean().round())

print(df)
