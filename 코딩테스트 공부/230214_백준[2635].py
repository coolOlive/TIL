# 브루트포스/수 이어가기/실버5

n = int(input())
ans = []

for i in range(1,n+1):
    first = [n,i]
    idx = 1
    while 1:
        last = first[idx-1] - first[idx]
        if last < 0:
            break
        first.append(last)
        idx += 1

    if len(ans) < len(first):
        ans = first

print(len(ans))
print(*ans)
