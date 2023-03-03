import sys
input=sys.stdin.readline

# 정렬,그리디/소가 길을 건너간 이유 3/실버4

n = int(input())
cow = []
for _ in range(n):
    a,b = map(int,input().split())
    cow.append([a,b])
cow.sort()
 
time = 0
for i in range(n):
    arrive, cost = cow[i]
    if time < arrive:
        time = arrive
    time += cost

print(time)