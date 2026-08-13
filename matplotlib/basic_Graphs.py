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
