import sys
input=sys.stdin.readline

# 구현/치킨 쿠폰/브론즈2

while 1:
  try:
    n,k = map(int, input().split())
    ans = n
    
    while (n//k) != 0:
      ans += n//k
      n = (n//k) + (n%k)
    print(ans)

  except:
    break
