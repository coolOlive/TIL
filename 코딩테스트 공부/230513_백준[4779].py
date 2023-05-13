import sys
input = sys.stdin.readline

# 재귀/칸토어 집합/실버3

while 1:
  try:
    n = int(input().strip())
    if n=='':
      break
    tmp = '-'
    for j in range(n):
      tmp = tmp+' '*len(tmp)+tmp
    print(tmp)
  except:
    break
