# 구현,문자열_뒤집힌 덧셈/브론즈1

x,y = map(str,input().split())

x,y=int(x[::-1]),int(y[::-1])

ans=str(x+y)

print(int(ans[::-1]))