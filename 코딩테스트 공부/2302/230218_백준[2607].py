import sys
input=sys.stdin.readline

# 구현,문자열/비슷한 단어/실버3

n = int(input())
tmp = list(input().strip())
ans = 0

for _ in range(n-1):
    word = tmp[:]
    word2 = input().strip()
    cnt = 0

    for w in word2:
        if w in word:
            word.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(word) < 2:
        ans += 1

print(ans)
