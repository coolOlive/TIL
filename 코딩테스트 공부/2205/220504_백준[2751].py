import sys
input=sys.stdin.readline

# 정렬_수 정렬하기/실버5

n=int(input())
arr=[int(input()) for _ in range(n)]

for a in sorted(arr):
    print(a)