# 그리디/세탁소 사장 동혁/브론즈3

n = int(input())
coin = [25, 10, 5, 1]

for _ in range(n):
	money = int(input())
	for c in coin:
		print(money//c, end=' ')
		money = money%c
