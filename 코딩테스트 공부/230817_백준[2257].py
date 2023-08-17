import sys
input=sys.stdin.readline

# 스택/화학식량/실버2

word = list(map(str,input().strip()))
atom = {"H": 1, "C": 12, "O": 16}
stack = []

for i in word:
  if i == "(":
    stack.append(i)
  elif i == ")":
    check = 0

    while 1:
      target = stack.pop()
      if target == "(":
        break
      check += target
    stack.append(check)

  elif i in atom:
    stack.append(atom[i])
  else:
    stack[-1] *= int(i)

print(sum(stack))
