from sys import stdin
from collections import Counter
n=stdin.readline()
cards=stdin.readline().split()
m=stdin.readline()
numbers=stdin.readline().split()

c=Counter(cards)
for number in numbers:
  if number in c:
    print(c[number], end=' ')
  else:
    print(0, end=' ')
