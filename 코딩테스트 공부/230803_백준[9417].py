# 유클리드호제법/최대 GCD/실버4

t = int(input())

def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b,a%b)

for _ in range(t):
  nums = sorted(list(map(int,input().split())))
  ans = [1]
  for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
      ans.append(gcd(nums[i],nums[j]))
  print(max(ans))
