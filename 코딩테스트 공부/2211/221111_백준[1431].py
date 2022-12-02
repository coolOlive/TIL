import sys
input=sys.stdin.readline

# 정렬/시리얼 번호/실버3

n = int(input())
arr = []

def hap(inputs):
    result = 0
    for a in inputs:
        if a.isdigit():
            result+=int(a)
    return result

for i in range(n):
    tmp = input().strip()
    arr.append(tmp)

arr.sort(key = lambda x:(len(x), hap(x), x))
for ans in arr:
    print(ans)