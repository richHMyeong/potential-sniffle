from itertools import combinations

# 입력 받기
n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 조합 구하기
combs = list(combinations(balls, 2))

# 구해진 조합의 개수로 answer 정의
answer=len(combs)

# 서로 다른 무게의 공을 고른다고 하였으므로 구해진 조합 중 서로 같은 무게인 경우를 제외
for a, b in combs:
    if a==b:
        answer-=1

# 정답 출력
print(answer)
