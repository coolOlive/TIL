import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

# 자료구조,분리집합/집합의 표현/골드5
# 어려웠어..

n,m = map(int,input().split())
nums = [i for i in range(n+1)]

def search(x):
    if nums[x] == x:
        return x
    nums[x] = search(nums[x])
    return nums[x]

def union(a,b):
    a,b = search(a),search(b)
    nums[a] = b
    return

for _ in range(m):
    tmp,a,b = map(int,input().split())
    if tmp == 0:
        union(a,b)
    else:
        if search(a) == search(b):
            print('YES')
        else:
            print('NO')
