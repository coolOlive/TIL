from itertools import permutations
import sys
input=sys.stdin.readline

# 브루트포스,순열/차이를 최대로/실버2

n=int(input())
nums=map(int,input().split())

perm=permutations(nums)
ans=0
 
for p in perm:
    tmp=0
    for i in range(len(p)-1):
        tmp += abs(p[i]-p[i+1])
    ans=max(tmp,ans)
 
print(ans)