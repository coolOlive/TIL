# 구현/오르막길/브론즈1

n = int(input())

road = list(map(int,input().split()))
tmp = []
size = 0

for i in range(n-1):
    if road[i] < road[i+1]:
        size += road[i+1] - road[i]
    else:
        tmp.append(size)
        size = 0
        
tmp.append(size)
print(max(tmp))