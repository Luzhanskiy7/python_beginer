import random
from tkinter import*
from tkinter import messagebox as mbox

tk = Tk()
tk.title('X_vs_0')
tk.geometry('377x367')
tk.resizable(False, False)

def start():
    global game_field
    global game_remains
    global button
    game_field = [None] * 9
    game_remains = list(range(9))
    button = [Button(width=5, height=2, font=('Arial', 28, 'bold'), bg='black',
                  command=lambda x=i: push(x)) for i in range(9)]
    row = 0
    col = 0
    for i in range(9):
        button[i].grid(row=row, column=col)
        row += 1
        if row == 3:
            col += 1
            row = 0

start()

def win(n):
    global game_field
    if (game_field[0] == n and game_field[3] == n and game_field[6] == n) or\
        (game_field[0] == n and game_field[1] == n and game_field[2] == n) or\
        (game_field[3] == n and game_field[4] == n and game_field[5] == n) or\
        (game_field[6] == n and game_field[7] == n and game_field[8] == n) or\
        (game_field[1] == n and game_field[4] == n and game_field[7] == n) or\
        (game_field[2] == n and game_field[5] == n and game_field[8] == n) or\
        (game_field[0] == n and game_field[4] == n and game_field[8] == n) or\
        (game_field[2] == n and game_field[4] == n and game_field[6] == n):
        return True

def message(choice):
    r = mbox.askquestion(choice, "Repeat?")
    if r == 'no':
        exit()
    else:
        start()

def push(num):
    global game_field
    global game_remains
    global button
    for j in range(9):
        if j == num:
            game_field[num] = 'X'
            button[num].config(text='X', bg='yellow', fg='black', state='disabled')
            game_remains.remove(num)
            if len(game_remains) > 0:
                cpu = random.choice(game_remains)
                game_field[cpu] = '0'
                button[cpu].config(text='0', bg='green', fg='black', state='disabled')
                game_remains.remove(cpu)
            else:
               message("Draw")
            if win('X'):
                message("You WIN")
            elif win('0'):
                message("You LOSE")

mainloop()
