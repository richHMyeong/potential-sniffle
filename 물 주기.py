n, k, a, b= map(int, input().split())

data=[k for i in range(n)]

start=0
end=a

day=0
dead=False

while True:
  day+=1
  for i in range(n):
    if i>=start and i<end:
      data[i]+=b
    data[i]-=1
    if data[i]==0:
      dead=True
      break;
  if dead:
    break;
  start+=a
  end+=a
  
  if start>=n:
    start=0
    end=a

print(day)
