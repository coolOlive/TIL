import sys
input=sys.stdin.readline

# 자료구조/콰트로치즈피자/실버5

n = int(input())
food = list(map(str,input().split()))
pizza = set()

for f in food:
  if len(f)>=6 and f[-6:] == 'Cheese':
    pizza.add(f)

if len(pizza)>=4:
  print('yummy')
else:
  print('sad')
