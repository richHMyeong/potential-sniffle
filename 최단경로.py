import heapq
import sys
input=sys.stdin.readline
INF = int(1e9)

#노드, 간선
n, m=map(int, input().split())
#시작 노드
start=int(input())
#각 노드에 연결되어 있는 노드에 대한 정보 (노드 번호, 가중치)
graph = [[] for i in range(n+1)]
#최단거리 테이블. 무한으로 초기화
distance=[INF]*(n+1)

#간선 정보 입력 받음
for _ in range(m):
  a, b, c = map(int, input().split())
  #a에서 b로 가는 간선. 간선의 가중치는 c
  graph[a].append((b, c)) 

def dijkstra(start):
  q=[] #힙큐
  heapq.heappush(q, (0, start)) #거리0으로 start노드를 힙큐에 삽입
  distance[start] = 0 #거리 0으로 설정
  while q: #힙큐에 노드가 있는 동안
    #힙큐에서 가장 거리가 짧은 노드 하나 꺼냄
    dist, now = heapq.heappop(q)
    #꺼낸 노드가 이전에 처리된 적 있다면 무시
    if distance[now] < dist:
      continue

    #현재 노드와 연결된 노드 확인
    for i in graph[now]:
      #cost는 현재 노드를 거쳐서 가는 경로의 가중치
      cost=dist+i[1]
      #cost가 최단거리인 경우
      if cost<distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
  if distance[i]==INF:
    print("INF")
  else:
    print(distance[i])
  
