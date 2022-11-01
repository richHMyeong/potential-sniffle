
import heapq # 쉬운 문제 (낮은 숫자)부터 풀어야 하므로 heapq 사용

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, input().split())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]  # 0번째 리스트는 사용x

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 a에서 b로 이동 가능
    # 진입 차수를 1로 증가
    indegree[b] += 1
    
# 위상 정렬 함수 
"""
문제
4 2
4 2
3 1
"""
def topology_sort():
    result = []  # 알고리즘 수행 결과를 담을 리스트
    heap = []

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    # 현재 힙은 3, 4. 3이 먼저 나온다.

    # 힙이 빌 때까지 반복
    while heap:
        # 힙에서 원소 꺼내기
        now = heapq.heappop(heap) # 3 꺼냄
        # 현재 힙이 4,1인데 1이 4보다 쉬운 문제이므로 1를 먼저 꺼낸다.
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                heapq.heappush(heap, i) # 삽입
                # 현재 힙은 1, 4 -> 1이 먼저 나옴
                # result는 3

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')


topology_sort()


# 작은 숫자부터
# 간선 수 적은 것부터
