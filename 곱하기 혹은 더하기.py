from collections import deque
# 큐에 넣어놓고 앞에서 하나씩 제거해나가면서 값을 처리하면 될 것 같다.
# 제거 연산이 빈번하게 일어나므로 deque사용

# 문자열 입력 받기
s = deque(map(int, input()))

answer = s.popleft() # 처음에 하나 꺼내기

while s:
    num = s.popleft() # 두 번째 거 꺼내기
    if answer==0 or num==0 :
        answer = answer+num
        # 곱했을 때 0이 되는 경우를 피하고자 answer == 0 or num == 0인 경우 더하라고 코드를 짰다.
    else:
        answer = answer*num

print(answer)
