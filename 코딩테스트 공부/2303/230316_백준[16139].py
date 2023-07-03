import sys
input=sys.stdin.readline

# 누적합/인간-컴퓨터 상호작용/실버1
# 계속하다 결국에는 pypy로 제출함

s = input().strip()
q = int(input())
alphaCnt = [[0 for _ in range(26)] for _ in range(len(s))]

for i in range(len(s)):
    if i == 0:
        alphaCnt[i][ord(s[i])-97] = alphaCnt[i][ord(s[i])-97] + 1
        continue
    for j in range(26):
        alphaCnt[i][j] = alphaCnt[i-1][j]
    alphaCnt[i][ord(s[i])-97] += 1

for _ in range(q):
    word,l,r = input().split()
    word, l, r = ord(word)-97, int(l), int(r)
    if l > 0:
        print(alphaCnt[r][word] - alphaCnt[l-1][word])
    else:
        print(alphaCnt[r][word])
