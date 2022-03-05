n, k = map(int, input().split())

data=[]

for _ in range(n):
  data.append(int(input()))

data.sort(reverse=True)

answer=0
for coin in data:
  if coin <= k:
    answer += k // coin
    k=k % coin
    if k==0:
      break

print(answer)
