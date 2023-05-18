import sys
input = sys.stdin.readline

# 그리디/Byte Coin/실버4

n,w  = map(int,input().split())
price = [0]+[int(input().strip()) for _ in range(n)]+[0]
price[0] = price[1]
coin = 0

if n>1:
  price[-1] = price[-2]


for i in range(1,n+1):
##    최저점
  if price[i-1]>=price[i]<price[i+1]:
    coin += w//price[i]
    w %= price[i]
        
##    최고점
  elif price[i-1]< price[i] >= price[i+1]:
    w += coin*price[i]
    coin = 0

print(w)
