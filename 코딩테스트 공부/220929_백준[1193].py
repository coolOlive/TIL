 # 수학/분수찾기/브론즈1

x=int(input())

tmp=1
while x>tmp:
    x-=tmp
    tmp+=1
    
if tmp%2==0:
    a=x
    b=tmp-x+1
else:
    a=tmp-x+1
    b=x
    
print(a,'/',b,sep='')