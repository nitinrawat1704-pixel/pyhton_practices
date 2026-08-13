--------------------------line chart-------------------------------------

import matplotlib.pyplot as plt
player=["Haland","Neymar","Messi","Ronaldo"]
goals=[10,50,65,150]



plt.title("Goals per player")                   #Title display
plt.xlabel("player")                            #X axis display
plt.ylabel("goals")                             #Y axis display

plt.plot(player,goals)                          #.plot for ploting line graph
#plt.plot(player,goals,marker="*")              #upgrade 1
#plt.plot(player,goals,marker="*",color="blue") #upgrade 2
plt.show()


------------------------------bar chart--------------------------------

import matplotlib.pyplot as plt
player=["Haland","Neymar","Messi","Ronaldo"]
goals=[10,50,65,150]

plt.title("Goals per player")
plt.xlabel("player")
plt.ylabel("goals")

plt.bar(player,goals,color="blue")         #.bar for ploting bar chart
plt.show()


----------------------------------h bar------------------------------------

import matplotlib.pyplot as plt
player=["Haland","Neymar","Messi","Ronaldo"]
goals=[10,50,65,150]

plt.title("Goals per player")
plt.xlabel("player")
plt.ylabel("goals")

plt.barh(player,goals,color="blue")         #.barh for ploting horizontal bar chart
plt.show()



-------------------------------Scatter plot-----------------------------------

import matplotlib.pyplot as plt
tree=[100,200,350,600]
pollution=[100,50,20,5]

plt.title("trees vs pollution")
plt.xlabel("no of trees")
plt.ylabel("pollution")
plt.grid()                                                 #for more defined background for graph


plt.scatter(tree,pollution,marker="*",color="purple")       #.scatter for ploting scatter plot chart
plt.show()

-------------------------------Histogram----------------------------------------------

import matplotlib.pyplot as plt
exp=[3,2,3,1,3,5,3,2,1,2,3,5,4]
plt.hist(exp,bins=5)                                       #.hist for histogram 
plt.show()

--------------------------pie chart----------------------------------------------------

import matplotlib.pyplot as plt
player=["Haland","Neymar","Messi","Ronaldo"]
goals=[10,50,65,150]

plt.pie(goals,labels=player)                             #.pie for pie chart (here column that consists no will come first then the column will be second with "labels=" )
#plt.pie(goals,labels=player,autopct="%1.1f%%") upgrade    (to see percentage)
plt.show()


