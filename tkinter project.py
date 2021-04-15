from tkinter import *
import random
root = Tk()
root.title('Rock Paper Scissors!')
root.configure(bg='grey')
root.geometry("700x470+480+150")
frame = Frame(root)
frame.pack()
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)
bottomFrame = Frame(root)
bottomFrame.pack(side=LEFT)
leftFrame = Frame(root)
leftFrame.pack(side=LEFT)
topFrame = Frame(root)
topFrame.pack(side=TOP)
text = Text(root, fg="purple")
text.insert(INSERT, "Rock Paper Scissors!")
text.pack()
text.configure(bg='lightblue')
def calculationforrock():
    if random.randrange(1, 3) == 1:
        text.insert(INSERT, "     rock, Draw!     ")
    elif random.randrange(1, 3) == 2:
        text.insert(INSERT, "    Paper, Haha I got you!     ")
    else:
        text.insert(INSERT, "     scissors, Nooo you got me!     ") 
def calculationforpaper():
    if random.randrange(1, 3) == 1:
        text.insert(INSERT,"     Rock, Nooo I lost!     ")
    elif random.randrange(1, 3) == 2:
        text.insert(INSERT, "     Paper, Draw!     ")
    else:
        text.insert(INSERT, "     Scissors, Haha I win!     ")
def calculationforscissors():
    if random.randrange(1, 3) == 1:
        text.insert(INSERT, "     rock, Haha I win!     ")
    elif random.randrange(1, 3) == 2:
        text.insert(INSERT, "     Paper, Nooo I lost!     ")
    else:
        text.insert(INSERT, "     Scissors, Draw!     ")
B = Button(leftFrame, text ="rock", fg="red", command=calculationforrock, bg="lightgrey")
C = Button(root, text="paper", fg="green", command=calculationforpaper, bg="lightgrey")
D = Button(rightFrame, text="scissors", fg="blue", bg="lightgrey", command=calculationforscissors)
E = Button(root, text="Quit", command=root.destroy)

B.pack(side=BOTTOM)
C.pack()
D.pack(side=BOTTOM)
E.pack(side=BOTTOM)
root.mainloop()
