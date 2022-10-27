# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드르를 찾을 때까지 재귀적으로 호출
    if parent[x] !=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합ㅇ르 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: # 수가 더 작은 애를 root로
        parent[b] = a # a가 더 작으니까 a가 루트
    else:
        parent[a] = b
# 노드의 개수와 간선(union연산)의 개수 입력받기
v = int(input())
e = int(input())

# 부모 테이블 초기화
parent = [0] * (v+1) # 0번째는 사용x

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서 부모를 가지 자신으로 초기ㅗ하
for i in range(1, v+1): # 1~v까지
    parent[i]=i

# 모든 간선에 대한 정보 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 이해서 유플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
