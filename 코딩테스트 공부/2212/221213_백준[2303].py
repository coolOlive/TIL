from itertools import combinations
import sys
input=sys.stdin.readline

# 브루트포스/숫자 게임/실버5

n = int(input())
answer = []

for i in range(n):
    cards = list(combinations(list(map(int,input().split())),3))
    score = 0
    for num in cards:
        score = max(score, sum(num)%10)
    answer.append([score,i+1])

print((max(answer)[1]))