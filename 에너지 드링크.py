n = map(int, input())
data = list(map(int, input().split()))

answer=max(data)
ind = data.index(answer)
data[ind]=0
for i in data:
  if i!=0:
    answer+=(i/2)

print(answer)
