# 그리디,정렬,수학_로프/실버4

n=int(input())
maximum=sorted([int(input()) for _ in range(n)],reverse=True)
w=[maximum[i]*(i+1) for i in range(n)]
print(max(w))