from tkinter import *
from subprocess import call

#to call and link to the other python files
def welcome():
    call(["python", "checkin.py"])

def out():
    call(["python", "checkout.py"])

def glist():
    call(["python", "guestlist.py"]) 

def food():
    call(["python", "food.py"])   

class MainMenu:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("700x500")
        self.window.title("Hotel Management System")
        self.photo = PhotoImage(file="D:/Users/marun_hr6sf03/Pictures/Patet Files/School/College/Second Year/2nd Semester/AOOP/Assembled proj/pool.png")

        self.label = Label(self.window)
        self.label.configure(
            text="Hotel de Levi",
            font=("italic", 30),
            image=self.photo,
            compound='bottom',
            relief=GROOVE,
            bd=10
        )

        self.button1 = Button(self.window)
        self.button1.configure(
            text="CHECK IN",
            font=("italic", 20),
            bd=5,
            command=welcome
        )

        self.button2 = Button(self.window)
        self.button2.configure(
            text="GUEST LIST",
            bd=5,
            font=("italic", 20),
            command=glist
        )
        self.button3 = Button(self.window)
        self.button3.configure(
            text="CHECKOUT",
            bd=5,
            font=("italic", 20),
            command=out
        )

        self.button4 = Button(self.window)
        self.button4.configure(
            text="FOOD",
            bd=5,
            font=("italic", 20),
            command=food
        )

        self.button5 = Button(self.window)
        self.button5.configure(
            text="EXIT",
            bd=5,
            font=("italic", 20),
            command=exit
        )

        self.label.place(x=45, y=15)
        self.button1.place(relx=0.15, rely=0.3, relwidth=0.3)
        self.button2.place(relx=0.55, rely=0.3, relwidth=0.3)
        self.button3.place(relx=0.15, rely=0.55, relwidth=0.3)
        self.button4.place(relx=0.55, rely=0.55, relwidth=0.3)
        self.button5.place(relx=0.35, rely=0.75, relwidth=0.3)
        self.window.mainloop()


menu = MainMenu()