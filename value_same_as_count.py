
n=int(input())
a=list(map(int,input().split()))
r=[]
for i in a:
    if i==a.count(i) and i not in r:
        r.append(i)
print(len(r))

