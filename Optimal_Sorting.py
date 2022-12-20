t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    if b==a:
        print(0)
    else:
        print(b[-1]-b[0])
    t-=1