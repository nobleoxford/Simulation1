import random
plyerPosition = 0
menuinput=input("1 = start, 2 = exit: ")
if menuinput == '1':
    while playerPosition <= 25:
        diceroll = randint(1,6)
    	print("Dice roll: " + diceroll)
    	playerPosition += diceroll
    	    if playerPosition== '6':
                    playerPosition -= 4
                
                    
