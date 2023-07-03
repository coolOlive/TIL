import sys
input=sys.stdin.readline

# 구현/직사각형 네개의 합집합의 면적 구하기/브론즈1

box = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            box[i][j] = 1

answer = 0
for line in box:
    answer += sum(line)
print(answer)
