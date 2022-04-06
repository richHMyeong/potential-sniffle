import sys
input=sys.stdin.readline

#INF 설정
INF=int(1e9)

#노드, 간선의 개수
n=int(input())
m=int(input())

#그래프 전부 INF로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

#대각선의 경우 자기 자신이니까 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b]=0

#간선을 입력받아 그래프에 삽입
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b]=min(c, graph[a][b]) #노선이 하나가 아닐 수도 있다고 되어 있으므로


#삼중for문
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
      #a->k(현재노드)->b와 a->b 중 더 작은 값을 그래프에 넣음

#출력
for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b]==INF:
      print(0, end=' ')
    else:
      print(graph[a][b], end=' ')
  print()
  
