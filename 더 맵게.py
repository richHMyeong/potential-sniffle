import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #리스트를 힙으로 바꿈
    while scoville: #힙에 원소가 존재하는 동안
        first=heapq.heappop(scoville)
        if first>=K: #처음 꺼낸 게 K이상인 경우 break
            break
        if len(scoville)==0: #다음에 꺼낼 게 존재하는지 확인
            answer=-1
            break
        second = heapq.heappop(scoville) #두 번째로 매운 거 꺼내기
        result=first+(2*second) 
        heapq.heappush(scoville, result) #계산 결과 삽입
        answer+=1 #카운트 증가
        
    return answer
