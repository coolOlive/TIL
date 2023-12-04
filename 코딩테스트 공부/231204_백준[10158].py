# 수학,애드혹/개미/실버3

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

if ((p + t) // w) % 2 == 0:
  print((p + t) % w,end = ' ')
else:
  print(w - (p + t) % w,end = ' ')

if ((q + t) // h) % 2 == 0:
  print((q + t) % h)
else:
  print(h - (q + t) % h)
