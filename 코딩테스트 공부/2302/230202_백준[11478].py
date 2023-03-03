import sys
input=sys.stdin.readline

# 자료구조/서로 다른 부분 문자열의 개수/실버3

s = input().strip()
sLength = len(s)
ans = set()

for i in range(sLength):
    for j in range(i,sLength):
        ans.add(s[i:j+1])

print(len(ans))
