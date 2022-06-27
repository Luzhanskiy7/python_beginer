import random
from tkinter import*
from tkinter import messagebox as mbox

tk = Tk()
tk.title('X_vs_0')
tk.geometry('377x367')
tk.resizable(False, False)

hody = [None] * 9
zalyshok_hodiv = list(range(9))

but = [Button(width=5, height=2, font=('Arial', 28, 'bold'), bg='black', command=lambda x=i: push(x)) for i in range(9)]
row = 0
col = 0
for i in range(9):
    but[i].grid(row=row, column=col)
    row += 1
    if row == 3:
        col += 1
        row = 0

def restart():
    global hody
    global zalyshok_hodiv
    global but
    hody = [None] * 9
    zalyshok_hodiv = list(range(9))
    but = [Button(width=5, height=2, font=('Arial', 28, 'bold'), bg='black',
                  command=lambda x=i: push(x)) for i in range(9)]
    row = 0
    col = 0
    for i in range(9):
        but[i].grid(row=row, column=col)
        row += 1
        if row == 3:
            col += 1
            row = 0

def win(n):
        global hody
        if (hody[0] == n and hody[3] == n and hody[6] == n) or (hody[0] == n and hody[1] == n and hody[2] == n) \
                or (hody[3] == n and hody[4] == n and hody[5] == n) or (hody[6] == n and hody[7] == n and hody[8] == n)\
                or (hody[1] == n and hody[4] == n and hody[7] == n) or (hody[2] == n and hody[5] == n and hody[8] == n)\
                or (hody[0] == n and hody[4] == n and hody[8] == n) or (hody[2] == n and hody[4] == n and hody[6] == n):
            return True

def push(num):
        global hody
        global zalyshok_hodiv
        global but
        for j in range(9):
            if j == num:
                hody[num] = 'X'
                but[num].config(text='X', bg='yellow', fg='black', state='disabled')
                zalyshok_hodiv.remove(num)
                cpu = random.choice(zalyshok_hodiv)
                hody[cpu] = '0'
                but[cpu].config(text='0', bg='green', fg='black', state='disabled')
                zalyshok_hodiv.remove(cpu)
                if win('X'):
                    r = mbox.askquestion("You WIN", "Repeat?")
                    if r == 'no':
                        exit()
                    elif r == 'yes':
                         restart()
                elif win('0'):
                    r = mbox.askquestion("You LOSE", "Repeat?")
                    if r == 'no':
                        exit()
                    elif r == 'yes':
                        restart()

mainloop()

