from heapq import heappop, heappush

input_string = list(input())
pq = []
sum = 0
for x in input_string:
    if x.isalpha():
        heappush(pq, x)
    else:
        sum += int(x)

answer = ''
length = len(pq)
for i in range(length):
    answer += heappop(pq)

answer += str(sum)
print(answer)
'''
예시
K1KA5CB7 -> ABCKK13
AJKDLSI412K4JSJ9D -> ADDIJJJKKLSS20
'''
