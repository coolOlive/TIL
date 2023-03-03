import sys
input=sys.stdin.readline

# 해시,자료구조/배부른 마라토너/실버4

n = int(input())
name = dict()

for _ in range(n):
    a = input().strip()
    if a in name:
        name[a] += 1
    else:
        name[a] = 1

for i in range(n-1):
    b = input().strip()
    name[b] -= 1
    if name[b] == 0:
        name.pop(b)
        
print(list(name.keys())[0])
