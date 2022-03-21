
import sys
sys.setrecursionlimit(10**5)
n=int(input())

graph=[ list(map(int, input().split())) for i in range(n)]

visited=[ 0 for i in range(n)]

def dfs(graph, v, visited):
  for i in range(len(graph[v])):
    if graph[v][i]==1 and visited[i]==0:
      visited[i]=1
      dfs(graph, i, visited)

for i in range(n):
  dfs(graph, i, visited)
  print(' '.join(map(str, visited)))

  visited=[0 for i in range(n)]
  


