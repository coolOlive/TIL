# 정렬,수학/안테나/실버3

n = int(input())
house = list(map(int,input().split()))
house.sort()
print(house[(n-1)//2])
