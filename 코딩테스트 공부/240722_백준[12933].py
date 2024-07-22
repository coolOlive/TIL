# 구현/오리/실버2

def duckduck(sound):
  quack = 'quack'
  stages = [0 for _ in range(5)]
  nowCnt, maxCnt = 0, 0

  for s in sound:
    if s not in quack:
      return -1
    idx = quack.index(s)

    if idx == 0:
      if stages[4] > 0:
        stages[4] -= 1
      else:
        nowCnt += 1
        maxCnt = max(maxCnt, nowCnt)
      stages[0] += 1
    else:
      if stages[idx - 1] == 0:
        return -1
      stages[idx - 1] -= 1
      stages[idx] += 1

      if idx == 4:
        stages[4] -= 1
        nowCnt -= 1

  if any(stages):
    return -1

  return maxCnt

# 입력 받기
sound = input().strip()
ans = duckduck(sound)
print(ans)
