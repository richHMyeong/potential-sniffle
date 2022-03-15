from collections import deque

n, m = map(int, input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int, input())))

#방향 정의(상, 하 좌, 우)
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def bfs(x, y): #좌표값받음
  queue = deque()
  queue.append((x,y)) #큐 생성후 현재 위치 삽입
  while queue:
    x, y = queue.popleft() #하나 꺼내서 x, y에 넣음
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      #상하좌우 4번 반복하면서 nx, ny 좌표를 방문했는지 체크
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue #미로 범위 벗어난 경우에는 컨티뉴
      if graph[nx][ny] == 0:
        continue
        #벽인 경우 컨티뉴
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] +1
        queue.append((nx, ny)) 
        #현재 노드의 값+1을 넣어주고 큐에 넣음 (방문처리)
        
  return graph[n-1][m-1]

print(bfs(0, 0))
  

