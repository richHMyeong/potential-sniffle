n, l = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

answer=0
t=0
for i in data:
  if t==0:
    t = (i-0.5)+l
    answer+=1
    continue
  if t<i:
    t = (i-0.5)+l
    answer+=1

print(answer)
