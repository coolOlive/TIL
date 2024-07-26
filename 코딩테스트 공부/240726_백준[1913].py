# 구현/달팽이/실버3

def snail(n, t):
  dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  arr = [[0] * n for _ in range(n)]
  x, y, num, dir_idx = 0, 0, n * n, 0
  target_pos = (0, 0)

  while num > 0:
    arr[x][y] = num
    if num == t:
      target_pos = (x + 1, y + 1)
    num -= 1

    nx, ny = x + dirs[dir_idx][0], y + dirs[dir_idx][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] != 0:
      dir_idx = (dir_idx + 1) % 4
      nx, ny = x + dirs[dir_idx][0], y + dirs[dir_idx][1]

    x, y = nx, ny

  return arr, target_pos

n = int(input().strip())
t = int(input().strip())

arr, target_pos = snail(n, t)

for row in arr:
  print(' '.join(map(str, row)))
print(target_pos[0], target_pos[1])
