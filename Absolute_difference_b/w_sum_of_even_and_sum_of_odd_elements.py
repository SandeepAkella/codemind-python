n=int(input())
a=list(map(int,input().split()))
e,o=0,0
for i in a:
    if i%2:
        o+=i
    else:
        e+=i
print(abs(e-o))