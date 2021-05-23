import socket
import random

import tkinter as tk
from functools import partial

deck = [
'0.r','1.r','1.r','2.r','2.r','3.r','3.r','4.r','4.r','5.r','5.r','6.r','6.r','7.r','7.r','8.r','8.r','9.r','9.r','S.r','S.r','R.r','R.r','+2.r','+2.r','+4.w','C.w',
'0.y','1.y','1.y','2.y','2.y','3.y','3.y','4.y','4.y','5.y','5.y','6.y','6.y','7.y','7.y','8.y','8.y','9.y','9.y','S.y','S.y','R.y','R.y','+2.y','+2.y','+4.w','C.w',
'0.g','1.g','1.g','2.g','2.g','3.g','3.g','4.g','4.g','5.g','5.g','6.g','6.g','7.g','7.g','8.g','8.g','9.g','9.g','S.g','S.g','R.g','R.g','+2.g','+2.g','+4.w','C.w',
'0.b','1.b','1.b','2.b','2.b','3.b','3.b','4.b','4.b','5.b','5.b','6.b','6.b','7.b','7.b','8.b','8.b','9.b','9.b','S.b','S.b','R.b','R.b','+2.b','+2.b','+4.w','C.w']


noOfPlayers = int(input("How many players?\n"))

playersDeck = []

for a in range(noOfPlayers):
    playersDeck.append(['P.w'])

for x in range(len(playersDeck)):
    for y in range(7):
        playersDeck[x].append(random.choice(deck))

gameOver = False
lastCard = random.choice(deck)
print(lastCard)

my_w = tk.Tk()
my_w.title("www.plus2net.com")  # Adding a title


my_str = tk.StringVar()
l1 = tk.Label(my_w,  textvariable=my_str, width=10 )
l1.grid(row=0,column=1,columnspan=5) 
my_str2 = tk.StringVar()
l2 = tk.Label(my_w,  textvariable=my_str2,width=10 )
l2.grid(row=0,column=2,columnspan=5) 
while(not gameOver):
    for curntPlayer in playersDeck:
        my_str2.set("Player " + str(playersDeck.index(curntPlayer)+1))
        def show_lan(my_language):
            global lastCard
            my_str.set(my_language)
            if(my_language == 'P.w'):
                    newCard=random.choice(deck)
                    print("Picking up", newCard)
                    curntPlayer.append(newCard)
                    my_w.quit()

            elif('.w' in lastCard):
                print("next step")
                lastCard = my_language
                del curntPlayer[curntPlayer.index(my_language)]
                my_w.quit()

            elif(my_language == 'C.w'):
                print("color change")
                lastCard = my_language
                del curntPlayer[curntPlayer.index(my_language)]
                my_w.quit()

            elif(my_language.split('.')[0] in lastCard.split('.') or my_language.split('.')[1] in lastCard.split('.')):
                print("cool")
                lastCard = my_language
                del curntPlayer[curntPlayer.index(my_language)]
                my_w.quit()

            else:
                print("not valid")

        karirano = list(tk.PhotoImage(file="img/"+str(k)+".png") for k in curntPlayer)
        x = 0
        y = 1
        z=0
        loldeck = tk.PhotoImage(file="img/"+str(lastCard)+".png")
        btn1 = tk.Button(my_w, image=loldeck)
        btn1.grid(row=0,column=0)
        for language in curntPlayer:
            btn = tk.Button(my_w, image=karirano[z], command=lambda lan=language:show_lan(lan))
            btn.grid(row=y,column=x)
            x += 1
            z+=1
            if(x >= 4):
                x=0
                y+=1
        if(len(curntPlayer) == 1):
            my_str2.set("Player " + str(playersDeck.index(curntPlayer)+1)+ " Won!!")
            input()
        my_w.mainloop()
        
