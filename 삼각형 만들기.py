import sys
n = int(input())
data = [ int(sys.stdin.readline()) for i in range(n)]

data.sort(reverse=True)

answer=-1
for i in range(len(data)):
  if i==len(data)-2:
    break;
  if data[i]<data[i+1]+data[i+2]:
    answer=data[i]+data[i+1]+data[i+2]
    break;

print(answer)
