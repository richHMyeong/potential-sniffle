n, m = map(int, input().split())

array=[]
for i in range(n):
  array.append(int(input()))

d=[10001]*(m+1)
d[0]=0
for i in range(n):
  for j in range(array[i], m+1):
    if d[j-array[i]] != 10001: #k원을 만들 방법이 존재하는 경우. 이 if문은 없어도 상관 없음. 어차피 아래 min에서 알아서 반환됨.
      d[j] = min(d[j], d[j - array[i]]+1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
      
      
