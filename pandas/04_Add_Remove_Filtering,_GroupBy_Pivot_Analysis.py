# Q1. Display the first 10 rows.
# ...
print(df.loc[0:9])


# Q2. Display only Employee_Name, Department, Salary, and Performance_Score.
# ...
print(df[["Employee_Name","Department","Salary","Performance_Score"]])


# Q3. Find the total number of employees.
# ...
print(df["Employee_ID"].count())


# Q4. Display employees whose salary is greater than 50,000.
# ...
print(df[df["Salary"]>50000])


# Q5. Display employees who belong to the IT department.
# ...
print(df[df["Department"]=="IT"])


# Q6. Find the average salary of all employees.
# ...
print(df["Salary"].mean().round())


# Q7. Display employees whose performance score is greater than 90
#     AND attendance is greater than 95.
# ...
print(df[(df["Performance_Score"]>90) & (df["Attendance"]>95)])


# Q8. Find the highest salary.
# ...
print(df["Salary"].max())


# Q9. Display employees from Delhi OR Mumbai.
# ...
print(df[(df["City"]=="Delhi") | (df["City"]=="Mumbai")])


# Q10. Add a column Annual_Salary by multiplying Salary by 12.
# ...
df["Annual salary"]=df["Salary"]*12
print(df)


# Q11. Find the average performance score.
# ...
print(df["Performance_Score"].mean())


# Q12. Display employees who have completed more than 7 projects.
# ...
print(df[df["Projects_Completed"]>7])


# Q13. Find the total salary paid by each department.
# ...
print(df.groupby("Department")["Salary"].sum())


# Q14. Remove the Attendance column.
# ...
df.drop("Attendance",axis=1,inplace=True)


# Q15. Find the average salary for each department.
# ...
print(df.groupby("Department")["Salary"].mean())


# Q16. Display employees who are not from Delhi.
# ...
print(df[df["City"]!="Delhi"])


# Q17. Find the number of employees in each department.
# ...
print(df.groupby("Department")["Employee_ID"].count())


# Q18. Rename Performance_Score to Performance.
# ...
df.rename({"Performance_Score":"performanece"},axis=1,inplace=True)


# Q19. Find the maximum salary for each department.
# ...
print(df.groupby("Department")["Salary"].max())


# Q20. Display employees with experience greater than 5 years
#      AND performance greater than 85.
# ...
print(df[(df["Experience"]>5) & (df["Performance_Score"]>85)])


# Q21. Find the average experience for each department.
# ...
print(df.groupby("Department")["Experience"].mean())


# Q22. Find the total number of projects completed by each department.
# ...
print(df.groupby("Department")["Projects_Completed"].sum())


# Q23. Find the total and average salary for each city.
# ...
print(df.groupby("Department")["Salary"].agg(['sum','mean']))


# Q24. Find the average performance score for each city.
# ...
df.groupby("City")["Performance_Score"].mean()


# Q25. Find the total salary for each Department and City.
# ...
print(df.groupby(["Department","City"])["Salary"].sum())


# Q26. Create a pivot table showing average Salary by Department and City.
# ...
print(df.pivot_table(values="Salary",index="Department",columns="City",aggfunc="mean"))


# Q27. Create a pivot table showing average Performance by Department and City.
# ...
print(df.pivot_table(values="Performance_Score",index="Department",columns="City",aggfunc="mean"))


# Q28. Find the employee with the highest performance score.
# ...
print(df[df["Performance_Score"]==df["Performance_Score"].max()]["Employee_Name"])


# Q29. Find the department having the highest average salary.
# ...
max_avg_sal=df.groupby("Department")["Salary"].mean().max()
max_dept_sal=df.groupby("Department")["Salary"].mean().idxmax()
print(max_dept_sal,max_avg_sal)


# Q30. Create a pivot table showing total Projects_Completed by Department and City.
# ...
print(pd.pivot_table(df,values="Projects_Completed",index="Department",columns="City",aggfunc="sum"))
