import sys
input=sys.stdin.readline

# 구현/Yangjojang of The Year/브론즈1
# 너무 피곤해서.. 이걸 풀었다... 브론즈라니

t = int(input())

for _ in range(t):
    n = int(input())
    rank = 0
    ans = ''
    for _ in range(n):
        school, drink = input().split()
        drink = int(drink)
        if(drink > rank):
            rank = drink
            ans = school
    print(ans)
