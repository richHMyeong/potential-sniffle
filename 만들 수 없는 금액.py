import itertools

# 인풋 받기
n = int(input())
nums = list(map(int, input().split()))
# output은 8

sum_list = []
# 만들 수 있는 모든 합 확인
for i in range(len(nums)):
    com_list = list(itertools.combinations(nums,
                                           i + 1))  # i+1개의 수를 골라 조합을 만든다.
    for com in com_list:
        sum_list.append(sum(com))

# set해서 정렬 및 중복 제거 실행
sum_list = list(set(sum_list))

# 1부터 차례대로 하나씩 확인.
for i in range(len(sum_list)):
    if i + 1 != sum_list[i]:
        answer = i + 1
        break
    else:
        answer = sum_list[i] + 1  # 1~n까지 다 만들 수 있는 경우. n+1을 못 만든다.

print(answer)
