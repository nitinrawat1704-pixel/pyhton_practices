A. Add New Columns
1. Add a new column Annual_Salary by multiplying Salary by 12.
2. Add a new column Bonus equal to 10% of Sales.
3. Add a new column Total_Income by adding Salary and Bonus.
4. Add a new column Sales_Lakhs by dividing Sales by 100000.
________________


B. Remove Columns
5. Remove the Age column from the DataFrame.
6. Remove the Department and Sales_Lakhs columns.
7. Remove the Employee_ID column permanently using inplace=True.
________________


C. Remove Rows
8. Remove the first row from the DataFrame.
9. Remove the row having Employee_ID = 105.
10. Remove the last two rows from the DataFrame.
________________


D. Filter Rows
11. Display employees whose Salary is greater than 40,000.
12. Display employees whose Sales are less than 50,000.
13. Display employees who belong to the Sales department.
14. Display employees who are from Delhi.
________________


E. AND Condition
15. Display employees whose Salary is greater than 40,000 AND Sales are greater than 50,000.
16. Display employees who are from Delhi AND belong to the Sales department.
________________


F. OR Condition
17. Display employees who are from Delhi OR Mumbai.
18. Display employees whose Salary is less than 30,000 OR Sales are greater than 60,000.
________________


G. NOT Condition
19. Display employees who are NOT from Delhi.
________________


H. Rename Columns
20. Rename the following columns:
* Name → Employee_Name
* City → Location
* Salary → Monthly_Salary




 # ------------------------------------------------------------
 A. Add New Columns
 # ------------------------------------------------------------

# Q1. Add Annual_Salary
...
df["Annual Salary"]=df["Salary"]*12
# Q2. Add Bonus
...
df["Bonus"]=df["Sales"]*.10
# Q3. Add Total_Income
...
df["Total Income"]=df["Bonus"]+df["Annual Salary"]
# Q4. Add Sales_Lakhs
...
df["Sales in lakhs"]=df["Sales"]/100000

 # ------------------------------------------------------------
 B. Remove Columns
 # ------------------------------------------------------------

# Q5. Remove Age
...
df1=df.drop("Age",axis=1)
print(df1)
# Q6. Remove Department and Sales_Lakhs
...
df2=df.drop(["Department","Sales in lakhs"],axis=1)
print(df2)
# Q7. Remove Employee_ID permanently
...
df.drop("Employee_ID",axis=1,inplace=True)
print(df)

# ------------------------------------------------------------
 C. Remove Rows
# ------------------------------------------------------------

# Q8. Remove first row
...
df=df.drop([0])
print(df)
# Q9. Remove Employee_ID = 105
...
 df=df.drop(df[df["Employee_ID"]==105].index)
 print(df)
# Q10. Remove last two rows
...
r,c=df.shape
print(r-1,r-2)
df=df.drop([r-1,r-2])
print(df)

# ============================================================
D. FILTER ROWS
# ============================================================

# Q11. Display employees whose Salary is greater than 40,000.
# ...
print(df[df["Salary"]>40000])

# Q12. Display employees whose Sales are less than 50,000.
# ...
print(df[df["Sales"]<50000])

# Q13. Display employees who belong to the Sales department.
# ...
print(df[df["Department"]=="Sales"])

# Q14. Display employees who are from Delhi.
# ...
print(df[df["City"]=="Delhi"])

# ============================================================
 E. AND CONDITION
# ============================================================

# Q15. Display employees whose Salary is greater than 40,000
#     AND Sales are greater than 50,000.
# ...
print(df[(df["Salary"]>4000) & (df["Sales"]>50000)])


# Q16. Display employees who are from Delhi
#     AND belong to the Sales department.
# ...
print(df[(df["City"]=="Delhi") & (df["Department"]=="Sales")])
# ============================================================
 F. OR CONDITION
# ============================================================

# Q17. Display employees who are from Delhi OR Mumbai.
# ...
print(df[(df["City"]=="Delhi") | (df["City"]=="Mumbai")])

# Q18. Display employees whose Salary is less than 30,000
#     OR Sales are greater than 60,000.
# ...
print(df[(df["Salary"]<30000) | (df["Salary"]>60000)])

# ============================================================
 G. NOT CONDITION
# ============================================================

# Q19. Display employees who are NOT from Delhi.
# ...
print(df[df["City"]!="Delhi"])

# ============================================================
 H. RENAME COLUMNS
# ============================================================

# Q20. Rename the following columns:
#      Name   → Employee_Name
#      City   → Location
#      Salary → Monthly_Salary

df=pd.DataFrame(data)
df.rename(columns={"Name":"Employee_name","City":"Location","Salary":"Monthly sal"},inplace=True)
print(df)


