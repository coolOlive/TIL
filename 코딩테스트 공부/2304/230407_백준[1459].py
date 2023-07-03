# 수학,조건분기/걷기/실버4

x, y, w, s = map(int, input().split())
small,large = min(x,y),max(x,y)

tmp1 = (x+y)*w

if (x+y)%2==0:
  tmp2 = large*s
else:
  tmp2 = (large-1)*s+w

tmp3 = (small*s) + (abs(x-y)*w)

print(min(tmp1,tmp2,tmp3))
