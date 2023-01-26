import sys
input=sys.stdin.readline

# 정렬,문자열,트리/접두사/실버2
# 트리..?

n = int(input())
words = [input().strip() for _ in range(n)]
words.sort(key = len)
ans = len(words)

for i in range(n):
    for j in range(i+1,n):
        if words[i] == words[j][:len(words[i])]:
            ans -= 1
            break
        
print(ans)
