# 수학/무알콜 칵테일/브론즈1

a,b,c = map(int,input().split())
i,j,k = map(int,input().split())

ju = min(a/i, b/j, c/k)

print(a-i*ju, b-j*ju, c-k*ju)
