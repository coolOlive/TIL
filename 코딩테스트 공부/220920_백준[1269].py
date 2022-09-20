import sys
input=sys.stdin.readline

 # 자료구조/대칭 차집합/실버4

n,m=map(int,input().split())

a=set(map(int,input().split()))
b=set(map(int,input().split()))


print(len(a-b)+len(b-a))