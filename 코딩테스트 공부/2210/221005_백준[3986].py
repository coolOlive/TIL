import sys
input=sys.stdin.readline

 # 스택/좋은 단어/실버4
 # 문제 이해하는데 시간이 걸렸다.

n=int(input())
word=[input().strip() for _ in range(n)]
cnt=0

for w in word:
    stack=[]
    for a in w:
        if stack and stack[-1]==a:
            stack.pop()
        else:
            stack.append(a)

    if not stack:
        cnt+=1

print(cnt)
