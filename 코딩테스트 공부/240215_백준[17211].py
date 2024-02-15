# 수학/좋은 날 싫은 날/실버5

n,emotion = map(int,input().split())
oo,ox,xo,xx = map(float,input().split())

oCnt = [0]*n
xCnt = [0]*n

if emotion == 0:
  oCnt[0] = oo
  xCnt[0] = ox
else:
  oCnt[0] = xo
  xCnt[0] = xx

for i in range(1,n):
  oCnt[i] = oCnt[i-1]*oo+xCnt[i-1]*xo
  xCnt[i] = oCnt[i-1]*ox+xCnt[i-1]*xx

print(round(oCnt[n-1]*1000))
print(round(xCnt[n-1]*1000))
