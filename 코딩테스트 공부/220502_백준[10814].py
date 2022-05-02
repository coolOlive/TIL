import sys
input=sys.stdin.readline

# 정렬_나이순 정렬/실버5

n=int(input())
arr=[]
for _ in range(n):
    data=list(input().split())
    a=int(data[0])
    b=data[1]
    arr.append([a,b])

arr.sort(key=lambda x:(x[0]))

for i in range(n):
    print(arr[i][0],arr[i][1])