k = int(input())

fib = [0]*(k+1)
fib[1]=1 #k=1일 때. for문 안 돈다.

#피보나치수열 활용(이전 두 수의 합)
# 0 1 1 2 3 5 ....
# k가 4인 경우 fib[4]가 b의 개수, fib[3]이 a의 개수
for i in range(2,k+1):
  fib[i] = fib[i-1] + fib[i-2]

print(fib[k-1], fib[k])
