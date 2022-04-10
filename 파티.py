import heapq
import sys
input = sys.stdin.readline
INF=int(1e9) #무한은 10억으로 설정

#노드, 간선, 도착지점 설정
n, m, x = map(int, input().split())

#그래프
graph=[[] for i in range(n+1)]
#최단거리 테이블
distance = [INF] * (n+1)

#모든 간선 정보를 입력 받기
for _ in range(m):
  a, b, c = map(int, input().split())
  #a에서 b로 가는 비용 c
  graph[a].append((b, c))

#다익스트라 알고리즘
def dijkstra(start):
  q=[]
  heapq.heappush(q, (0, start)) #시작 노드는 거리 0으로 삽입
  distance[start]=0 #시작노드 거리 0으로 초기화
  while q:
    #최단 거리 노드 꺼내서
    dist, now=heapq.heappop(q)
    #이미 처리된 노드라면 무시
    if distance[now]<dist:
      continue
    #인접 노드 확인
    for i in graph[now]:
      cost=dist+i[1]
      #현재 노드 거쳐서 가는 게 더 짧은지 확인
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

#x부터 시작해서 다른 노드로 감
dijkstra(x)
result=distance[:]

#x가 아닌 노드들에 대해 다익스트라 실행. 다른 노드에서 x로 갈 때
for i in range(1, n+1):
  if i!=x:
    distance = [INF] * (n+1)
    dijkstra(i)
    result[i]+=distance[x]

#합이 가장 큰 거 찾기
max_val=0
for i in result:
  if i!=INF and max_val<i:
    max_val=i

print(max_val)
