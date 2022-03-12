from collections import deque

n, k = map(int, input().split())

data=deque([i+1 for i in range(n)])

answer=[]
while True:
  if data:
    data.rotate(-k+1)
    answer.append(data.popleft())
  else:
    break

print('<', end='')
print(', '.join(str(x) for x in answer), end='')
print('>')
