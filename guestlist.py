from tkinter import *
import pickle

class guestlist:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("700x500")
        self.window.title("Guest List")

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
            text="Guest List",
            font=("", 45),
        )
        self.name.pack(pady=20)

        #=====================================================

        self.frame3 = Frame(self.frame1)
        self.frame3.configure(
            relief = GROOVE,
            borderwidth=3,
            background="light gray"
        )
        self.frame3.place(relwidth=1, relheight=0.8, rely=0.2)

        self.listname = Label(self.frame3)
        self.listname.configure(
            text="LIST",
            font=("", 30),
            background="light gray"
        )
        self.listname.place(relx=0.3, rely=0.05)

        self.list = Listbox(self.frame3)
        self.list.configure(
            font=("", 25)
        )
        self.list.place(rely=0.2, relx=0.1, relheight=0.7, relwidth=0.5)

        #it reads the namedata file and display it in the listbox above
        filename = "namedata"
        output_file = open(filename, 'rb')
        object = []
        num = 1
        while True:
            try:
                object.append(pickle.load(output_file))
            except EOFError:
                break
        output_file.close()

        for items in object:
            self.list.insert(END, str(num) + ". " + items.upper())
            num=num+1

        #to close the window and get back to the home page
        self.exit = Button(self.frame3)
        self.exit.configure(
            text="EXIT",
            font=("", 25),
            command=lambda: self.window.destroy()
        )
        self.exit.place(relx=0.75, rely=0.7)

        self.window.mainloop()


glist = guestlist()
