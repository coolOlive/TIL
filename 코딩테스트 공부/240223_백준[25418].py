# DP,수학/정수 a를 k로 만들기/실버3

a,k = map(int,input().split())
ans = 0

while a<=k//2:
  ans += (k&1)+1
  k //= 2

print(ans+k-a)
