import sys

n = int(input())
data = [int(sys.stdin.readline()) for i in range(n)]

data.sort()

answer=0
for i in range(1, n+1):
    if data[i-1] != i:
        cha=abs(data[i-1]-i)
        answer+=cha

print(answer)
