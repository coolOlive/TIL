import sys
input = sys.stdin.readline

# 문자열/민균이의 비밀번호/브론즈1

n = int(input())
pw = [input().strip() for _ in range(n)]

for p in pw:
  if p[::-1] in pw:
    L = len(p)
    mid = L//2
    print(L,p[mid])
    break
