# 구현/나무 조각/브론즈1

tree = list(map(int, input().split()))
ans = [1,2,3,4,5]

while True:
  for i in range(len(tree)-1):
    if tree[i] > tree[i+1]:
      tree[i],tree[i+1] = tree[i+1],tree[i]
      print(*tree)

  if tree == ans:
    break
