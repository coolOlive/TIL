import sys
input=sys.stdin.readline
from itertools import permutations

# 순열,그리디/숫자 야구/실버3

n = int(input())
ans = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3))

for _ in range(n):
    num,strik,ball = map(int,input().split())
    num = list(map(int, str(num)))
    remove = 0
    for i in range(len(ans)):
        s=b=0
        i-=remove
        for j in range(3):
            if ans[i][j]==num[j]:
                s+=1
            elif num[j] in ans[i]:
                b+=1
        if s!=strik or b!=ball:
            ans.remove(ans[i])
            remove+=1
            
print(len(ans))