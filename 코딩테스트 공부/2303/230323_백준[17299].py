from collections import Counter
import sys
input=sys.stdin.readline

# 스택/오등큰수/골드3

n = int(input())
nums = list(map(int,input().split()))
ans = [-1]*n
stack = [0]
cnt = Counter(nums)

for i in range(n):
    while stack and cnt[nums[i]] > cnt[nums[stack[-1]]]:
        ans[stack.pop()]=nums[i]
    stack.append(i)

print(*ans)
