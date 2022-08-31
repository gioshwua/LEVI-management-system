from tkinter import *
import pickle
#it close the first and secondary window 
#and let the user get back to the home page
def exit(window, window2):
    window.destroy()
    window2.destroy()

def submit(name2, addressI, mobile, window, pay1, pay2):

    name = name2.get()
    address = addressI.get()
    number = mobile.get()
    MOD1 = pay1.get()
    MOD2 = pay2.get()

    #to store the names 
    filename = "namedata"
    input_file1 = open(filename, 'ab')
    pickle.dump(name, input_file1)
    input_file1.close()

    #to store the address
    filename = "addressdata"
    input_file2 = open(filename, 'ab')
    pickle.dump(address, input_file2)
    input_file2.close()

    #to store the contact number
    filename = "numberdata"
    input_file3 = open(filename, 'ab')
    pickle.dump(number, input_file3)
    input_file3.close()

    #to store how will the customer will pay
    if MOD1 == 1 and MOD2 == 0:
        creditcard = "will be paying using credit card"
        print(creditcard)
        filename = "MODdata"
        input_file4 = open(filename, 'ab')
        pickle.dump(creditcard, input_file4)
        input_file4.close()
    elif MOD1 == 0 and MOD2 == 1:
        cash="will be paying in cash"
        print(cash)
        filename = "MODdata"
        input_file4 = open(filename, 'ab')
        pickle.dump(cash, input_file4)
        input_file4.close()
    else:
        print("ERROR")

    #=====================================================

    window2 = Tk()
    window2.geometry("300x200")

    pop = Label(window2)
    pop.configure(
        text="SAVED",
        font=("", 30)
    )
    pop.pack(pady=25)

    butt = Button(window2)
    butt.configure(
        text="OK",
        font=("", 25),
        command= lambda: exit(window, window2)
    )
    butt.pack(pady=30)
    window2.mainloop()
            
    print(name + "\n" + address + "\n" + number)

class check_in:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("700x500")
        self.window.title("Guest Check In")
        
        self.pay1 = IntVar()
        self.pay2 = IntVar()
        
        self.frame1 = Frame(self.window)
        self.frame1.configure(
            relief = GROOVE,
            borderwidth=3,
        )
        self.frame1.place(relheight=0.95, relwidth=0.96, relx=0.02, rely=0.02)

        self.frame5 = Frame(self.frame1)
        self.frame5.configure(
            relief = GROOVE,
            borderwidth=3,
        )
        self.frame5.place(relwidth=1, relheight=0.2)

        self.name = Label(self.frame5)
        self.name.configure(
            text="Guest Check In",
            font=("", 45),
        )
        self.name.pack(pady=20)

        #=====================================================

        self.frame2 = Frame(self.frame1)
        self.frame2.configure(
            relief = GROOVE,
            borderwidth=3,
        )
        self.frame2.place(relheight=0.5, relwidth=0.45, rely=0.2)

        self.name1 = Label(self.frame2)
        self.name1.configure(
            text="Enter Your Name                   :",
            font=("", 15),
        )
        self.name1.place(relx=0.03, rely=0.1)

        self.address = Label(self.frame2)
        self.address.configure(
            text="Enter Your Address               :",
            font=("", 15),
        )
        self.address.place(relx=0.03, rely=0.4)

        self.contact = Label(self.frame2)
        self.contact.configure(
            text="Enter Your Contact Number    :",
            font=("", 15),
        )
        self.contact.place(relx=0.03, rely=0.7)

        #=====================================================

        self.frame3 = Frame(self.frame1)
        self.frame3.configure(
            relief = GROOVE,
            borderwidth=3,
        )
        self.frame3.place(relheight=0.5, relwidth=0.55, relx=0.45, rely=0.2)

        self.name2 = Entry(self.frame3)
        self.name2.configure(
            font=("", 20),
        )
        self.name2.place(relheight=0.15, relwidth=0.9, relx=0.05, rely=0.1)

        self.addressI = Entry(self.frame3)
        self.addressI.configure(
            font=("", 20)
        )
        self.addressI.place(relheight=0.15, relwidth=0.9, relx=0.05, rely=0.4)

        self.mobile = Entry(self.frame3)
        self.mobile.configure(
            font=("", 20)
        )
        self.mobile.place(relheight=0.15, relwidth=0.9, relx=0.05, rely=0.7)

        #=====================================================

        self.frame4 = Frame(self.frame1)
        self.frame4.configure(
            relief = GROOVE,
            borderwidth=3,
        )
        self.frame4.place(relheight=0.3, relwidth=1, rely=0.7)

        self.pay = Label(self.frame4)
        self.pay.configure(
            text="Mode of Payment :",
            font=("", 20)
        )
        self.pay.place(relx=0.05, rely=0.05)

        self.card = Checkbutton(self.frame4)
        self.card.configure(
            text="Credit Card",
            font=("", 15),
            variable=self.pay1,
            onvalue=1,
            offvalue=0,

        )
        self.card.place(relx=0.05, rely=0.5)

        self.cash = Checkbutton(self.frame4)
        self.cash.configure(
            text="Cash",
            font=("", 15),
            variable=self.pay2,
            onvalue=1,
            offvalue=0,
        )
        self.cash.place(relx=0.3, rely=0.5)

        self.submit = Button(self.frame4)
        self.submit.configure(
            text="SUBMIT",
            font=("", 20),
            command= lambda: submit(self.name2, self.addressI, self.mobile, self.window, self.pay1, self.pay2)
        )
        self.submit.place(relx=0.75, rely=0.3)

        self.cancel = Button(self.frame4)
        self.cancel.configure(
            text="CANCEL",
            font=("", 20),
            command=lambda: self.window.destroy()
        )
        self.cancel.place(relx=0.45, rely=0.3)

        self.window.mainloop()

checkin = check_in()