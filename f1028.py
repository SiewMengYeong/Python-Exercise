import random
count = [ 0 ] * 6

for i in range(10):
    n = random.randint(1,6)
    count[n-1] = count[n-1] + 1
    print(count)
    
for i in range(6):
    print( i+1 , count[i] )
