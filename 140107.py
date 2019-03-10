from random import randint
from time import time

a=randint(0,9)
b=randint(0,9)
c=randint(0,9)
d=randint(0,9)

while not (a!=0 and a!=b and b!=c and c!=d and d!=a and a!=c and b!=d):
    a=randint(0,9)
    b=randint(0,9)
    c=randint(0,9)
    d=randint(0,9)

alist=[str(a),str(b),str(c),str(d)]

starttime=time()
i=eval(input("guess 4 number = "))
s=[]
f=0
for j in str(i):
    s.append(j)
while alist!=s:
    for i in range(4):
        if alist[i]==s[i]:
            print (s[i],end='')
        else:
            print(chr(65+f),end='')
            f=f+1
    f=0
    print()
    i=eval(input("guess 4 number = "))
    s=[]
    for j in str(i):
        s.append(j)
        
endtime=time()

print('\nCongratulation the answer is correct!')
print('You spend the time is', endtime-starttime,'seconds.\n')
input("exit please <enter>")

