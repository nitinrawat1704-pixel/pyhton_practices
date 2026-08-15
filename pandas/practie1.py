1. Add a new column Annual_Income by multiplying Income by 12.

2. Add a new column Loan_Amount_Lakhs by dividing Loan_Amount by 100000.

3. Display applicants whose Income is greater than 60000.

4. Display applicants whose Loan_Amount is greater than 500000.

5. Display applicants whose Credit_Score is greater than 750.

6. Display applicants whose Loan_Status is "Approved".

7. Display only Female applicants.

8. Display applicants whose Income is less than 50000.

9. Display applicants whose Loan_Amount is equal to 5000.

10. Display applicants whose Age is greater than 30 AND Loan_Status is "Approved".

11. Display applicants whose Employment_Type is "Salaried" OR whose Gender is "Male".

12. Display applicants whose Loan_Amount is greater than 400000 OR Credit_Score is greater than 780.

 

data = {

    "Loan_ID": [

        1001, 1002, 1003, 1004, 1005,

        1006, 1007, 1008, 1009, 1010,

        1011, 1012, 1013, 1014, 1015,

        1016, 1017, 1018, 1019, 1020

    ],

 

    "Applicant_Name": [

        "Rahul Sharma", "Priya Verma", "Amit Kumar", "Neha Singh", "Rohan Mehta",

        "Anjali Gupta", "Vikas Yadav", "Sneha Kapoor", "Arjun Malhotra", "Pooja Jain",

        "Karan Patel", "Simran Kaur", "Manish Sharma", "Ritika Joshi", "Aditya Rao",

        "Nisha Agarwal", "Suresh Kumar", "Meena Rani", "Varun Gupta", "Kavita Singh"

    ],

 

    "Age": [

        28, 35, 42, 31, 29,

        45, 38, 27, 33, 40,

        36, 30, 48, 26, 34,

        39, 44, 32, 37, 41

    ],

 

    "Gender": [

        "Male", "Female", "Male", "Female", "Male",

        "Female", "Male", "Female", "Male", "Female",

        "Male", "Female", "Male", "Female", "Male",

        "Female", "Male", "Female", "Male", "Female"

    ],

 

    "Income": [

        45000, 60000, 75000, 52000, 48000,

        90000, 68000, 42000, 80000, 55000,

        72000, 65000, 95000, 40000, 70000,

        58000, 85000, 50000, 78000, 62000

    ],

 

    "Loan_Amount": [

        250000, 400000, 600000, 300000, 275000,

        800000, 500000, 200000, 650000, 350000,

        550000, 450000, 900000, 180000, 500000,

        375000, 700000, 280000, 620000, 420000

    ],

 

    "Loan_Term": [

        5, 10, 15, 7, 5,

        20, 15, 5, 20, 10,

        15, 10, 20, 5, 15,

        10, 20, 7, 15, 10

    ],

 

    "Credit_Score": [

        720, 680, 750, 690, 710,

        800, 740, 650, 780, 700,

        730, 690, 810, 640, 760,

        710, 790, 675, 745, 700

    ],

 

    "Employment_Type": [

        "Salaried", "Self-Employed", "Salaried", "Salaried", "Business",

        "Salaried", "Business", "Salaried", "Salaried", "Self-Employed",

        "Salaried", "Business", "Salaried", "Salaried", "Business",

        "Salaried", "Self-Employed", "Salaried", "Business", "Salaried"

    ],

 

    "Loan_Status": [

        "Approved", "Approved", "Approved", "Approved", "Rejected",

        "Approved", "Approved", "Rejected", "Approved", "Approved",

        "Approved", "Rejected", "Approved", "Rejected", "Approved",

        "Approved", "Approved", "Rejected", "Approved", "Approved"

    ]

}


import pandas as pd

df = pd.DataFrame(data)

1.df["Annual income"]=df["Income"] *12  

2.df["Loan_Amount_Lakhs"]=df["Loan_Amount"]/100000

3.print(df[df["Income"] > 60000])

4.print(df[df["Loan_Amount"] > 500000])

5.print(df[df["Credit_Score"] > 750])

6.print(df[df["Loan_Status"] == "Approved"])

7.print(df[df["Gender"] == "Female"])

8.print(df[df["Income"] < 50000])

9.print(df[df["Loan_Amount"] == 5000])

10.print(df[(df["Age"] > 30) & (df["Loan_Status"]=="Approved")])

11.print(df[(df["Employment_Type"] == "Salaried") & (df["Gender"]=="Male")])

12.print(df[(df["Loan_Amount"] > 400000) & (df["Credit_Score"]>780)]) 
