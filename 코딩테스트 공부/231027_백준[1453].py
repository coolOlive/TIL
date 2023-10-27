# 구현/피시방 알바/브론즈2

n = int(input())
user = list(map(int, input().split()))
want = len(set(user))

print(n-want)
