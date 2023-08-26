import sys
input=sys.stdin.readline

# 문자열/팀 이름 정하기/브론즈1

green = input().strip()
n = int(input())
li = sorted([input().strip() for i in range(n)])
love = {'L':0,'O':0,'V':0,'E':0}
max_p, max_i = 0, 0

for L in love.keys():
  love[L] = green.count(L)

for i in range(n):
  L = love['L'] + li[i].count("L")
  O = love['O'] + li[i].count("O")
  V = love['V'] + li[i].count("V")
  E = love['E'] + li[i].count("E")
  p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
  if max_p < p:
    max_p = p
    max_i = i

print(li[max_i])
