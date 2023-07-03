import sys
input=sys.stdin.readline

# dp,lis/가장 긴 바이토닉 부분 수열/골드4

n=int(input())
nums=list(map(int,input().split()))
dpUp = [1]*n
dpDown = [1]*n
ans = 0

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dpUp[i]=max(dpUp[i],dpUp[j]+1)
nums.reverse()
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dpDown[i]=max(dpDown[i],dpDown[j]+1)

for i in range(n):
    ans = max(ans,dpUp[i]+dpDown[n-i-1])

print(ans-1)
