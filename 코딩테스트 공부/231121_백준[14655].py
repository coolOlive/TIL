import sys
input = sys.stdin.readline

# 그리디/욱제는 도박쟁이야!!/실버5

n=int(input())

one=list(map(int,input().split()))
two=list(map(int,input().split()))
plays = one+two
ans = 0

for p in plays:
  ans+=abs(p)

print(ans)
