import pandas as pd
l=[50,60,75,55,65,80]
goal=pd.Series(l,index=["Haland","Neymar","Messi","Ronaldo","Mbappe","Rashfoard"])

print(goal["Haland"])
print(goal["Haland":"Messi"])
print(goal[0])
print(goal[0:4])

 print(goal+5)  # every index value is getting added with 5 (list can't do this u have to use loop for that)
