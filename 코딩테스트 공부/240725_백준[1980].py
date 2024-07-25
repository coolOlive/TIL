# 수학,브루트포스/햄버거 사랑/실버4

a,b,t = map(int, input().split())
max_b,min_l = 0,t

for i in range(t // a+1):
  for j in range((t-i*a) // b+1):
    spent = i*a + j*b
    burgers = i +j
    leftover = t-spent

    if leftover < min_l or (leftover == min_l and burgers > max_b):
      max_b = burgers
      min_l = leftover

print(max_b, min_l)
