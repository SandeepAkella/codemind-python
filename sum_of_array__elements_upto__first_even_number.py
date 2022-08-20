
n=int(input())
a=list(map(int,input().split()))
d=0
for i in a:
    if i%2==0:
        break
    else:
        d+=i
print(d)
