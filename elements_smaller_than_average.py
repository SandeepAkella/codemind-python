n=int(input())
a=list(map(int,input().split()))
c=0
avg=0
avg=sum(a)//len(a)
for i in range(0,n):
    if a[i]<=avg:
        c+=1
print(c)