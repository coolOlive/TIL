import sys
input = sys.stdin.readline

# 자료구조,정렬/빈도 정렬/실버2

n,c = map(int,input().split())
message = list(map(int,input().split()))
cnt = dict()

for i in range(n):
    if message[i] not in cnt:
        cnt[message[i]] = [1,i]
    else:
        cnt[message[i]][0] += 1

number = [[k,v] for k,v in cnt.items()]
number.sort(key = lambda x:(-x[1][0],x[1][1]))
ans = []

for a,b in number:
    for x in range(b[0]):
        ans.append(a)

print(*ans)
