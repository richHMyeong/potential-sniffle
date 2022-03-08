import sys

n = int(input())

data = list(map(int, sys.stdin.readline().split()))

answer=0

my = [0 for i in range(n)]

for i in range(n):
  if data[i]!=my[i]:
    answer+=1
    my[i]=my[i]^1      
    
    if i+2<n:
      my[i+1] = my[i+1]^1
      my[i+2] = my[i+2]^1
    elif i+1<n :
      my[i+1] = my[i+1]^1


print(answer)
