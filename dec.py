n=int(input())
l=[]
while n>0:
    rem=n%2
    l.append(rem)
    n=n//2
print(l[::-1])#1010
for i in range(len(l)):
    if l[i]==1:
        l[i]=0
    else:
        l[i]=1
print(l[::-1])#0101
p=len(l)-1
d=0
for i in range(len(l)-1,-1,-1):
    d+=l[i]*(2**p)
    p-=1
print(d)

n=int(input())
b=bin(n)[2:]#to remove 0b
b=b.replace('0','x')
b=b.replace('1','0')
b=b.replace('x','1')
print(int(b,2))