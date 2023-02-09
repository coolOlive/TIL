import sys
input = sys.stdin.readline
from itertools import permutations

# 조합,자료구조/카드 놓기/실버4
# 재귀함수로도 풀어보려했지만,, 잘 안됨 코드 한 줄씩 다시 보자

n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]
per = list(permutations(cards,k))
ans = set()

for word in per:
    ans.add(''.join(word))

print(len(ans))
