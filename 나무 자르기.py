import sys
#get the number of trees(n), need tree's length(m)
n, m = map(int, input().split())    #나무 개수n과 필요한 길이m을 입력받음


#get the length of the trees
data=list(map(int, sys.stdin.readline().split()))    #숲에 있는 나무들의 길이를 입력받음


#시작은 0, 끝은 가장 길이가 긴 나무의 길이로 함. start is 0, end is longest tree's length
start=0
end=max(data)

result=0     #정답 초기화 answer initialization
while (start<=end):    #이진탐색 시작. binary search stsrt
  total=0    #total length of cut trees 잘린 나무들의 총합
  mid = (start+end)//2
  for x in data:
    if x>mid:
      total+= x-mid    #잘린 나무들의 길이의 총합을 구함. get the total length of cut trees
  if total<m:   #구한 총합이 요구 길이보다 작은 경우 if total is smaller than m
    end=mid-1   #end를 mid-1로 설정. set the end is mid-1
  else:   #구한 총합이 m과 같거나 작은 경우 if total is equal m or smaller than m
    result=mid    #result에 mid를 넣어줌 set the result mid 
    start=mid+1    #구한 총합이 요구보다 큰 경우 start를 mid+1로 설정. set start mid+1

print(result)
