from collections import deque

def solution(food_times, k):
    answer = -1

    # 순서를 담은 dict 생성
    food_dict = {}
    for i in range(len(food_times)):
        food_dict[i+1] = food_times[i] 
        # i+1번째에 해당 값을 넣음

    que = deque(food_dict) # key만 담는다.
    
    for i in range(k): # k번 돌면서
        if len(que) != 0 : # que에 원소 있는 동안
            now = que.popleft()
            food_dict[now] -= 1 # 1빼주고
            if food_dict[now]>0: # 1을뺐어도 여전히 양수인 경우
                que.append(now) # 다시 넣어준다.
        else:
            break

    if len(que) != 0:
        answer = que.popleft()
    else:
        answer = -1

    return answer
