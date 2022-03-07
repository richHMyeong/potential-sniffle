import sys

n, m = map(int, input().split())

data = list(map(int, sys.stdin.readline().split()))

for i in range(m):
  data.sort()
  tmp=data[0]+data[1]
  data[0]=tmp
  data[1]=tmp

answer=0
for i in data:
  answer+=i

print(answer)
