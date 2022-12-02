import sys
input=sys.stdin.readline

# 정렬,문자열/생일/실버5

n=int(input())
info=[]
for _ in range(n):
    name,day,month,year=map(str,input().split())
    info.append([int(year),int(month),int(day),name])
    
info.sort()
print(info[-1][3])
print(info[0][3])