from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('tic-tac-toe')

# X start so true
clicked = True
count = 0


#disable all the buttons after game is over
def disable_buttons():
    BoxNum1.config(state=DISABLED)
    BoxNum2.config(state=DISABLED)
    BoxNum3.config(state=DISABLED)
    BoxNum4.config(state=DISABLED)
    BoxNum5.config(state=DISABLED)
    BoxNum6.config(state=DISABLED)
    BoxNum7.config(state=DISABLED)
    BoxNum8.config(state=DISABLED)
    BoxNum9.config(state=DISABLED)

#check to see if someone won
def checkifwon():
    global winner
    winner = False

    #check if X won

    if BoxNum1["text"] == "X" and BoxNum2["text"] == "X" and BoxNum3["text"] == "X":
        BoxNum1.config(bg="red")
        BoxNum2.config(bg="red")
        BoxNum3.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "X wins!!")
        disable_buttons()
    elif BoxNum4["text"] == "X" and BoxNum5["text"] == "X" and BoxNum6["text"] == "X":
        BoxNum4.config(bg="red")
        BoxNum5.config(bg="red")
        BoxNum6.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "X wins!!")
        disable_buttons()
    elif BoxNum7["text"] == "X" and BoxNum8["text"] == "X" and BoxNum9["text"] == "X":
        BoxNum7.config(bg="red")
        BoxNum8.config(bg="red")
        BoxNum9.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "X wins!!")
        disable_buttons()
    elif BoxNum1["text"] == "X" and BoxNum4["text"] == "X" and BoxNum7["text"] == "X":
        BoxNum1.config(bg="red")
        BoxNum4.config(bg="red")
        BoxNum7.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "X wins!!")
        disable_buttons()
    elif BoxNum2["text"] == "X" and BoxNum5["text"] == "X" and BoxNum8["text"] == "X":
        BoxNum2.config(bg="red")
        BoxNum5.config(bg="red")
        BoxNum8.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "X wins!!")
        disable_buttons()
    elif BoxNum3["text"] == "X" and BoxNum6["text"] == "X" and BoxNum9["text"] == "X":
        BoxNum3.config(bg="red")
        BoxNum6.config(bg="red")
        BoxNum9.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "X wins!!")
        disable_buttons()
    elif BoxNum1["text"] == "X" and BoxNum5["text"] == "X" and BoxNum9["text"] == "X":
        BoxNum1.config(bg="red")
        BoxNum5.config(bg="red")
        BoxNum9.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "X wins!!")
        disable_buttons()
    elif BoxNum3["text"] == "X" and BoxNum5["text"] == "X" and BoxNum7["text"] == "X":
        BoxNum3.config(bg="red")
        BoxNum5.config(bg="red")
        BoxNum7.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "X wins!!")
        disable_buttons()

    #check if O won

    elif BoxNum1["text"] == "O" and BoxNum2["text"] == "O" and BoxNum3["text"] == "O":
        BoxNum1.config(bg="red")
        BoxNum2.config(bg="red")
        BoxNum3.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "O wins!!")
        disable_buttons()
    elif BoxNum4["text"] == "O" and BoxNum5["text"] == "O" and BoxNum6["text"] == "O":
        BoxNum4.config(bg="red")
        BoxNum5.config(bg="red")
        BoxNum6.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "O wins!!")
        disable_buttons()
    elif BoxNum7["text"] == "O" and BoxNum8["text"] == "O" and BoxNum9["text"] == "O":
        BoxNum7.config(bg="red")
        BoxNum8.config(bg="red")
        BoxNum9.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "O wins!!")
        disable_buttons()
    elif BoxNum1["text"] == "O" and BoxNum4["text"] == "O" and BoxNum7["text"] == "O":
        BoxNum1.config(bg="red")
        BoxNum4.config(bg="red")
        BoxNum7.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "O wins!!")
        disable_buttons()
    elif BoxNum2["text"] == "O" and BoxNum5["text"] == "O" and BoxNum8["text"] == "O":
        BoxNum2.config(bg="red")
        BoxNum5.config(bg="red")
        BoxNum8.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "O wins!!")
        disable_buttons()
    elif BoxNum3["text"] == "O" and BoxNum6["text"] == "O" and BoxNum9["text"] == "O":
        BoxNum3.config(bg="red")
        BoxNum6.config(bg="red")
        BoxNum9.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "O wins!!")
        disable_buttons()
    elif BoxNum1["text"] == "O" and BoxNum5["text"] == "O" and BoxNum9["text"] == "O":
        BoxNum1.config(bg="red")
        BoxNum5.config(bg="red")
        BoxNum9.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "O wins!!")
        disable_buttons()
    elif BoxNum3["text"] == "O" and BoxNum5["text"] == "O" and BoxNum7["text"] == "O":
        BoxNum3.config(bg="red")
        BoxNum5.config(bg="red")
        BoxNum7.config(bg="red")
        winner = True
        messagebox.showinfo(" ", "O wins!!")
        disable_buttons()   
    
    #check if tie
    if count == 9 and winner == False:
        messagebox.showinfo(" ", "tie!! \n no one wins") 
        disable_buttons()

#button clicked fun
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
          b["text"] = "O"
          clicked = True
          count += 1
          checkifwon()
    else:
        messagebox.showerror(" ", "try another box \n")

#restart the game
def restart():
    global BoxNum1, BoxNum2, BoxNum3, BoxNum4, BoxNum5, BoxNum6, BoxNum7, BoxNum8, BoxNum9
    global clicked, count
    clicked = True
    count = 0

    #build our buttons
    BoxNum1 = Button(root, text=" ", font=("", 20), height=3, width=6, command= lambda: b_click(BoxNum1))
    BoxNum2 = Button(root, text=" ", font=("", 20), height=3, width=6, command= lambda: b_click(BoxNum2)) 
    BoxNum3 = Button(root, text=" ", font=("", 20), height=3, width=6, command= lambda: b_click(BoxNum3)) 

    BoxNum4 = Button(root, text=" ", font=("", 20), height=3, width=6, command= lambda: b_click(BoxNum4)) 
    BoxNum5 = Button(root, text=" ", font=("", 20), height=3, width=6, command= lambda: b_click(BoxNum5)) 
    BoxNum6 = Button(root, text=" ", font=("", 20), height=3, width=6, command= lambda: b_click(BoxNum6)) 

    BoxNum7 = Button(root, text=" ", font=("", 20), height=3, width=6, command= lambda: b_click(BoxNum7)) 
    BoxNum8 = Button(root, text=" ", font=("", 20), height=3, width=6, command= lambda: b_click(BoxNum8)) 
    BoxNum9 = Button(root, text=" ", font=("", 20), height=3, width=6, command= lambda: b_click(BoxNum9)) 

    #grid our buttons to the screen
    BoxNum1.grid(row=0, column=0)
    BoxNum2.grid(row=0, column=1)
    BoxNum3.grid(row=0, column=2)

    BoxNum4.grid(row=1, column=0)
    BoxNum5.grid(row=1, column=1)
    BoxNum6.grid(row=1, column=2)

    BoxNum7.grid(row=2, column=0)
    BoxNum8.grid(row=2, column=1)
    BoxNum9.grid(row=2, column=2)

#create menue
my_menu = Menu(root)
root.config(menu=my_menu)

#create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="options", menu=options_menu)
options_menu.add_command(label="play again", command=restart)
restart()

root.mainloop()