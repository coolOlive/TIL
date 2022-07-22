# 구현_방 번호/실버5

n=list(input().strip())
tmp_n=list(set(n))

cnt=[]
for a in tmp_n:
    if a=='6' or a=='9':
        sixnine=n.count('6')+n.count('9')
        sixnine= sixnine//2 if sixnine%2==0 else sixnine//2+1
        cnt.append(sixnine)
    else:
        cnt.append(n.count(a))

print(max(cnt))