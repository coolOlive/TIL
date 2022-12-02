# 정렬,값/좌표압축_좌표 압축/실버2

n=int(input())
xy=list(map(int,input().split()))
xy_tmp=sorted(list(set(xy)),reverse=True)

dic=dict()
cnt=0
while xy_tmp:
    dic[xy_tmp[-1]]=cnt
    xy_tmp.pop()
    cnt+=1

for a in xy:
    print(dic[a],end=' ')
