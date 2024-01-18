# 구현/피터팬 프레임/실버5

word = input()
ans = ['.', '.', '#', '.', '.']

for i in range(len(word)):
  praim = '#'
  if (i+1)%3==0:
    praim = '*'
    ans[2] = ans[2][:-1]+praim
  ans[0] += f'.{praim}..'
  ans[1] += f'{praim}.{praim}.'
  ans[2] += f'.{word[i]}.{praim}'
  ans[3] += f'{praim}.{praim}.'
  ans[4] += f'.{praim}..'

for line in ans:
  print(line)
