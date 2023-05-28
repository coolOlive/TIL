# 수학/거듭제곱/실버4

n = int(input())
num = []
ans = 0

while n > 0:
  num.append(n % 2)
  n //= 2

for i in range(len(num)):
  if num[i] == 1:
    ans += 3 ** i
        
print(ans)
