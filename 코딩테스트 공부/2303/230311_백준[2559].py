import sys
input = sys.stdin.readline

# 누적합,슬라이딩윈도우/수열/실버3

n, k = map(int,input().split())
weather = list(map(int, input().split()))

ans = [sum(weather[:k])]

for i in range(n - k):
    ans.append(ans[i] - weather[i] + weather[k+i])
        
print(max(ans))
