# 수학/나머지와 몫이 같은 수/브론즈1

n = int(input())
ans = 0

for i in range(1,n):
  ans += n*i+i
    
print(ans)
