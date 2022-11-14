# idiotic tictactoe

# Author :qNthuman

# the most idiotic foolish stupid way of creating a tic tac toe game.
# also u have to decide the winner.


from tkinter import *


from tkinter.ttk import *


root = Tk()

user = StringVar()
display = IntVar()
display.set(9)
user.set("X")


b1 = StringVar()
b2 = StringVar()
b3 = StringVar()
b4 = StringVar()
b5 = StringVar()
b6 = StringVar()
b7 = StringVar()
b8 = StringVar()
b9 = StringVar()


def play(var):
    usrstate = user.get()
    no = display.get()

    if no >= 0:
        if usrstate == 'X':
            var.set(usrstate)
            user.set("O")
            no -= 1
            display.set(no)
        elif usrstate == 'O':
            var.set(usrstate)
            user.set("X")
            no -= 1
            display.set(no)

        print(no)
    else:
        win = Toplevel(root)
        label = Label(win, text="You Win!").grid()


def fb1():
    play(b1)


def fb2():
    play(b2)


def fb3():
    play(b3)


def fb4():
    play(b4)


def fb5():
    play(b5)


def fb6():
    play(b6)


def fb7():
    play(b7)


def fb8():
    play(b8)


def fb9():
    play(b9)


userlabel = Label(root, textvariable=user).grid()
button1 = Button(root, textvariable=b1, command=fb1).grid(row=0, column=0)
button2 = Button(root, textvariable=b2, command=fb2).grid(row=0, column=1)
button3 = Button(root, textvariable=b3, command=fb3).grid(row=0, column=2)
button4 = Button(root, textvariable=b4, command=fb4).grid(row=1, column=0)
button5 = Button(root, textvariable=b5, command=fb5).grid(row=1, column=1)
button6 = Button(root, textvariable=b6, command=fb6).grid(row=1, column=2)
button7 = Button(root, textvariable=b7, command=fb7).grid(row=2, column=0)
button8 = Button(root, textvariable=b8, command=fb8).grid(row=2, column=1)
button9 = Button(root, textvariable=b9, command=fb9).grid(row=2, column=2)


root.mainloop()

# But, it works.



# under rate the game