import sys
input=sys.stdin.readline

# 정렬/성적 통계/실버5

k = int(input())
for i in range(k):
    arr = list(map(int,input().split()))
    arr=arr[1:]
    gap=0
    arr.sort()
    for j in range(len(arr)-1):
        gap=max(gap,arr[j+1]-arr[j])
    print('Class',i+1)
    print(f'Max {arr[-1]}, Min {arr[0]}, Largest gap {gap}')