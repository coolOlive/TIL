# 정렬/커트라인/브론즈2

n,k = map(int,input().split())
score = list(map(int,input().split()))
score.sort(reverse = True)
ans = score[:k]

print(ans[-1])
