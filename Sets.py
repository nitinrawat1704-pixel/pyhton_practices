1. Create a set containing 5 numbers.
2. Add a new element using add().
3. Remove an element using remove().
4. Check whether an element exists in a set.
5. Create two sets and find their union.
6. Create two sets and find their intersection.
7. Create two sets and find their difference.
8. Create a set containing duplicate numbers and observe the result.
9. Given two sets of student names, find students present in both sets.
10. Given two sets of students, find students who are present in the first class but not in the second class.

1
ratings={5,4.5,3,3.5,4}
print(ratings)

2
ratings.add(2)
print(ratings)

3
ratings.remove(2)
print(ratings)

4
if 5 in ratings:print("found")
else:("not found")
  
5.
print(s.union(r))

6
print(s.intersection(r))

7
print(s.difference(r))  

8.
It removes the duplicate

9.
first={"nathan","drake","dani","eli"}
second={"nathan","eli"}
print(first.intersection(second))

10.
first={"nathan","drake","dani","eli"}
second={"nathan","eli"}
print(first.difference(second))
