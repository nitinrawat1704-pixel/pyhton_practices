import pandas as pd
df=pd.read_excel("/content/Store Data Analysis (1).xlsx")    # file in my colab

# print(df.head(5))                                          # top five rows

# print(df.shape)                                            # Gives no rows and no of columns

# print(df.columns)                                          # column name

# print(df.info())                                           # Number of rows,Number of columns,Column names,Non-null values,Data types,Memory usage

# print(df.describe())                                       # give count,div,max,min etc for each column 

# df.columns=df.columns.str.strip()                          # removes space from column name

# print(df[["Amount","Channel","Status"]])                   # fetch particular column from table

# # print(df[df["Gender"]=="Women"])                         # conditioning

# print(df[df["Amount"]>400 | (df["Gender"]=="Men")]) or 
# print(df[df["Amount"]>400 & (df["Gender"]=="Men")]) and
# print(df[df["Amount"]>500 & (df["Amount"]<1000) & (df["Gender"]=="Women")])
