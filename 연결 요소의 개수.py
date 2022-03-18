n, m = map(int, input().split())

graph=[ [] for i in range(n+1)]

for i in range(m):
  v1, v2=map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)


visited=[False]*(n+1)

def dfs(graph, v, visited):
  visited[v]=True

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)



result=0
for i in range(1, n+1):
  if not visited[i]:
    dfs(graph, i, visited)
    result+=1


print(result)
