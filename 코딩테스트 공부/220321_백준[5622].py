import sys
input=sys.stdin.readline

s = input()
str_list=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
time = 0

for a in s:
    for i in str_list:
        if a in i:
            time+=str_list.index(i)+3

print(time)
