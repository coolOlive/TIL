# 수학,그리디/물병/실버1

n,k = map(int, input().split())
ans = 0;

while bin(n).count('1') > k:
  n += 1
  ans += 1

print(ans)
