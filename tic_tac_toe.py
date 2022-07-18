import random
from tkinter import*
from tkinter import messagebox as mbox

tk = Tk()
tk.title('X_vs_0')
tk.geometry('377x398')
tk.resizable(False, False)
tk.config(cursor="target", bg='black')
MAX_BUTTON = 9
count_x = 0
count_o = 0

def visual_score():
    you_text = Label(tk, text='You:', font='Arial 18', fg='green', bg='black')
    bot_text = Label(tk, text='Bot:', font='Arial 18', fg='yellow', bg='black')
    you_score = Label(tk, text=count_x, font='Arial 18', fg='green', bg='black')
    bot_score = Label(tk, text=count_o, font='Arial 18', fg='yellow', bg='black')
    you_text.place(x=80, y=365)
    bot_text.place(x=200, y=365)
    you_score.place(x=135, y=365)
    bot_score.place(x=250, y=365)

def start():
    global game_field
    global game_remains
    global button
    global count_x
    global count_o

    game_field = [None] * MAX_BUTTON
    game_remains = list(range(9))
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
visual_score()

def win(n):
    global game_field
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
    global count_x
    global count_o
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
                count_x += 1
                message("You WIN")
            elif win('0'):
                count_o += 1
                message("You LOSE")
    visual_score()

mainloop()
