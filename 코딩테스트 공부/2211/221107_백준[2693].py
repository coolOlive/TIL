import sys
input=sys.stdin.readline

# 정렬/N번째 큰 수/브론즈1

t=int(input())

for _ in range(t):
    nums=sorted(list(map(int,input().split())))
    print(nums[-3])