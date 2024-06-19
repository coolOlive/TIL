import sys
input=sys.stdin.readline

# 구현/부분 문자열/브론즈2

s, p = (input().strip() for _ in range(2))
print([0,1][p in s])
