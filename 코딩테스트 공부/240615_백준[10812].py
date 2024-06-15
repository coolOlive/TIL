import sys
input=sys.stdin.readline

# 구현/바구니 순서 바꾸기 /브론즈2

n,m = map(int,input().split())
box = [i+1 for i in range(n)]

for _ in range(m):
  i,j,k = map(int, input().split())
  box = box[:i-1]+box[k-1:j]+box[i-1:k-1]+box[j:]

print(*box)
