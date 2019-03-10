from random import*

def main():
  a=eval(input('How many cards do you want to test -- '))
  for i in range(a):
    r=randint(1,13)
    x=randint(0,3)
    y=['d','c','h','s']
    s=y[x]
    
    if 2<=r<=10:
      print(r,end=' ')
    elif r==1:
      print('Ace',end=' ')
    elif r==11:
      print('Jack',end=' ')
    elif r==12:
      print('Queen',end=' ')
    elif r==13:
      print('King',end=' ')
      
    if s=='d':
      print('of','Diamonds.',end='\t')
    elif s=='c':
      print('of','Clubs.',end='\t')
    elif s=='h':
      print('of','Hearts.',end='\t')
    elif s=='s':
      print('of','Spades.',end='\t')
      
    if 1<=r<=10:
      print(r)
    else:
      print(10)

main()

