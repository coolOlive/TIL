import sys
input = sys.stdin.readline

# 구현/최댓값/브론즈3
# 졸프하느라 문제 푸는거 잊고 있었다ㄷㄷ

nums = [list(map(int, input().split())) for _ in range(9)]

ans = 0
x_loca, y_loca = 0, 0

for x in range(9):
  for y in range(9):
    if ans <= nums[x][y]:
      ans = nums[x][y]
      x_loca = x + 1
      y_loca = y + 1
            

print(ans)
print(x_loca, y_loca)
