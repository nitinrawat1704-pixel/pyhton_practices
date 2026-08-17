import pandas as pd


# ============================================================
# Pandas Practice - Filtering, GroupBy & Pivot Tables
# ============================================================


# ------------------------------------------------------------
# Dataset
# ------------------------------------------------------------


data = {
    "Loan_ID": [
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
    "Loan_Type": [
        "Home", "Personal", "Car", "Home", "Education", "Personal", "Home",
        "Car", "Personal", "Home", "Car", "Education", "Home", "Personal",
        "Car", "Home", "Education", "Personal", "Car", "Home", "Personal",
        "Education", "Home", "Car", "Personal", "Home", "Education", "Car",
        "Home", "Personal"
    ],
    "Loan_Amount": [
        500000, 200000, 350000, 800000, 300000, 150000, 700000, 450000,
        250000, 900000, 400000, 250000, 650000, 180000, 500000, 750000,
        300000, 220000, 400000, 850000, 275000, 350000, 600000, 450000,
        200000, 700000, 320000, 500000, 950000, 150000
    ],
    "Interest_Rate": [
        8.5, 12.0, 9.5, 8.2, 7.5, 13.0, 8.0, 10.5, 11.5, 8.3,
        9.2, 7.8, 8.7, 12.5, 9.8, 8.1, 7.2, 13.5, 10.2, 8.4,
        12.2, 7.6, 8.9, 10.0, 11.8, 8.6, 7.4, 10.8, 8.0, 12.8
    ],
    "Loan_Term": [
        120, 60, 84, 240, 60, 36, 180, 84, 48, 240,
        60, 48, 180, 60, 84, 240, 60, 48, 84, 240,
        48, 60, 180, 84, 48, 180, 60, 84, 240, 36
    ],
    "Credit_Score": [
        750, 680, 720, 790, 710, 650, 780, 700, 690, 810,
        730, 680, 760, 640, 725, 800, 710, 660, 740, 795,
        670, 720, 770, 705, 690, 785, 715, 675, 805, 655
    ],
    "Loan_Status": [
        "Approved", "Approved", "Approved", "Approved", "Approved",
        "Rejected", "Approved", "Approved", "Rejected", "Approved",
        "Approved", "Rejected", "Approved", "Rejected", "Approved",
        "Approved", "Approved", "Rejected", "Approved", "Approved",
        "Rejected", "Approved", "Approved", "Rejected", "Approved",
        "Approved", "Rejected", "Approved", "Approved", "Rejected"
    ]
}

df = pd.DataFrame(data)

# ============================================================
# A. FILTERING - BASIC
# ============================================================

# Q1. Display all customers whose Loan_Amount is greater than 500000.
# ...
print(df[df["Loan_Amount"]>500000])

# Q2. Display customers whose Interest_Rate is less than 10%.
# ...
print(df[df["Interest_Rate"]<10])


# Q3. Display customers whose Credit_Score is greater than 750.
# ...
print(df[df["Credit_Score"]>750])

# Q4. Display all customers whose Loan_Status is "Approved".
# ...
print(df[df["Loan_Status"]=="Approved"])

# Q5. Display all customers who took a Home loan.
# ...
print(df[df["Loan_Type"]=="Home"])

# Q6. Display all customers from Delhi.
# ...
print(df[df["City"]=="Delhi"])

# ============================================================
# B. FILTERING - AND / OR / NOT
# ============================================================

# Q7. Display customers whose Loan_Amount is greater than 500000
#     AND Credit_Score is greater than 750.
# ...
print(df[(df["Loan_Amount"]>500000) & (df["Credit_Score"]>750)])

# Q8. Display customers from Delhi AND Mumbai.
# ...
print(df[(df["City"]=="Mumbai") | (df["City"]=="Delhi")])

# Q9. Display customers who have Credit_Score less than 700
#     OR Interest_Rate greater than 12%.
# ...
print(df[(df["Interest_Rate"]>12) & (df["Credit_Score"]<700)])

# Q10. Display customers who are NOT from Delhi.
# ...
print(df[df["City"]!="Delhi"])

# Q11. Display customers whose loan is Approved
#     AND Loan_Amount is greater than 600000.
# ...
print(df[(df["Loan_Status"]=="Approved") & (df["Loan_Amount"]>600000)])

# ============================================================
# C. AGGREGATE FUNCTIONS
# ============================================================

# Functions to practice:
# sum()
# mean()
# min()
# max()
# count()


# Q12. Find the total Loan_Amount.
# ...
print(df["Loan_Amount"].sum())

# Q13. Find the average Loan_Amount.
# ...
print(df["Loan_Amount"].mean())

# Q14. Find the maximum Loan_Amount.
# ...
print(df["Loan_Amount"].max())

# Q15. Find the minimum Interest_Rate.
# ...
print(df["Interest_Rate"].min())

# Q16. Find the average Credit_Score.
# ...
print(df["Credit_Score"].mean())

# Q17. Count the total number of loans.
# ...
print(df["Loan_ID"].count())

# ============================================================
# D. GROUPBY
# ============================================================

# Q18. Find the total Loan_Amount for each City.
# ...
print(df.groupby("City")["Loan_Amount"].sum())

# Q19. Find the average Loan_Amount for each Loan_Type.
# ...
print(df.groupby("Loan_Type")["Loan_Amount"].mean())

# Q20. Find the number of loans for each Loan_Type.
# ...
print(df.groupby("Loan_Type")["Loan_ID"].count())

# Q21. Find the average Interest_Rate for each City.
# ...
print(df.groupby("City")["Interest_Rate"].mean())

# Q22. Find the total Loan_Amount for each Loan_Status.
# ...
print(df.groupby("Loan_Status")["Loan_Amount"].sum())

# Q23. Find the maximum Credit_Score for each Loan_Type.
# ...
print(df.groupby("Loan_Type")["Credit_Score"].max())

# Q24. Find the total Loan_Amount for each City and Loan_Type.
# ...
print(df.groupby(["City", "Loan_Type"])["Loan_Amount"].sum())

# ============================================================
# E. GROUPBY WITH MULTIPLE AGGREGATIONS
# ============================================================

# Q25. For each City, calculate:
#      - Total Loan Amount
#      - Average Loan Amount
#      - Maximum Loan Amount
#      - Minimum Loan Amount
# ...
df.groupby("City")["Loan_Amount"].agg(['sum','mean','max','min'])

# Q26. For each Loan_Type, calculate:
#      - Average Interest Rate
#      - Average Credit Score
#      - Total Loan Amount
# ...

df.groupby("Loan_Type").agg(
    avg_IR=("Interest_Rate","mean"),
    avg_CS=("Credit_Score","mean"),
    sum_LA=("Loan_Amount","sum")
  )

# ============================================================
# F. PIVOT TABLE
# ============================================================

# Q27. Create a pivot table showing total Loan_Amount
#      by City and Loan_Type.
#
pd.pivot_table(df,values="Loan_Amount",index="City",columns="Loan_Type",aggfunc="sum")


# Q28. Create a pivot table showing the average Interest_Rate
#      by City and Loan_Status.
# ...
pd.pivot_table(df,values="Interest_Rate",index="City",columns="Loan_Status",aggfunc="mean")


# Q29. Create a pivot table showing the count of loans
#      by City and Loan_Status.
# ...
pd.pivot_table(df,values="Loan_ID",index="City",columns="Loan_Status",aggfunc="count")


# Q30. Create a pivot table showing the average Credit_Score
#      by Loan_Type and Loan_Status.
# ...

pd.pivot_table(df,values="Credit_Score",index="Loan_Type",columns="Loan_Status",aggfunc="mean")
