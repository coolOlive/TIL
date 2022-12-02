# DP_피보나치 함수/실버3

t=int(input())

fibo_num=[[0,0] for i in range(41)]
fibo_num[0]=[1,0]
fibo_num[1]=[0,1]
index=1

def fibo(num):
    global index
    if index<num:
        for i in range(index+1,num+1):
            index+=1
            a=fibo_num[i-1]
            b=fibo_num[i-2]
            zero=a[0]+b[0]
            one=a[1]+b[1]
            fibo_num[i]=[zero,one]
        print(fibo_num[num][0],fibo_num[num][1])
    else:
        print(fibo_num[num][0],fibo_num[num][1])


for i in range(t):
    n=int(input())
    fibo(n)