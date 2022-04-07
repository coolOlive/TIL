# 수 찾기/실버4 (1. 이진탐색 & 2. set 사용)

#1. 이진탐색법 _시간복잡도: O(logN)
n=int(input())
a=sorted(list(map(int,input().split())))

m=int(input())
x=list(map(int,input().split()))

def binary(i,x,start,end):
    if start>end:
        return 0
    mid=(start+end)//2
    if i==a[mid]:
        return 1
    elif i < a[mid]:
        end=mid-1
        return binary(i,x,start,end)
    else:
        start=mid+1
        return binary(i,x,start,end)

for i in x:
    print(binary(i,x,0,n-1))

'''
# 2. set 사용법_ set의 시간복잡도 : O(1)

n=int(input())
a=set(list(map(int,input().split())))

m=int(input())
x=list(map(int,input().split()))

for i in x:
    if i in a:
        print(1)
    else:
        print(0)
'''