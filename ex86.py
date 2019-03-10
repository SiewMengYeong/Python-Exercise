def main():
  print('Find every prime number less than or equal to N.')
  from time import time
  start_time=time()
  import math
  x=eval(input('Please input a positive number -- '))
  for i in range(2,x+1):
    y=round(math.sqrt(i))
    for j in range(2,y+1):
      if i%j==0 and i!=j:
        print(end='')
      elif i%j!=0:
        print(i,end=' ')
      else:
        print(end='')
  print()
  end_time=time()
  print('It takes',abs(start_time-end_time),
        'seconds to find these prime numbers.')

main()

def a():
 while i<=y:
     if x%i!=0:
        i=i+1
     else:
        i=y+1
        print(x,'is not a prime number.')

