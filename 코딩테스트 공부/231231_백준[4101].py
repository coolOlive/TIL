# 구현/크냐?/브론즈5

while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  if a > b:
    print("Yes")
  else:
    print("No")
