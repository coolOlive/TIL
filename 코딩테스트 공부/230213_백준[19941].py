import sys
input=sys.stdin.readline

# 그리디/햄버거 분배/실버3

n,k = map(int, input().split())
arr = list(input().strip())
ans = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(max(i-k,0), min(i+k+1,n)):
            if arr[j] == 'H':
                arr[j] = 0
                ans += 1
                break

print(ans)
