from collections import deque

# 구현,자료구조,문자열,브루트포스,해시_사이클 단어/실버4

n=int(input())
cnt=0
words=dict()

for _ in range(n):
    q=deque()
    w=input().strip()
    if w not in words:
        words[w]=0
        for i in range(len(w)):
            q.append(w[i])
        for j in range(len(w)):
            words[''.join(q)]=0
            q.rotate(-1)
        cnt+=1

print(cnt)