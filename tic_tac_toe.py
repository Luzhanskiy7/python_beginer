import random
from tkinter import*
from tkinter import messagebox as mbox

tk = Tk()
count_you = 0
count_bot = 0

tk.title('X_vs_0')
tk.geometry('377x387')
tk.resizable(False, False)
tk.config(cursor="target", bg='black')
def visual():
    global count_bot
    global count_you
    you_text = Label(tk, text='You:', font='Arial 18', fg='green', bg='black')
    bot_text = Label(tk, text='Bot:', font='Arial 18', fg='yellow', bg='black')
    you_score = Label(tk, text=count_you, font='Arial 18', fg='green', bg='black')
    bot_score = Label(tk, text=count_bot, font='Arial 18', fg='yellow', bg='black')
    you_text.place(x=80, y=357)
    bot_text.place(x=200, y=357)
    you_score.place(x=140, y=357)
    bot_score.place(x=250, y=357)



visual()

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
    global count_you
    global count_bot


    for j in range(9):
        count_you = 0
        count_bot = 0
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
                count_you += 1
                print(count_you)
            elif win('0'):
                message("You LOSE")
                count_bot += 1
                print(count_bot)
visual()


mainloop()
