# 브루트포스/금민수의 개수/실버1

a,b = map(int,input().split())
q = [4,7]
ans = 0

while len(q) > 1:
  num = q[0]
  q.pop(0)

  if num <= b:
    if a <= num:
      ans += 1
    q.append(num*10+4)
    q.append(num*10+7)

print(ans)
