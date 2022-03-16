n = int(input())

graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

list=[]
val=0
def dfs(x, y):
  global val
  if x<= -1 or x>=n or y<=-1 or y>=n:
    return False
  if graph[x][y]==1:
    graph[x][y]=0
    val+=1
    
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    
    return True
  return False


result=0
for i in range(n):
  for j in range(n):
    if dfs(i, j) == True:
      list.append(val)
      val=0
      result+=1

list.sort()
print(result)
for i in range(len(list)):
  print(list[i])
