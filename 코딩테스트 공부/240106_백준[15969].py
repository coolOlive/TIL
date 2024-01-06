# 구현/행복/브론즈2

n = int(input())
score = list(map(int, input().split()))

print(max(score)-min(score))
