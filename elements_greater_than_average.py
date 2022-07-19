n=int(input())
a=list(map(int,input().split()))
avg=0
c=0
avg=sum(a)//len(a)
for i in a:
    if i>=avg:
        c+=1
print(c)