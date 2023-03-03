import re
import sys
input=sys.stdin.readline

# 문자열,파싱,정렬/수학숙제/실버4

n = int(input())
words = [input().strip() for _ in range(n)]
ans = []
pattern = re.compile('\d+')

for i in range(n):
    nums = pattern.findall(words[i])
    for num in nums:
        ans.append(int(num))

ans.sort()
for i in ans:
    print(i)
