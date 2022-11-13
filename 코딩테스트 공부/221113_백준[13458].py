import sys
input = sys.stdin.readline

# 수학/시험 감독/브론즈2
# 일단 쉬운거 먼저 올린다.

n = int(input())
arr = list(map(int,input().split()))
master,sub = map(int,input().split())

ans=n

for i in range(n):
    arr[i] -= master
    if arr[i] > 0:
        if arr[i]%sub > 0:
            ans += (arr[i]//sub)+1
        else:
            ans += arr[i]//sub

print(ans)