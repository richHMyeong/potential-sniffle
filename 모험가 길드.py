# 입력받기
n = int(input())
fear = list(map(int, input().split()))
#print(fear)
fear.sort() # 오름차순 정렬. [1,2,2,2,3]

cnt=0 # 한 그룹 내 인원 수
result=0 # 그룹의 수
for i in fear:
    cnt+=1
    if cnt>=i: # 그룹 내 인원수가 현재 공포도보다 크거나 같다면 
        result+=1
        cnt=0
print(result)
