s = input()

prev=s[0]
cnt=0
for i in range(1, len(s)):
    if prev!=s[i]:
        cnt+=1
        prev=s[i]

answer = cnt//2 + cnt%2

print(answer)
