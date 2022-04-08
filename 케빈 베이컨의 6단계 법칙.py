import sys
INF = int(1e9)
input=sys.stdin.readline

#노드, 간선 개수 입력 받기
n, m = map(int, input().split())
#2차원 리스트 무한으로 초기화
graph=[[INF] * (n+1) for _ in range(n+1)]

#자기자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b]=0

#간선 정보 입력 받음
for _ in range(m):
  #a와 b가 서로에게 가는 비용은 1로 설정
  a, b = map(int, input().split())
  graph[a][b]=1
  graph[b][a]=1

#플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#케빈 베이컨의 수가 가장 작은 사람을 출력
min_index=0
min_val=INF
for i in range(1, n+1):
  sum=0
  for j in range(1, n+1):
    if graph[i][j]!=INF:
      sum+=graph[i][j]
  if min_val>sum:
    min_val=sum
    min_index=i


print(min_index)
