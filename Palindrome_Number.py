n=int(input())
for i in range(1,n+1,1):
    t=int(input())
    temp=t
    sum=0
    while t>0:
        r=t%10
        sum=sum*10+r
        t=t//10
    if(temp==sum):
        print('True',end='
')
    else:
        print('False',end='
')
