from tkinter import *
import random

# Initialize the main window
play = Tk()
play.geometry('700x500')
play.title("Rock-Paper-Scissor")
play.configure(bg='lightblue')

# Define choices for the game
choices = {'0': 'Rock', '1': 'Paper', '2': 'Scissor'}

def player_rock():
    selected = choices[str(random.randint(0, 2))]
    if selected == 'Rock':
        result = 'Tie!..'
    elif selected == 'Paper':
        result = 'Computer Wins!..'
    else:
        result = 'Player Wins!..'
    l1.config(text='Rock')
    l2.config(text=selected)
    l3.config(text=result)
    btndisable()

def player_paper():
    selected = choices[str(random.randint(0, 2))]
    if selected == 'Rock':
        result = 'Player Wins!..'
    elif selected == 'Paper':
        result = 'Tie!..'
    else:
        result = 'Computer Wins!..'
    l1.config(text='Paper')
    l2.config(text=selected)
    l3.config(text=result)
    btndisable()

def player_scissor():
    selected = choices[str(random.randint(0, 2))]
    if selected == 'Rock':
        result = 'Computer Wins!..'
    elif selected == 'Paper':
        result = 'Player Wins!..'
    else:
        result = 'Tie!..'
    l1.config(text='Scissor')
    l2.config(text=selected)
    l3.config(text=result)
    btndisable()

def btndisable():
    b1['state'] = 'disabled'
    b2['state'] = 'disabled'
    b3['state'] = 'disabled'

def reset():
    b1['state'] = 'active'
    b2['state'] = 'active'
    b3['state'] = 'active'
    l1.config(text=' ')
    l2.config(text=' ')
    l3.config(text=' ')

# Create UI elements
Label(play, text='Rock-Paper-Scissor', font=('calibri', 30)).place(x=200, y=10)
Label(play, text="Choose Any one..", font=('calibri', 20), bg='lightblue').place(x=270, y=90)

b1 = Button(play, text='Rock', font=('calibri', 20), bg='orange', fg='white', width='9', height='1', command=player_rock)
b1.place(x=80, y=150)

b2 = Button(play, text='Paper', font=('calibri', 20), bg='orange', fg='white', width='9', height='1', command=player_paper)
b2.place(x=270, y=150)

b3 = Button(play, text='Scissor', font=('calibri', 20), bg='orange', fg='white', width='9', height='1', command=player_scissor)
b3.place(x=460, y=150)

selectframe = Frame(play, width='600', height='100')
selectframe.place(x=50, y=250)

Label(selectframe, text='Player Selected : ', font=('calibri', 15)).place(x=20, y=20)
Label(selectframe, text='Computer Selected : ', font=('calibri', 15)).place(x=350, y=20)

l1 = Label(selectframe, font=('calibri', 17, 'bold'), fg='red')
l1.place(x=100, y=50)

l2 = Label(selectframe, font=('calibri', 17, 'bold'), fg='red')
l2.place(x=430, y=50)

l3 = Label(play, font=('calibri', 20, 'bold'), fg='red')
l3.place(x=250, y=400)

b4 = Button(play, text='Reset', font=('calibri', 20), bg='blue', fg='white', width='9', height='1', command=reset)
b4.place(x=500, y=420)

play.mainloop()
