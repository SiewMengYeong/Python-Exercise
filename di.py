import random
count = [ 0 ] * 12
for i in range(100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    a = dice1 + dice2
    count[a-1] = count[a-1] + 1

for j in range(11):
    print(j+2,count[a],sep=" - ")
