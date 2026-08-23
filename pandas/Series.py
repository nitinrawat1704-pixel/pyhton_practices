import pandas as pd
l=[50,60,75,55,65,80]
goal=pd.Series(l,index=["Haland","Neymar","Messi","Ronaldo","Mbappe","Rashfoard"])

print(goal["Haland"])
print(goal["Haland":"Messi"])
print(goal[0])
print(goal[0:4])

 print(goal+5)  # every index value is getting added with 5 (list can't do this u have to use loop for that)

#-------------------adding to series------------------------
season2025=[20,33,45,66]
season2026=[50,65,55,10]

#print(season2025+season2026) #cant be done with list

s25=pd.Series(season2025,index=["Haland","Neymar","Messi","Ronaldo"])

s26=pd.Series(season2026,index=["Haland","Neymar","Messi","Ronaldo"])

print("Total goals of 2025 and 2026",s25+s26)

#--------------------------pandas function flexible with series not with list-----------------------

import pandas as pd

books=["sql","excel","sql","excel","python","ML","python","ML","sql","excel","python","ML"]

s1=pd.Series(books)

print(s1.value_counts())

#print(s1)


