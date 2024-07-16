import sys
from collections import deque
input=sys.stdin.readline

# 자료구조/queuestack/실버3
# 시간초괃ㄷㄷㄷㄷㄷ

n = int(input())
questack = list(map(int, input().split()))
elements = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
ans = deque([])

for i in range(n):
    if questack[i] == 0:
        ans.appendleft(elements[i])
        
for i in range(m):
    ans.append(c[i])
    print(ans.popleft(), end=' ')
