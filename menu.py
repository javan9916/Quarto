from tkinter import *
from User import *
from game import *

usersList = []

def openGameScreen():
    root.withdraw()
    global screen1
    screen1 = Toplevel()
    screen1.geometry("300x200+100+100")
    screen1.config(background='black')
    label1 = Label(screen1, text="Jugador 1: ", fg="white", bg="black")
    label1.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entry1 = Entry(screen1, background="white")
    entry1.pack()
    label2 = Label(screen1, text="Jugador 2: ", fg="white", bg="black")
    label2.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entry2 = Entry(screen1, background="white")
    entry2.pack()


    user1 = User("", 0, 0)
    user2 = User("", 0, 0)

    button1 = Button(screen1, text="Let's go", command=lambda: getNames(entry1,entry2,user1,user2))
    button1.pack(padx=5, pady=5, ipadx=5, ipady=5)


def getNames(entry1,entry2,user1,user2):
    name1 = Entry.get(entry1)
    name2 = Entry.get(entry2)
    user1.setName(name1)
    user2.setName(name2)

    if len(usersList) == 0:
        usersList.append(user1)
        usersList.append(user2)
    else:
        i = 0
        while i < len(usersList):
            if usersList[i].getName() != user1.getName():
                usersList.append(user1)
            else:
                user1 = usersList[i]
            i+=1

        i = 0
        while i < len(usersList):
            if usersList[i].getName() != user2.getName():
                usersList.append(user2)
            else:
                user2 = usersList[i]
            i+=1

    openGame(user1,user2)

def openGame(user1,user2):
    screen1.withdraw()
    main(user1, user2)

def openStatsScreen():
    root.withdraw()
    global screen2
    screen2 = Toplevel()
    screen2.geometry("600x400+100+100")

root = Tk()
root.title("Quarto")
root.geometry("300x200+100+100")
root.config(background='black')

label = Label(root, text="Quarto", fg="white", bg="black", )
label.pack(padx=5, pady=5, ipadx=5, ipady=5)
button1 = Button(root, text="Play", command=openGameScreen)
button1.place(x=632, y=220)
button1.pack(padx=5, pady=5, ipadx=5, ipady=5)
button = Button(root, text="Stats", command=openStatsScreen)
button.pack(padx=5, pady=5, ipadx=5, ipady=5)
button = Button(root, text="Exit", command=root.destroy)
button.pack(padx=5, pady=5, ipadx=5, ipady=5)

root.mainloop()



