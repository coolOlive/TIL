# 그리디/컵홀더/브론즈1

n = int(input())
seat = input()

cnt = seat.count('LL')

if (cnt <= 1):
  print(len(seat))
else:
  print(len(seat) - cnt + 1)
