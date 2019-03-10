def simNGames(n,a,b):
    from ramdom import*
    serving = 'A'
    winsA=0
    winsB=0
    for i in range (n):
        sA,sB=simOneGame(a,b)
        if sA>sB:
            winsA=winsA+1
        else:
            winsB=winsB+1
    return winsA,winsB
 
def simOneGame(a, b):
    winsA=0
    winsB=0
    while not(winsA==15 or winsB==15):
            if serving == 'A':
                if ramdon()<a:
                    winsA=winsA+1
                else:
                    serving ='B'            
            if serving == 'B':
                if ramdon()<b:
                    winsB=winsB+1
                else:
                    serving ='A'
      return winsA,winsB 
    
def simNGames(n, probA, probB):
# Simulates n games of racquetball between players A and B
# RETURNS number of wins for A, number of wins for B
    winsA= winsB= 0
    for i in range(n):
        scoreA, scoreB= simOneGame(probA, probB)
        if scoreA> scoreB:
            winsA= winsA+ 1
        else:
            winsB= winsB+ 1
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players A and B
    # RETURNS A's final score, B's final score
    serving = "A“
    scoreA= 0
    scoreB= 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a,b):
    # a and b are scores for players in a racquetball game
    # RETURNS true if game is over, false otherwise
    return a == 15 or b == 15

