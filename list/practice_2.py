marks = [45, 67, 32, 89, 56, 28, 76, 91, 35, 62]
1.Find the length of the list using len().
2.Find the total marks using sum().
3.Find the highest marks using max().
4.Find the lowest marks using min().
5.Sort the marks in ascending order.
6.Sort the marks in descending order.
7.Count how many students scored more than 50.
8.Count how many students passed, assuming passing marks are 40.
9.Count how many students failed, assuming passing marks are 40.
10.Calculate the average marks of all students.

1.print(len(marks))

2.print(sum(marks))

3.print(max(marks))

4.print(min(marks))

5.marks.sort()
  print(marks)

6.marks.sort(reverse=True)
  print(marks)

7.c=0
  for i in marks:
    if i >50:
      c=c+1
  print(c)  

8.pn=0
  for i in marks:
    if i >40:
      pn=pn+1
  print(pn)

9.fn=0
  for i in marks:
    if i < 40:
      fn=fn+1
  print(fn)

10.print(sum(marks)/len(marks))
