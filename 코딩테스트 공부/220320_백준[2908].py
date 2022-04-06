import sys
input=sys.stdin.readline

# 상수/브론즈2

a, b=map(str,input().split())

# 문자열 뒤집기
a=int(a[::-1])
b=int(b[::-1])

# 파이썬 삼항연산식
print(a) if a>b else print(b)