n = input()

mid = len(n)//2
# print(mid)

left = n[:mid]
right = n[mid:]

left_sum=0
right_sum=0
for l, r in zip(left, right):
    left_sum+=int(l)
    right_sum+=int(r)
# print(left_sum, right_sum)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
