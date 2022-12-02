import sys
input=sys.stdin.readline

 # 정렬/중복 빼고 정렬하기/실버5

n=int(input())
num=sorted(list(set(map(int,input().split()))))
print(' '.join(map(str,num)))