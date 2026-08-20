  import pandas as pd

  data = {
      "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
      "Name": ["Amit", "Priya", "Rahul", "Neha", "Vikas", "Sneha", "Arjun", "Pooja"],
      "City": ["Delhi", "Mumbai", None, "Pune", "Mumbai", "Delhi", None, "Chennai"],
      "Department": ["Sales", "HR", "Sales", None, "Sales", "HR", "IT", "IT"],
      "Age": [25, 30, None, 35, 24, 29, 32, None],
      "Salary": [30000, None, 38000, 55000, 28000, None, 50000, 40000],
      "Sales": [50000, 30000, None, 40000, 55000, 25000, 70000, None]
  }

  df=pd.DataFrame(data)
 
  df.isnull().sum()

  print(df["City"].isnull().sum())                                        #there are two null values 
  df["City"]=df["City"].fillna("Delhi")                                   #replacing null value with Delhi
  print(df["City"].isnull().sum())                                        #Now there is No null values in City column 

  # simillar for other columns
  df["Department"]=df["Department"].fillna("Temp")

  df["Age"]=df["Age"].fillna(df["Age"].mean().round())                     #replacing null with avg age

  df["Salary"]=df["Salary"].fillna(df["Salary"].mean().round())            #replacing null with avg Salary

  df["Sales"]=df["Sales"].fillna(df["Sales"].mean().round())               #replacing null with avg Sales

  print(df.isnull().sum())
