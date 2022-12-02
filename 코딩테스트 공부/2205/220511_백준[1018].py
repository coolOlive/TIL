import sys
input=sys.stdin.readline

# 브루트포스_체스판 다시 칠하기/실버5

n,m=map(int,input().split())

b_line=[j for i in range(4) for j in ('B''W')]
w_line=[j for i in range(4) for j in ('W''B')]

b_bord=[]
w_bord=[]

for _ in range(4):
    b_bord.append(b_line)
    b_bord.append(w_line)
    w_bord.append(w_line)
    w_bord.append(b_line)

input_board = []
for i in range(n):
    input_board.append(list(input().strip()))

b_cnt,w_cnt=401,401
for i in range(n-7):
    for j in range(m-7):
        b_change=0
        w_change=0
        for a in range(8):
            for b in range(8):
                if input_board[i+a][j+b] != b_bord[a][b]:
                    b_change+=1
                if input_board[i+a][j+b] != w_bord[a][b]:
                    w_change+=1
        if b_change<=b_cnt:
            b_cnt=b_change
        if w_change<=w_cnt:
            w_cnt=w_change

print(b_cnt) if b_cnt<w_cnt else print(w_cnt)
