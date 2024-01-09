# 구현,문자열,브루트포스/수학은 체육과목 입니다 3/실버4

s = input()
sLen = 1

while sLen <=3:
  sNumber = s[:sLen]
  nextCheck = int(sNumber)

  while len(s)>len(sNumber):
    nextCheck += 1
    sNumber += str(nextCheck)

  if s == sNumber:
    print(s[:sLen],nextCheck)
    break

  sLen += 1
