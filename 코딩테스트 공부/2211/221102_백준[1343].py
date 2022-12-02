import sys
input=sys.stdin.readline

# 구현/폴리오미노/실버5

board=input().strip()
board=board.replace('XXXX','AAAA')
board=board.replace('XX','BB')
print(-1) if 'X' in board else print(board)