import sys
input=sys.stdin.readline

# 문자열,정렬/너의 핸들은/브론즈1

n,i = map(int,input().split())
h = [input().strip() for _ in range(n)]
h.sort()

print(h[i-1])
