import sys
input=sys.stdin.readline

# 정렬_국영수/실버4

n=int(input())
student=[list(input().split()) for _ in range(n)]

student.sort(key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for s in student:
    print(s[0])