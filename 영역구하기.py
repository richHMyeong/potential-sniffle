import sys
sys.setrecursionlimit(10**5)

m, n, k = map(int, input().split())

graph = [[0]*m for i in range(n)]


for i in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for j in range(x1, x2):
    for z in range(y1, y2):
      graph[j][z]=1

cnt=0
def dfs(x, y):
  global cnt
  if x<=-1 or y<=-1 or x>=n or y>=m:
    return False
  if graph[x][y]==0:
    graph[x][y]=1
    cnt+=1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

result=0
list=[]
for i in range(n):
  for j in range(m):
    if dfs(i, j)==True:
      result+=1
      list.append(cnt)
      cnt=0

list.sort()
print(result)
for i in list:
  print(i)
