from itertools import combinations_with_replacement

# 조합,브루트포스/로마 숫자 만들기/실버3
# 중복 조합하는 법을 알게됨

n = int(input())
rome = [1,5,10,50]
alphaList = combinations_with_replacement(rome, n)
ans = set()

for alpha in alphaList:
    ans.add(sum(alpha))

print(len(ans))
