import sys
input=sys.stdin.readline

# 구현/소가 길을 건너간 이유 1/브론즈1
# 오늘은 우테코 최종 코테에 다녀왔다.

n = int(input())
cow = [-1]*11
ans=0

for _ in range(n):
    eachcow,location = map(int,input().split())
    if cow[eachcow-1] == -1:
        cow[eachcow-1] = location
    elif cow[eachcow-1] != location:
        cow[eachcow-1] = location
        ans+=1

print(ans)
