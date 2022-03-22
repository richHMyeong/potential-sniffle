import sys

sys.setrecursionlimit(15000)

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def dfs(x, y, height):

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if (0 <= nx <n)  and (0<=ny< n)  and not visited[nx][ny] and graph[nx][ny]>height:
            visited[nx][ny] = True
            dfs(nx, ny, height)

max_area = -1

for k in range(max(map(max, graph))):
    visited = [ [False]*n for i in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>k and not visited[i][j]:
                visited[i][j]=True
                dfs(i, j, k)
                result += 1
    max_area=max(result, max_area)


print(max_area)
