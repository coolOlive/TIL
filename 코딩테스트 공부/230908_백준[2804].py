# 구현,문자열/크로스워드 만들기/브론즈1

a,b = input().split()
n,m = len(a),len(b)
line,left,right = 0,0,0
ans = []

for i in range(n):
  if a[i] in b:
    left = i
    line = b.index(a[i])
    right = n-left-1
    break

for i in range(m):
  ans.append('.'*left+b[i]+'.'*right)

ans[line] = a

print(*ans,sep = '\n')
