from collections import deque

def solution(n, edge):
    answer=0

    #그래프생성
    graph=[]
    for i in range(n+1):
        graph.append([])
        
    for (a, b) in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    #방문확인을 위한 리스트 생성
    visited=[0]*(n+1)

    queue = deque(graph[1])   #1번 노드를 큐에 넣고
    visited[1]=-1         #1번 노드 방문했다는 의미로 -1로 변경
    dist=1      #1번노드와의 거리를 확인하기 위한 변수 
    while queue:   #큐에 노드가 있는 동안
        for i in range(len(queue)):   #큐의 길이만큼(큐에 있는 모든 노드에 대해)
            v=queue.popleft()     #큐의 왼쪽에서 하나 빼서
            if visited[v]==0:     #해당 노드를 방문하지 않았을 경우
                visited[v] = dist  #dist를 넣어줌으로써 방문 처리
                for j in graph[v]:  #해당 노드와 연결되어 있는 모든 노드를 큐에 삽입
                    queue.append(j)
        dist+=1   #큐에 있는 노드 개수만큼 반복한 후에는 dist에 +1을 해준다.

    max_value = max(visited)  #최대값 찾아서 max_value에 넣음

    for i in visited:   #visited리스트 순회하면서
        if max_value==i:   #최대값과 같은 게 몇 개 있는지 확인
            answer+=1
    return answer
