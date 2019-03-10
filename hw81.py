def printIntro():
    print('This program simulates a game of racquetball between two players')
    print('called "A" and "B". The abilities of each player is indicated by')
    print('a probability (a number between 0 and 1) that the player wins the')
    print('point when serving. Player A always has the first serve.')
    print()
    
def getInputs():
    x=eval(input('What is the probability player A wins a serve? '))
    y=eval(input('What is the probability that player B wins a server? '))
    z=eval(input('How many games to simulate? '))
    print()
    print('Games simulated:',z)
    return x,y,z

def simOneGame(a, b):
    from random import random
    serving ='A'
    winsA=0
    winsB=0
    while not(winsA==15 or winsB==15):
            if serving == 'A':
                if random()<a:
                    winsA=winsA+1
                else:
                    serving ='B'            
            if serving == 'B':
                if random()<b:
                    winsB=winsB+1
                else:
                    serving ='A'
    return winsA, winsB 

def simNGames(n,a,b):   
    winsA=0
    winsB=0
    for i in range (n):
        sA, sB =simOneGame(a,b)
        if sA>sB:
            winsA=winsA+1
        else:
            winsB=winsB+1
    return winsA, winsB

def printSummary(x,y):
    print('Wins for A: ',x,'(','{0:3.1%}'.format(x/(x+y)),')')
    print('Wins for B: ',y,'(','{0:3.1%}'.format(y/(x+y)),')')
    
def main():
    printIntro()
    probA,probB,n=getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(probA,probB)

main()
