from sys import stdin

n=int(stdin.readline()) #n 입력받기
answer=0 #정답으로 출력할 변수

while n>=0: #n이 0보다 큰 동안 
  if n%5==0: #5로 나눠지면 출력하고 break
    answer+=(n//5)
    print(answer)
    break
  #그렇지 않을 경우 n에서 3을 빼고 answer에 1을 더해줌
  n-=3
  answer+=1

else: #while문이 false가 된 경우(나누어 떨어지지 않은 경우) -1 출력
  print(-1)
