from itertools import combinations
import sys
input=sys.stdin.readline

# 브루트포스,조합/한윤정이 이탈리아에 가서 아이스크림을 사먹는데/실버5

n,m = map(int,input().split())
icecream = [[0 for _ in range(n)] for __ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    icecream[a-1][b-1]=1
    icecream[b-1][a-1]=1
    
ans=0

for i in combinations(range(n),3):
    if icecream[i[0]][i[1]] or icecream[i[0]][i[2]] or icecream[i[1]][i[2]]:
        continue
    ans += 1
print(ans)