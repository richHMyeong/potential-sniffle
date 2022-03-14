#입력받기
n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)] #정점의 개수 +1만큼 graph요소 만듦

for i in range(m): #간선의 개수만큼 돌면서
  v1, v2=map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)
  #양방향이므로

for i in graph:
  i.sort()
#작은순부터 탐색하도록

visited = [False] * (n+1) #노드의 개수+1만큼 방문체크할 원소 만듦. [0]은 안 씀
#dfs 함수 정의
def dfs(graph, v, visited):
  visited[v]=True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)


#bfs 함수 정의
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start]) #초기 원소로 start를 가진 큐 만듦
  visited[start]=True

  while queue:
    v=queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)
