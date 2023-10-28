# 구현/그릇/브론즈2

dish = ['*']+list(input())
ans = 0

for i in range(1,len(dish)):
  if dish[i] == dish[i-1]:
    ans += 5
    continue
  ans += 10
        
print(ans)
