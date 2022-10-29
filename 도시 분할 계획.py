# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드 개수, 간선 개수 입력 받기
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v + 1)  # 0번째는 안 쓴다

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서부모를자기 자신으로초기화
for i in range(1, v + 1):
    parent[i] = i
print('초기 부모 테이블: ',parent)

# 간선 정보 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
# 비용순으로 정렬 (적은 것부터)
edges.sort()
# print('정렬한 edges: ', edges)
# 사이클이 발생하지 않는 선에서 가장 적은 비용으로

cnt = 0
for edge in edges:
    if cnt>=v-2:
        break
    cost, a, b = edge
    # a, b의 부모 노드가 같지 않은 경우 합친다.
    if find_parent(parent, a) != find_parent(parent, b):
        cnt+=1
        union_parent(parent, a, b)
        result += cost  # cost더해준다.
        # print("연결한 노드: ", a,' ',b)
        # print('부모 테이블: ',parent)
        # print('현재 cost: ', result)
print(result)
