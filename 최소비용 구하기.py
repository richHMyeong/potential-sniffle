import sys
import heapq
INF=int(1e9) #INF값 설정
input=sys.stdin.readline

#노드 수, 간선 수 입력받기
n=int(input())
m=int(input())

#그래프, DISTANCE 배열 초기화
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

#간선 입력받기
for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

#START, end 노드 입력받기
start, end = map(int,input().split())

#다익스트라 알고리즘
def dijkstra(start):
  #힙큐 사용
  q=[]
  heapq.heappush(q, (0, start)) #start는 거리 0으로 넣기
  distance[start]=0 #distance 리스트도 start는 자기 자신이니까 0으로 해두기
  #힙큐에 노드가 있는 동안
  while q:
    dist, now=heapq.heappop(q) #큐에서 하나 꺼내서
    if distance[now] < dist: #이전에 처리했던 노드라면 continue
      continue
    for i in graph[now]: #꺼낸 노드와 인접한 노드 살핌
      cost=dist+i[1] #현재 노드를 경유하는 경로의 비용을 cost로 설정
      if cost<distance[i[0]]: #현재 노드를 경유하는 게 비용이 더 적은 경우
        distance[i[0]]=cost #distance 갱신
        heapq.heappush(q, (cost, i[0])) #힙큐에 현재 노드와 갱신된 최저 비용 삽입

dijkstra(start) #다익스트라 알고리즘 실행

print(distance[end]) #결과 출력
  
