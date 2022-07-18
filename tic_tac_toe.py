import random
from tkinter import*
from tkinter import messagebox as mbox

tk = Tk()
tk.title('X_vs_0')
tk.geometry('377x367')
tk.resizable(False, False)
tk.config(cursor="target")
MAX_BUTTON = 9

def start():
    global game_field
    global game_remains
    global button

    game_field = [None] * MAX_BUTTON
    game_remains = list(range(MAX_BUTTON))
    button = [Button(width=5, height=2, font=('Arial', 28, 'bold'), bg='black',
                  command=lambda x=i: push(x)) for i in range(MAX_BUTTON)]
    row = 0
    col = 0
    for i in range(MAX_BUTTON):
        button[i].grid(row=row, column=col)
        row += 1
        if row == 3:
            col += 1
            row = 0

start()

def win(n):
    global game_field
    global batton

    if (game_field[0] == n and game_field[3] == n and game_field[6] == n):
        button[0].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[3].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[6].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        return True
    elif (game_field[0] == n and game_field[1] == n and game_field[2] == n):
        button[0].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[1].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[2].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        return True
    elif (game_field[3] == n and game_field[4] == n and game_field[5] == n):
        button[3].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[4].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[5].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        return True
    elif (game_field[6] == n and game_field[7] == n and game_field[8] == n):
        button[6].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[7].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[8].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        return True
    elif (game_field[1] == n and game_field[4] == n and game_field[7] == n):
        button[1].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[4].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[7].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        return True
    elif (game_field[2] == n and game_field[5] == n and game_field[8] == n):
        button[2].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[5].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[8].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        return True
    elif (game_field[0] == n and game_field[4] == n and game_field[8] == n):
        button[0].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[4].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[8].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        return True
    elif (game_field[2] == n and game_field[4] == n and game_field[6] == n):
        button[2].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[4].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        button[6].config(text=n, bg='red', fg='black', cursor='pirate', state='disabled')
        return True

def message(choice):
    ask_question = mbox.askquestion(choice, "Repeat?")
    if ask_question == 'no':
        exit()
    else:
        start()

def push(num):
    global game_field
    global game_remains
    global button
    for j in range(MAX_BUTTON):
        if j == num:
            game_field[num] = 'X'
            button[num].config(text='X', bg='yellow', fg='black', cursor='pirate', state='disabled')
            game_remains.remove(num)
            if len(game_remains) > 0:
                cpu = random.choice(game_remains)
                game_field[cpu] = '0'
                button[cpu].config(text='0', bg='green', fg='black', cursor='pirate', state='disabled')
                game_remains.remove(cpu)
            else:
               message("Draw")
            if win('X'):
                message("You WIN")
            elif win('0'):
                message("You LOSE")
mainloop()
