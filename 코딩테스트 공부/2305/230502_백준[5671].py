import sys
input = sys.stdin.readline

# 브루트포스/호텔 방 번호/실버5
# 다른거 풀다가 시간안에 출책하려 급하게 함

while 1:
  try:
    n, m = map(int, input().split())
  except:
    break
  ans = 0
  for num in range(n,m+1):
    cnt = set()
    s_num = str(num)
    for char in s_num:
      cnt.add(char)
    if len(s_num) == len(cnt):
      ans += 1
  print(ans)
