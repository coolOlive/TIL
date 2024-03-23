# DP/N으로 표현/L3

def solution(n, number):
  ans = -1
  dp = []

  for i in range(1,9):
    nSet = set()
    now = int(str(n)*i)
    nSet.add(now)

    for j in range(i-1):
      for a in dp[j]:
        for b in dp[-j-1]:
          nSet.add(a+b)
          nSet.add(a-b)
          nSet.add(a*b)
          if b != 0:
            nSet.add(a//b)
    if number in nSet:
      ans = i
      break

    dp.append(nSet)

  return ans