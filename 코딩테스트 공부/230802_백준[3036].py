# 유클리드호제법/링/실버4

n = int(input())
ring = list(map(int, input().split()))

def gcd(a, b):
  if b==0:
    return a
  return gcd(b,a%b)

for i in range(1, n):
  tmp = gcd(ring[0], ring[i])
  print('{0}/{1}'.format(ring[0]//tmp, ring[i]//tmp))
