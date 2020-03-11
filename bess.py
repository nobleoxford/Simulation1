import random

playerPosition = 0
menuinput=input("1 = start, 2 = exit: ")
print("Win when you Roll 2 6's")
if menuinput == '1':
    win = False
    while win == False:
        playerRoll = random.randint(1,6)
        print("Dice roll: " + str(playerRoll))
        if playerRoll == 6:
            diceroll = random.randint(1,6)
            if diceroll == 6:
                win = True
                print("You won the game")
                
                    
