import sys
input=sys.stdin.readline

# 문자열, 정렬_단어 정렬/실버5

n=int(input())
word=list(set([input().strip() for _ in range(n)]))
word.sort(key=lambda x:(len(x),x))

for a in word:
    print(a)