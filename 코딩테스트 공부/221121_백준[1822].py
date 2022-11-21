import sys
input=sys.stdin.readline

# 자료구조/차집합/실버4

n = map(int, input().split())

a =set(map(int, input().split()))
b = set(map(int, input().split()))

minus = sorted(a-b)
print(len(minus))

if len(minus):
    print(*sorted(minus))