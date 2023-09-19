# 브루트포스,수학/0의 개수/브론즈1

t = int(input())
nums = []

for _ in range(t):
  a,b = map(int,input().split())
  nums.append(a)
  nums.append(b)

small = min(nums)
large = max(nums)
zero = [0]*(large+1)


for i in range(small,large+1):
  zero[i] = str(i).count('0')

for i in range(0,t*2,2):
  print(sum(zero[nums[i]:nums[i+1]+1]))
