
m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
x=len(a.union(b))
y=len(a.intersection(b))
print(x-y)

