# 재귀함수 사용
def facto(n):
    if n>1:
        return n*facto(n-1)
    else:
        return 1

n=int(input())
print(facto(n))