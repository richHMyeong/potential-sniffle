n = map(int, input().split())
data=list(map(int, input().split()))
data.sort()

sum=0
tmp=0
for i in data:
  tmp+=i
  sum+=tmp

print(sum)
