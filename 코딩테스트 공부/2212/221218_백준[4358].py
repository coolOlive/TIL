import sys
input=sys.stdin.readline

# 자료구조/생태학/실버2

treeName = []
trees = dict()
count = 0

while True:
    tree = input().strip()
    if tree == '':
        break
    count += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
        treeName.append(tree)

treeName.sort()

for i in range(len(treeName)):
    name = treeName[i]
    print(name ,'%.4f' %(trees[name] /count * 100))