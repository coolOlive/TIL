import sys
input=sys.stdin.readline
from itertools import combinations

# 조합,브루트포스/부분수열의 합/실버2
# 백트래킹 공부를 해야겠다.

n,s = map(int,input().split())
nums = list(map(int,input().split()))
ans = 0

for i in range(1,n+1):
    combi = list(combinations(nums,i))
    for com in combi:
        if sum(com) == s:
            ans += 1

print(ans)
