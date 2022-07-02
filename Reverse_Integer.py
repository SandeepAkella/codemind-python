a=int(input())
temp=a
n=abs(a)
sum=0
while(n):
    r=n%10
    sum=sum*10+r
    n=n//10
if temp>0:
    print(sum)
else:
    print(-sum)
    