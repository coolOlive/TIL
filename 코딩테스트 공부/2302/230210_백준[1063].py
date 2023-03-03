import sys
input = sys.stdin.readline

# 구현/킹/실버3
# 딕셔너리로 풀면 더 짧게 할 수 있는듯

king,rock,n = map(str,input().split())
king = [ord(king[0]),int(king[1:])]
rock = [ord(rock[0]),int(rock[1:])]
n = int(n)

def boardCheck(a,b,c,d):
    if a<65 or a>72 or b<1 or b>8:
        return False
    if c<65 or c>72 or d<1 or d>8:
        return False
    return True

def kingRock(ktmp,rtmp,x,y):
    if ktmp == rtmp:
        return [rtmp[0]+x,rtmp[1]+y]
    return rtmp

def move(m):
    global king
    global rock
    kingtmp = king
    rocktmp = rock
    if m == 'R':
        kingtmp = [kingtmp[0]+1,kingtmp[1]]
        rocktmp = kingRock(kingtmp,rocktmp,1,0)
    elif m == 'L':
        kingtmp = [kingtmp[0]-1,kingtmp[1]]
        rocktmp = kingRock(kingtmp,rocktmp,-1,0)
    elif m == 'B':
        kingtmp = [kingtmp[0],kingtmp[1]-1]
        rocktmp = kingRock(kingtmp,rocktmp,0,-1)
    elif m == 'T':
        kingtmp = [kingtmp[0],kingtmp[1]+1]
        rocktmp = kingRock(kingtmp,rocktmp,0,1)
    elif m == 'RT':
        kingtmp = [kingtmp[0]+1,kingtmp[1]+1]
        rocktmp = kingRock(kingtmp,rocktmp,1,1)
    elif m == 'LT':
        kingtmp = [kingtmp[0]-1,kingtmp[1]+1]
        rocktmp = kingRock(kingtmp,rocktmp,-1,1)
    elif m == 'RB':
        kingtmp = [kingtmp[0]+1,kingtmp[1]-1]
        rocktmp = kingRock(kingtmp,rocktmp,1,-1)
    elif m == 'LB':
        kingtmp = [kingtmp[0]-1,kingtmp[1]-1]
        rocktmp = kingRock(kingtmp,rocktmp,-1,-1)

    if boardCheck(kingtmp[0],kingtmp[1],rocktmp[0],rocktmp[1]):
        king = kingtmp
        rock = rocktmp

for _ in range(n):
    kingMove = input().strip()
    move(kingMove)

king = [chr(king[0]),str(king[1])]
rock = [chr(rock[0]),str(rock[1])]
print(''.join(king))
print(''.join(rock))
