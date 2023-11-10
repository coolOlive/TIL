# 구현/화성 수학/브론즈2

t = int(input())

for _ in range(t):
  ques = list(map(str, input().split()))
  ans = float(ques[0])
  for i in range(1,len(ques)):
    if ques[i] == '@':
      ans*=3
      continue
    if ques[i] == '%':
      ans += 5
      continue
    ans -= 7
  print("%0.2f" % ans)
