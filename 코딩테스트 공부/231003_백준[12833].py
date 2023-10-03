# 수학,비트마스킹/XORXORXOR/브론즈1

a,b,c = map(int,input().split())

for i in range(c%2):
  a^=b

print(a)
