import sys
input = sys.stdin.readline

# 정렬,수학,그리디/카우버거/실버5

b,c,d = map(int, input().split())

burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

ans = 0
mini = min(b, c, d)

for i in range(mini) :
  ans += (burger[i] + side[i] + drink[i]) * 0.9

ans += (sum(burger[mini::])+sum(side[mini::])+sum(drink[mini::]))

print(sum(burger) + sum(side) + sum(drink))
print(int(ans))
