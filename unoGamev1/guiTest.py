import tkinter as tk
from functools import partial

root = tk.Tk()
 
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, fill=tk.X)

cards = ['0.r','2.g','3.b','4.g']
karirano = list(tk.PhotoImage(file=str(k)+".png") for k in cards)
button = list()
z = 0
for y in range(2):
    for x in range(2):
        button.append(tk.Button(frame1, image=karirano[z]))
        button[-1].grid(row=y,column=x)
        z += 1

root.mainloop()
