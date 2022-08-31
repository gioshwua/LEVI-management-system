from tkinter import *
import pickle

#it close the first and secondary window 
#and let the user get back to the home page
def done(window, window2):
    window.destroy()
    window2.destroy()

def confirm(name, days, window):

    uname = name.get()
    nights = days.get()
    MOD = 0

    price = 500

    newprice = (int(nights)*price)

    print(newprice)

    #it will open and read the namedata file
    filename = "namedata"
    output_file = open(filename, 'rb')
    object = []

    #it will then transfer all the content to the object array
    while True:
        try:
            object.append(pickle.load(output_file))
        except EOFError:
            break
    
    #the for loop is to itirate through the object array
    #to look for the name that will be checked out

    #the MOD variable servers as an index for the MODdata
    #to know what kind of payment will be made

    for items in object:
        MOD = MOD + 1
        if uname == items:
            checkoutname = items
            object.remove(uname)
            break

    update = open("namedata", "wb")

    #after finding it, it will then delete and
    #update the file 
    [pickle.dump(value, update) for value in object]

    #it will open and read the MODdata
    filename = "MODdata"
    output_file = open(filename, 'rb')
    transaction = []

    #then it will transfer all the content to the transaction array
    while True:
        try:
            transaction.append(pickle.load(output_file))
        except EOFError:
            break
    
    #newtext is declared as is so that it can display 
    #how the user will make a payment in the window2
    newtext = transaction[MOD-1]

    #then it will be then deleted and the file will be updated
    transaction.remove(transaction[MOD-1])

    update = open("MODdata", "wb")

    [pickle.dump(value, update) for value in transaction]

    #--------------------------------------------------------

    window2 = Tk()
    window2.geometry("400x300")
    window2.title("Reciept")

    mainframe = Frame(window2)
    mainframe.configure(
        relief = GROOVE,
        borderwidth=3,
    )
    mainframe.place(relheight=0.95, relwidth=0.96, relx=0.02, rely=0.02)

    frame1 = Frame(mainframe)
    frame1.configure(
        relief = GROOVE,
        borderwidth=3,
    )
    frame1.place(relwidth=1, relheight=0.2)

    reciept = Label(frame1)
    reciept.configure(
        text = "Reciept",
        font=("", 20)
    )
    reciept.place(relx=0.38, rely=0.1)

    #=====================================================

    frame2 = Frame(mainframe)
    frame2.configure(
        relief = GROOVE,
        borderwidth=3,
    )
    frame2.place(relwidth=1, relheight=0.8, rely=0.2)

    chckoutname = Label(frame2)
    chckoutname.configure(
        text=checkoutname.upper() + ",",
        font=("", 15)
    )
    chckoutname.place(relx=0.1, rely=0.2)

    payment = Label(frame2)
    payment.configure(
        text = newtext,
        font=("", 15)
    )
    payment.place(relx=0.1, rely=0.35)

    payment2 = Label(frame2)
    payment2.configure(
        text = "for Php" + str(newprice) + ".",
        font=("", 15)
    )
    payment2.place(relx=0.1, rely=0.5)

    confirm = Button(frame2)
    confirm.configure(
        text="PAYMENT RECIEVED",
        font=("", 15),
        command=lambda: done(window, window2)
    )
    confirm.place(relx=0.2, rely=0.7)

    window2.mainloop()
    
    #=====================================================
    #=====================================================
    #=====================================================

class check_out:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("700x500")
        self.window.title("Guest Check Out")

        self.frame1 = Frame(self.window)
        self.frame1.configure(
            relief = GROOVE,
            borderwidth=3,
        )
        self.frame1.place(relheight=0.95, relwidth=0.96, relx=0.02, rely=0.02)

        self.frame2 = Frame(self.frame1)
        self.frame2.configure(
            relief = GROOVE,
            borderwidth=3,
        )
        self.frame2.place(relwidth=1, relheight=0.2)

        self.name = Label(self.frame2)
        self.name.configure(
            text="Guest Check Out",
            font=("", 45),
        )
        self.name.pack(pady=20)

        #=====================================================

        self.frame3 = Frame(self.frame1)
        self.frame3.configure(
            relief = GROOVE,
            borderwidth=3,
        )
        self.frame3.place(relwidth=0.5, relheight=0.3, rely=0.2 )

        self.check = Label(self.frame3)
        self.check.configure(
            text="Enter Name                   :",
            font=("", 20)
        )
        self.check.place(relx=0.05, rely=0.15)

        self.number = Label(self.frame3)
        self.number.configure(
            text="Number of days spent   :",
            font=("", 20)
        )
        self.number.place(relx=0.05, rely=0.55)

        #=====================================================

        self.frame4 = Frame(self.frame1)
        self.frame4.configure(
            relief = GROOVE,
            borderwidth=3,
        )
        self.frame4.place(relwidth=0.5, relheight=0.3, rely=0.2, relx=0.5 )

        self.name = Entry(self.frame4)
        self.name.configure(
            font=("", 20)
        )
        self.name.place(relheight=0.25, relwidth=0.9, relx=0.05, rely=0.15)

        self.days = Entry(self.frame4)
        self.days.configure(
            font=("", 20)
        )
        self.days.place(relheight=0.25, relwidth=0.9, relx=0.05, rely=0.6)

        #=====================================================

        self.frame5 = Frame(self.frame1)
        self.frame5.configure(
            relief = GROOVE,
            borderwidth=3,
        )
        self.frame5.place(relwidth=1, relheight=0.5, rely=0.5,)

        self.end1 = Label(self.frame5)
        self.end1.configure(
            text="Thank You",
            font=("", 35),
        )
        self.end1.place(relx=0.1, rely=0.15)

        self.end2 = Label(self.frame5)
        self.end2.configure(
            text="for",
            font=("", 35),
        )
        self.end2.place(relx=0.23, rely=0.35)

        self.end3 = Label(self.frame5)
        self.end3.configure(
            text="Choosing Us",
            font=("", 35),
        )
        self.end3.place(relx=0.08, rely=0.55)

        self.submit = Button(self.frame5)
        self.submit.configure(
            text="CONFIRM",
            font=("", 25),
            command=lambda: confirm(self.name, self.days, self.window)
        )
        self.submit.place(relx=0.6, rely=0.15, relwidth=0.3)

        self.cancel = Button(self.frame5)
        self.cancel.configure(
            text="CANCEL",
            font=("", 25),
            command=lambda: self.window.destroy()
        )
        self.cancel.place(relx=0.6, rely=0.55, relwidth=0.3)

        self.window.mainloop()

checkout = check_out()