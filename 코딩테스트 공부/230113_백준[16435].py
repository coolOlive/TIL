import sys
input=sys.stdin.readline

# 정렬,그리디/스네이크버드/실버5

n,l = map(int,input().split())
height = list(map(int,input().split()))
height.sort()

for i in range(n):
    if height[i] <= l:
        l += 1
        continue
    break

print(l)
