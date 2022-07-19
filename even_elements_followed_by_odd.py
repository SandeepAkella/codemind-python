n=int(input())
a=list(map(int,input().split()))
x=[]
y=[]
for i in a:
    if i%2:
        x.append(i)
    else:
        y.append(i)
print(*y,end=' ')
print(*x)
       