import sys
input=sys.stdin.readline

# 정렬,이분탐색/먹을 것인가 먹힐 것인가/실버3
# 생각보다 오래 걸렸다..

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    cnt = 0
    ans = 0
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()

    for i in range(n):
        while 1:
            if cnt == m or a[i] <= b[cnt]:
                ans += cnt
                break
            else:
                cnt += 1

    print(ans)