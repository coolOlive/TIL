# 문자열,파싱/더하기 2/브론즈1

num = ''
while 1:
  try:
    num += input()
  except:
    break

print(sum(map(int, num.split(','))))
