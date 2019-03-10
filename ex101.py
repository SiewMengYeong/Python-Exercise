from random import randint

class Card:
  def __init__(self,rank,suit):
    self.rank=rank
    self.suit=suit
    self.bjvalue=rank

  def getrank(self):
    if self.rank==1:
      self.rank='Ace'
    elif self.rank==11:
      self.rank='Jack'
    elif self.rank==12:
      self.rank='Queen'
    elif self.rank==13:
      self.rank='King'
    return self.rank

  def getsuit(self):
    if self.suit=='d':
      self.suit='Diamonds.'
    elif self.suit=='c':
      self.suit='Clubs.'
    elif self.suit=='h':
      self.suit='Hearts.'
    elif self.suit=='s':
      self.suit='Spades.'
    return self.suit

  def BJValue(self,rank):
    if rank>10:
      self.bjvalue=10
    return self.bjvalue

  def __str__(self):
    self.getrank()
    self.getsuit()
    return str(self.rank)+' of '+str(self.suit)

def main():
  a=eval(input('How many cards do you want to test -- '))
  for i in range(a):
    r=randint(1,13)
    x=randint(0,3)
    y=['d','c','h','s']
    s=y[x]
    poker=Card(r,s)
     
    
    print('{0:20}{1:>10}'.format(poker,poker.BJValue(r)))

if __name__=='__main__':main()
