import sys
input=sys.stdin.readline

# 구현,문자열/세로읽기/브론즈1

words=[input().strip() for _ in range(5)]

for i in range(15):
    for j in range(5):
        if i<len(words[j]):
            print(words[j][i],end='')