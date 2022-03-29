from sys import stdin

t=int(stdin.readline())
numbers=[]
for i in range(t):
  numbers.append(int(stdin.readline()))
n=max(numbers)


d=[ [0,0] for i in range(n+1)]

if n>0:
  d[0] = [1, 0]
  d[1] = [0, 1]
else:
  d[0] = [1, 0]

for i in range(2, n+1):
  d[i]=[d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1]]

for i in numbers:
  print(' '.join(map(str, d[i])))
