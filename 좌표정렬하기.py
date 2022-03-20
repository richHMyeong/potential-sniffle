n = int(input())
arr=[]

for i in range(n):
  input_data=input().split()
  arr.append((int(input_data[0]), int(input_data[1])))

arr=sorted(arr, key=lambda x: (x[0], x[1]))

for i in range(n):
  print(arr[i][0], arr[i][1])
