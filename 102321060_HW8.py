def printIntro():
    print('This program simulates a game of volleyball between two group')
    print('called "A" and "B". The abilities of each group is indicated by')
    print('a probability (a number between 0 and 1) that the group wins the')
    print('point when serving. Group A always has the first serve.')
    print()
    
def getInputs():
    x=eval(input('What is the probability group A wins a serve? '))
    y=eval(input('What is the probability that group B wins a server? '))
    z=eval(input('How many games to simulate? '))
    print()
    print('Games simulated:',z)
    return x,y,z

def simOneGame(a, b):
    from random import random
    serving ='A'
    winsA=0
    winsB=0
    while not(winsA==25 or winsB==25 or (winsA==24 and winsB==24)):
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
    if winsA==24 and winsB==24:
        while not abs(winsA-winsB)==2:
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
    printSummary(winsA, winsB)

main()
