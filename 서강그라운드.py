import sys
INF = int(1e9)
input=sys.stdin.readline

#노드, 수색범위, 간선 수 입력 받기
n, m, r = map(int, input().split())
#2차원 리스트 무한으로 초기화
graph=[[INF] * (n+1) for _ in range(n+1)]

items=list(map(int, input().split()))
          
#자기자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b]=0

#간선 정보 입력 받음
for _ in range(r):
  #a와 b가 서로에게 가는 비용은 c로 설정
  a, b, c = map(int, input().split())
  graph[a][b]=c
  graph[b][a]=c

#플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      dist= min(graph[a][b], graph[a][k] + graph[k][b])
      if dist>m:
        graph[a][b] = INF
      else:
        graph[a][b] = dist

#얻을 수 있는 아이템의 최대 개수 찾기
max_count=0
for i in range(1, n+1):
  sum=0
  for j in range(1, n+1):
    if graph[i][j]!=INF:
      sum+=items[j-1]
  if max_count<sum:
    max_count=sum

print(max_count)
