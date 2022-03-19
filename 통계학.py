import collections

#입력
n = int(input())
data=[]
for i in range(n):
  data.append(int(input()))

#첫 번째 조건 출력
print(round(sum(data)/n))

#두 번째 조건
data.sort()
print(data[n//2])

#세 번째 조건
dict=collections.Counter(data)
key= list(dict.keys())
val = list(dict.values())
sorted_dict=sorted(dict.items(), key=lambda item: item[1], reverse = True)
if len(data)==1:
  print(data[0])
elif sorted_dict[0][1]==sorted_dict[1][1]:
  print(sorted_dict[1][0])
else:
  print(sorted_dict[0][0])

#네 번째 조건
print(data[n-1]-data[0])


