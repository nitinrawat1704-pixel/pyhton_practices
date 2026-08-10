def add(a,b):
  print(a+b)
def sub(a,b):
  if a>b:print(a-b)
  else:print(b-a)
def div(a,b):
  if a>b:print(a/b)
  else:print(b/a)
def mul(a,b):
  print(a*b)
def cube(a):
  print(a*a*a)




while True:
 print("1.add\n2.sub\n3.mul\n4.divn\n5.exit")
 ch=int(input("enter your choice"))
 if ch ==5 :
  print("exiting..")
  break
 else:
  x=int(input("enter 1st no:"))
  y=int(input("enter 2nd no:"))
  if ch ==1:add(x,y)
  elif ch ==2:sub(x,y)
  elif ch ==3:mul(x,y)
  elif ch ==4:div(x,y)
