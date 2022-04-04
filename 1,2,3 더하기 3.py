from sys import stdin
t=int(stdin.readline())
data=[ int(stdin.readline()) for i in range(t)]
max_val=max(data)

d=[0]*1000001
d[1]=1
d[2]=2
d[3]=4

for i in range(4,max_val+1):
  d[i]=(d[i-3]+d[i-2]+d[i-1])%1000000009
for i in data:
  print(d[i])
