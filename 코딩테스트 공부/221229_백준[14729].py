import sys
input=sys.stdin.readline

# 정렬/칠무해/실버5
# heapq를 쓰면 더 빨리 할 수 있는듯.

n = int(input())
score = [float(input()) for _ in range(n)]
score.sort()

for i in range(7):
    print('{:.3f}'.format(score[i]))