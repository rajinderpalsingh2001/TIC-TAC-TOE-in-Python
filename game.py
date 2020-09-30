from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from random import *
class tictactoe:
    def chk(self,buttons):

        if(flag==1):
            if(buttons["text"]=="" and self.click==True):
                buttons["text"]="O"
                self.click=False
            elif(buttons["text"]=="" and self.click ==False):
                buttons["text"]="X"
                self.click=True
            if(self.btn1["text"]=="X" and self.btn2["text"]=="X" and self.btn3["text"]=="X" or
            self.btn4["text"]=="X" and self.btn5["text"]=="X" and self.btn6["text"]=="X" or
            self.btn7["text"]=="X" and self.btn8["text"]=="X" and self.btn9["text"]=="X" or
            self.btn1["text"]=="X" and self.btn4["text"]=="X" and self.btn7["text"]=="X" or
            self.btn2["text"]=="X" and self.btn5["text"]=="X" and self.btn8["text"]=="X" or
            self.btn3["text"]=="X" and self.btn6["text"]=="X" and self.btn9["text"]=="X" or
            self.btn3["text"]=="X" and self.btn5["text"]=="X" and self.btn7["text"]=="X" or
            self.btn1["text"]=="X" and self.btn5["text"]=="X" and self.btn9["text"]=="X"):

                showinfo("Yehh!","X won the Game")
                self.gamewin.withdraw()
            if (self.btn1["text"] == "O" and self.btn2["text"] == "O" and self.btn3["text"] == "O" or
                    self.btn4["text"] == "O" and self.btn5["text"] == "O" and self.btn6["text"] == "O" or
                    self.btn7["text"] == "O" and self.btn8["text"] == "O" and self.btn9["text"] == "O" or
                    self.btn1["text"] == "O" and self.btn4["text"] == "O" and self.btn7["text"] == "O" or
                    self.btn2["text"] == "O" and self.btn5["text"] == "O" and self.btn8["text"] == "O" or
                    self.btn3["text"] == "O" and self.btn6["text"] == "O" and self.btn9["text"] == "O" or
                    self.btn3["text"] == "O" and self.btn5["text"] == "O" and self.btn7["text"] == "O" or
                    self.btn1["text"] == "O" and self.btn5["text"] == "O" and self.btn9["text"] == "O"):
                showinfo("Yehh!", "O won the Game")
                self.gamewin.withdraw()



        else:
            if(buttons["text"]=="" and self.click==True):
                buttons["text"]="X"
                self.click=False
            elif(buttons["text"]=="" and self.click==False):
                buttons["text"]="O"
                self.click=True
            if (self.btn1["text"] == "X" and self.btn2["text"] == "X" and self.btn3["text"] == "X" or
                    self.btn4["text"] == "X" and self.btn5["text"] == "X" and self.btn6["text"] == "X" or
                    self.btn7["text"] == "X" and self.btn8["text"] == "X" and self.btn9["text"] == "X" or
                    self.btn1["text"] == "X" and self.btn4["text"] == "X" and self.btn7["text"] == "X" or
                    self.btn2["text"] == "X" and self.btn5["text"] == "X" and self.btn8["text"] == "X" or
                    self.btn3["text"] == "X" and self.btn6["text"] == "X" and self.btn9["text"] == "X" or
                    self.btn3["text"] == "X" and self.btn5["text"] == "X" and self.btn7["text"] == "X" or
                    self.btn1["text"] == "X" and self.btn5["text"] == "X" and self.btn9["text"] == "X"):
                showinfo("Yehh!", "X won the Game")
                self.gamewin.withdraw()
            if (self.btn1["text"] == "O" and self.btn2["text"] == "O" and self.btn3["text"] == "O" or
                    self.btn4["text"] == "O" and self.btn5["text"] == "O" and self.btn6["text"] == "O" or
                    self.btn7["text"] == "O" and self.btn8["text"] == "O" and self.btn9["text"] == "O" or
                    self.btn1["text"] == "O" and self.btn4["text"] == "O" and self.btn7["text"] == "O" or
                    self.btn2["text"] == "O" and self.btn5["text"] == "O" and self.btn8["text"] == "O" or
                    self.btn3["text"] == "O" and self.btn6["text"] == "O" and self.btn9["text"] == "O" or
                    self.btn3["text"] == "O" and self.btn5["text"] == "O" and self.btn7["text"] == "O" or
                    self.btn1["text"] == "O" and self.btn5["text"] == "O" and self.btn9["text"] == "O"):
                showinfo("Yehh!", "O won the Game")
                self.gamewin.withdraw()

    def start(self):
        self.root.withdraw()
        self.click = True
        self.gamewin=Tk()
        self.gamewin.title("TIC-TAC-TOE")
        self.f4=Frame()
        a=""
        self.btn1 = Button(self.gamewin,text=a,command=lambda:[self.chk(self.btn1)])
        self.btn2 = Button(self.gamewin, text=a, command=lambda:[self.chk(self.btn2)])
        self.btn3 = Button(self.gamewin, text=a, command=lambda:[self.chk(self.btn3)])
        self.btn4 = Button(self.gamewin, text=a, command=lambda:[self.chk(self.btn4)])
        self.btn5 = Button(self.gamewin, text=a, command=lambda:[self.chk(self.btn5)])
        self.btn6 = Button(self.gamewin, text=a, command=lambda:[self.chk(self.btn6)])
        self.btn7 = Button(self.gamewin, text=a, command=lambda:[self.chk(self.btn7)])
        self.btn8 = Button(self.gamewin, text=a, command=lambda:[self.chk(self.btn8)])
        self.btn9 = Button(self.gamewin, text=a, command=lambda:[self.chk(self.btn9)])
        #----------
        self.btn1.grid_configure(ipadx=6,ipady=26)
        self.btn2.grid_configure(ipadx=6, ipady=26)
        self.btn3.grid_configure(ipadx=6, ipady=26)
        self.btn4.grid_configure(ipadx=6, ipady=26)
        self.btn5.grid_configure(ipadx=6, ipady=26)
        self.btn6.grid_configure(ipadx=6, ipady=26)
        self.btn7.grid_configure(ipadx=6, ipady=26)
        self.btn8.grid_configure(ipadx=6, ipady=26)
        self.btn9.grid_configure(ipadx=6, ipady=26)


        #----------

        self.btn1.grid(row=0,column=0)
        self.btn2.grid(row=0,column=1)
        self.btn3.grid(row=0,column=2)

        self.btn4.grid(row=1, column=0)
        self.btn5.grid(row=1, column=1)
        self.btn6.grid(row=1, column=2)

        self.btn7.grid(row=2, column=0)
        self.btn8.grid(row=2, column=1)
        self.btn9.grid(row=2, column=2)
        #------------

        self.gamewin.mainloop()

    def submit(self):
        global flag
        if(self.gh.get()=="O"):
            self.playerinfo1=Label(self.f3,text="O......is of Player 1\nX......is of Player 2")
            flag=1
            self.playerinfo1.grid(row=5,column=0)
            self.startbtn.grid(row=6, column=0)
        elif(self.gh.get()=="X"):
            flag=0
            self.playerinfo1 = Label(self.f3, text="X......is of Player 1\nO......is of Player 2")
            self.playerinfo1.grid(row=5,column=0)
            self.startbtn.grid(row=6, column=0)

    def __init__(self):
        self.root=Tk()
        self.f1=Frame(self.root)
        self.f2=Frame(self.root)
        self.f3 = Frame(self.root)
        self.heading=Label(self.f1,text="TIC-TAC-TOE")
        self.lb1=Label(self.f2,text="Select For Player 1")
        self.gh = StringVar(self.f2, "X")
        self.gh = StringVar(self.f2, "O")
        self.rd1=Radiobutton(self.f2,text="O", var=self.gh, value="O")
        self.rd2=Radiobutton(self.f2,text="X", var=self.gh, value="X")
        self.submitbtn=Button(self.f2,text="Submit",command=self.submit)
        self.startbtn=Button(self.f3,text="Start",command=self.start)

        self.heading.grid(row=0,column=1)
        self.lb1.grid(row=1,column=0)
        self.rd1.grid(row=2,column=0)
        self.rd2.grid(row=2, column=1)
        self.submitbtn.grid(row=3,column=0)


        self.f1.pack()
        self.f2.pack()
        self.f3.pack()
        self.root.mainloop()
#----------------
obj=tictactoe()