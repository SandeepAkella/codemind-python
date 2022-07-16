n=int(input())
a=list(map(int,input().split()))
e,o=0,0
for i in range(n):
    if i%2:
        o+=a[i]
    else:
        e+=a[i]
print(abs(e-o))