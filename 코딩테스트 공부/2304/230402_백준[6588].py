import sys
input=sys.stdin.readline

# 에라토스테네스의체/골드바흐의 추측/실버1

eraNum = [1 for _ in range(1000001)]
prime = []
flg = 1

for i in range(2,1001):
  if eraNum[i]:
    prime.append(i)
    for j in range(i*2,1000001,i):
      eraNum[j] = 0

while True:
  n = int(input())
  if n == 0:
    break
  for i in range(n//2):
    if eraNum[n-prime[i]]:
      print("{} = {} + {}".format(n, prime[i], n-prime[i]))
      break
