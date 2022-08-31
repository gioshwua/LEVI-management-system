from cProfile import label
from tkinter import*

#to compute how much the customer will be paying 
#for the selected items
def compute(var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, self):
    ans = var1.get() + var2.get() + var3.get() + var4.get() + var5.get()+var6.get()+var7.get() + \
        var8.get()+var9.get()+var10.get()+var11.get() + \
        var12.get()+var13.get()+var14.get()

    self.disp.configure(text=ans)

#it close the first and secondary window 
#and let the user get back to the home page
def close(window, window2):
    window.destroy()
    window2.destroy()

#secondary window to show that the customer made a payment
def pay(window):
    window2 = Tk()
    window2.geometry("350x250")

    pop = Label(window2)
    pop.configure(
        text="PAYMENT",
        font=("", 15)
    )
    pop.pack(pady=15)

    pop2 = Label(window2)
    pop2.configure(
        text="RECEIEVED",
        font=("", 15)
    )
    pop2.pack(pady=20)

    butt = Button(window2)
    butt.configure(
        text="OK",
        font=("", 25),
        command=lambda: close(window, window2)
    )
    butt.pack(pady=30)
    window2.mainloop()


class food:
    def __init__(self):

        self.window = Tk()
        self.window.geometry("700x500")
        self.window.title("FOOD CART")

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.var12 = IntVar()
        self.var13 = IntVar()
        self.var14 = IntVar()

        #FRAME1

        self.frame1 = Frame(
            self.window,
            bd=3,
            relief=SUNKEN)
        self.frame1.place(relheight=.5, relwidth=0.5, relx=0, rely=0)

        self.label = Label(
            self.frame1, text="STARTERS",
            font=("italic", 15)
        ).place(relx=0.35, rely=0.05)

        self.start1 = Checkbutton(
            self.frame1,
            text="BREAD BASKET (100)",
            variable=self.var1,
            onvalue=100,
            offvalue=0
        ).place(relx=0.2, rely=0.2)

        self.start2 = Checkbutton(
            self.frame1,
            text="GARLIC & CHEESE BREAD (90)",
            variable=self.var2,
            onvalue=90,
            offvalue=0
        ).place(relx=0.2, rely=0.3)

        self.start3 = Checkbutton(
            self.frame1,
            text="GARLIC MUSHROOM (75)",
            variable=self.var3,
            onvalue=75,
            offvalue=0
        ).place(relx=0.2, rely=0.4)

        self.start4 = Checkbutton(
            self.frame1,
            text="CALAMARES (120)",
            variable=self.var4,
            onvalue=120,
            offvalue=0
        ).place(relx=0.2, rely=0.5)

        self.start5 = Checkbutton(
            self.frame1,
            text="TOSTADILLAS (60)",
            variable=self.var5,
            onvalue=60,
            offvalue=0
        ).place(relx=0.2, rely=0.6)

        self.start6 = Checkbutton(
            self.frame1,
            text="SPICY SCALLOP (95)",
            variable=self.var6,
            onvalue=95,
            offvalue=0
        ).place(relx=0.2, rely=0.7)

        #FRAME2

        self.frame2 = Frame(
            self.window,
            bd=3,
            relief=SUNKEN
        )
        self.frame2.place(relheight=1, relwidth=0.5, relx=.5, rely=0)

        self.label2 = Label(
            self.frame2, text="MAIN MENU",
            font=("italic", 15)).place(relx=0.3, rely=0.02)

        self.ulam1 = Checkbutton(
            self.frame2,
            text="SALT AND PEPPER CALAMARI (120)",
            variable=self.var7,
            onvalue=120,
            offvalue=0
        ).place(relx=0.2, rely=0.1)

        self.ulam2 = Checkbutton(
            self.frame2,
            text="TASMANIAN SALMON (135)",
            variable=self.var8,
            onvalue=135,
            offvalue=0
        ).place(relx=0.2, rely=0.15)

        self.ulam3 = Checkbutton(
            self.frame2,
            text="CHICKEN ROULADE (105)",
            variable=self.var9,
            onvalue=105,
            offvalue=0
        ).place(relx=0.2, rely=0.2)
        
        self.ulam3 = Checkbutton(
            self.frame2,
            text="EGGPLANT BRUSHCETTA (60)",
            variable=self.var10,
            onvalue=60,
            offvalue=0
        ).place(relx=0.2, rely=0.25)

        #FRAME3

        self.frame3 = Frame(
            self.window,
            bd=3,
            relief=SUNKEN)

        self.frame3.place(relheight=0.5, relwidth=0.5, relx=0, rely=.5)

        self.label = Label(
            self.frame3,
            text="DESSERT",
            font=("italic", 15)
        ).place(relx=0.3, rely=0.05)

        self.dessert1 = Checkbutton(
            self.frame3,
            text="CREME BRULEE (75)",
            variable=self.var11,
            onvalue=75,
            offvalue=0
        ).place(relx=0.2, rely=0.2)

        self.dessert2 = Checkbutton(
            self.frame3,
            text="HAZELNUT CHEESECAKE (35)",
            variable=self.var12,
            onvalue=35,
            offvalue=0
        ).place(relx=0.2, rely=0.3)

        self.dessert3 = Checkbutton(
            self.frame3,
            text="HALO-HALO (90)",
            variable=self.var13,
            onvalue=90,
            offvalue=0
        ).place(relx=0.2, rely=0.4)

        self.dessert4 = Checkbutton(
            self.frame3,
            text="FRESH FRUIT TART (130)",
            variable=self.var14,
            onvalue=130,
            offvalue=0
        ).place(relx=0.2, rely=0.5)

        #FRAME4

        self.frame4 = Frame(
            self.window,
            bd=3,
            relief=SUNKEN
        )
        self.frame4.place(relheight=.5, relwidth=0.5, relx=.5, rely=.5)

        self.label = Label(
            self.frame4,
            text="RECEIPT",
            font=("italic", 15)
        ).place(relx=0.4, rely=0.05)

        self.display1 = Label(
            self.frame4,
            font=("Italic", 10)
        ).pack()

        self.com = Button(
            self.frame4,
            text="COMPUTE",
            command=lambda: compute(self.var1, self.var2, self.var3, self.var4, self.var5,
                                    self.var6, self.var7, self.var8, self.var9, self.var10, 
                                    self.var11, self.var12, self.var13, self.var14, self),
            font=("", 15)
        ).place(relx=0.1, rely=0.45)

        self.pay = Label(
            self.frame4,
            text="You neeed to pay php: ",
            font=("Italic")
        )

        self.disp = Label(
            self.frame4,
            font=("italic", 20),
            relief=SUNKEN,
            bd=5,
            text="0"
        )
        self.pay.place(x=20, y=70)
        self.disp.place(relx=0.7, rely=0.25)

        self.back = Button(
            self.frame4,
            text="CLOSE",
            command=exit,
            font=("italic", 15),
        ).place(relx=0.2, rely=0.7)

        self.pay = Button(
            self.frame4,
            text="PAY",
            command=lambda: pay(self.window),
            font=("italic", 15),
        ).place(relx=0.6, rely=0.7)

        self.window.mainloop()


food = food()
