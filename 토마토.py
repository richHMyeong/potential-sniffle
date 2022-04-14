from collections import deque

m,n = map(int, input().split())

graph=[]
queue=deque()
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(m):
    if graph[i][j]==1: #1이 있는 위치 저장
      queue.append((i, j))

#좌/우/하/상
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def bfs():
  while queue:
    x, y = queue.popleft()
    #상하좌우 확인
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if graph[nx][ny]!=0:
        continue
      graph[nx][ny]=graph[x][y]+1
      queue.append((nx, ny))

bfs()
answer=0
for i in graph:
  for j in i:
    if j==0:
      print(-1)
      exit(0)
  answer=max(answer, max(i))

print(answer-1)

