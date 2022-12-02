import sys
input=sys.stdin.readline

# 분할정복,재귀_색종이 만들기/실버3

n=int(input().strip())
paper=[list(map(int,input().split())) for _ in range(n)]
white=0
blue=0

def cut(x,y,n):
    global white, blue
    same=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if same!= paper[i][j]:
                cut(x,y,n//2)
                cut(x+n//2,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y+n//2,n//2)
                return        
    if same==0:
        white+=1
    else:
        blue+=1
        
cut(0,0,n)
print(white)
print(blue)