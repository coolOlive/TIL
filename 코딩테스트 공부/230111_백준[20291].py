import sys
input=sys.stdin.readline

# 정렬,해시,문자열/파일 정리/실버3

n = int(input())

file = dict()
name = []
for _ in range(n):
    a,b = map(str,input().strip().split('.'))
    if b in file:
        file[b] += 1
    else:
        file[b] = 1
        name.append(b)

name.sort()

for file_ex in name:
    print(file_ex,file[file_ex])
