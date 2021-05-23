import socket
import random

deck = [
'0.r','1.r','1.r','2.r','2.r','3.r','3.r','4.r','4.r','5.r','5.r','6.r','6.r','7.r','7.r','8.r','8.r','9.r','9.r','S.r','S.r','R.r','R.r','+2.r','+2.r','+4.w','C.w',
'0.y','1.y','1.y','2.y','2.y','3.y','3.y','4.y','4.y','5.y','5.y','6.y','6.y','7.y','7.y','8.y','8.y','9.y','9.y','S.y','S.y','R.y','R.y','+2.y','+2.y','+4.w','C.w',
'0.g','1.g','1.g','2.g','2.g','3.g','3.g','4.g','4.g','5.g','5.g','6.g','6.g','7.g','7.g','8.g','8.g','9.g','9.g','S.g','S.g','R.g','R.g','+2.g','+2.g','+4.w','C.w',
'0.b','1.b','1.b','2.b','2.b','3.b','3.b','4.b','4.b','5.b','5.b','6.b','6.b','7.b','7.b','8.b','8.b','9.b','9.b','S.b','S.b','R.b','R.b','+2.b','+2.b','+4.w','C.w']


noOfPlayers = int(input("How many players?\n"))

playersDeck = []

for a in range(noOfPlayers):
    playersDeck.append([])

for x in range(len(playersDeck)):
    for y in range(7):
        playersDeck[x].append(random.choice(deck))

gameOver = False
lastCard = random.choice(deck)
print(lastCard)
while(not gameOver):
    for curntPlayer in playersDeck:
        print("Player", playersDeck.index(curntPlayer) + 1, "turn")            
        for a in curntPlayer:
            print(str(curntPlayer.index(a) + 1) + ")",a)
        print("Or type 0 to pickup")
        validCho = False
        while(not validCho):
            try:
                print("Last card is",lastCard)
                playerChoice = int(input("Chose a card to put down"))
                if(playerChoice == 0):
                    newCard=random.choice(deck)
                    print("Picking up", newCard)
                    curntPlayer.append(newCard)
                    validCho = True
                elif(curntPlayer[playerChoice - 1].split('.')[0] in lastCard.split('.') or curntPlayer[playerChoice - 1].split('.')[1] in lastCard.split('.')):
                    print("cool")
                    validCho = True
                    lastCard = curntPlayer[playerChoice - 1]
                    del curntPlayer[playerChoice - 1]
                else:
                    print("not valid")


            except:
                print("Type a number next to one of cards")
