from itertools import combinations

# 브루트포스,조합/복권/실버4

n, m, k = map(int,input().split())
lottos = [*combinations([i for i in range(n)], m)]
win,cnt = 0,0

for lotto in lottos:
    for jimin in lottos:
        cnt += 1
        if len(set(lotto)&set(jimin)) >= k:
            win += 1

print(win/cnt)
