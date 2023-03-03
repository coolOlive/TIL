import sys
input=sys.stdin.readline

# 구현,그리디/사과 담기 게임/실버5

n, m = map(int, input().split())
j = int(input())

start = 1
end = m
distance = 0

for _ in range(j):
    loca = int(input())

    if loca < start:
        distance += (start - loca)
        start = loca
        end = loca + m - 1

    elif loca > end:
        distance += (loca - end)
        end = loca
        start = end - m + 1

print(distance)
