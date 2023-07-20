# 그리디/팔/실버1

l,r = map(str,input().split())
ll,rl = len(l),len(r)
ans = 0

if ll != rl:
  print(ans)
else:
  for i in range(ll):
    if l[i] == r[i]:
      if l[i] == '8':
        ans += 1
    else:
      break
  
  print(ans)
