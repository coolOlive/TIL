import sys
input=sys.stdin.readline

# 브루트포스,문자열/반지/실버5

findString = input().strip()
n = int(input())
ans = 0

for i in range(n):
    words = input().strip()
    words += words
    if words.find(findString) != -1:
        ans +=1

print(ans)