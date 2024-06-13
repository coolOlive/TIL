import sys
input=sys.stdin.readline

# 구현/콘테스트/브론즈2

w = [int(input()) for _ in range(10)]
k = [int(input()) for _ in range(10)]
w.sort(reverse=True)
k.sort(reverse=True)

print(sum(w[:3]), sum(k[:3]))
