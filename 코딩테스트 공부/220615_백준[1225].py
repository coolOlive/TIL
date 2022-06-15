# 수학,구현,문자열_이상한 곱셈/브론즈2
# 각 자리수끼리 곱하는건 sum(a)*sum(b)와 같음

a,b=input().split()
a=list(map(int,a))
b=list(map(int,b))
print(sum(a)*sum(b))