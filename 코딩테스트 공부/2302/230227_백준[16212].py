import sys
input=sys.stdin.readline

# 정렬/정열적인 정렬/실버5

n = int(input())
ans = list(map(int,input().split()))
ans.sort()
print(*ans)
