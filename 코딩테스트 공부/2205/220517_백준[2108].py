import sys
from collections import Counter
input=sys.stdin.readline

# 수학,구현,정렬_통계학/실버3

n=int(input())

num=list(sorted(int(input()) for _ in range(n)))

print(round(sum(num)/n))
print(num[n//2])

cnt=Counter(num).most_common()
if len(cnt)>1 and cnt[0][1]==cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(num[-1]-num[0])