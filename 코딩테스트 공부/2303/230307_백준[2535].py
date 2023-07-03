import sys
input=sys.stdin.readline

# 정렬/아시아 정보올림피아드/실버5

n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]

students = sorted(students, key = lambda x: -x[2])
cnt = [0]*(n+1)

print(*students[0][:2])
print(*students[1][:2])
cnt[students[0][0]] += 1
cnt[students[1][0]] += 1

for i in range(2,n+1):
    if cnt[students[i][0]] < 2:
        print(*students[i][:2])
        break
