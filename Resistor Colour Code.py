from tkinter import *
import tkinter.messagebox as tmsg
from  tkinter import ttk

class Resistor:

    def __init__(self,root):
        self.root = root
        self.root.title("Resistor Color Code Calculator")
        self.root.geometry("1350x652+0+0")
        self.root.configure(background = "pink")

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = StringVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()

        var1.set("")
        var2.set("")
        var3.set("")
        var4.set("")
        var5.set("")
        var6.set("")
        var7.set("")
        var8.set("")

        var9 = IntVar()
        var9.set("")

        def Band1_Black():
            var1.set(0)
        def Band1_Brown():
            var1.set(1)
        def Band1_Red():
            var1.set(2)
        def Band1_Orange():
            var1.set(3)
        def Band1_Yellow():
            var1.set(4)
        def Band1_Green():
            var1.set(5)
        def Band1_Blue():
            var1.set(6)
        def Band1_Violet():
            var1.set(7)
        def Band1_Gray():
            var1.set(8)
        def Band1_White():
            var1.set(9)
        #===============================================================================================================
        def Band2_Black():
            var2.set(0)
        def Band2_Brown():
            var2.set(1)
        def Band2_Red():
            var2.set(2)
        def Band2_Orange():
            var2.set(3)
        def Band2_Yellow():
            var2.set(4)
        def Band2_Green():
            var2.set(5)
        def Band2_Blue():
            var2.set(6)
        def Band2_Violet():
            var2.set(7)
        def Band2_Gray():
            var2.set(8)
        def Band2_White():
            var2.set(9)
        #=============================================================================================================
        def Mult_Black():
            var3.set(1)
        def Mult_Brown():
            var3.set(10)
        def Mult_Red():
            var3.set(100)
        def Mult_Orange():
            var3.set(1000)
        def Mult_Yellow():
            var3.set(10000)
        def Mult_Green():
            var3.set(100000)
        def Mult_Blue():
            var3.set(1000000)
        def Mult_Violet():
            var3.set(10000000)
        def Mult_Gray():
            var3.set(100000000)
        def Mult_White():
            var3.set(1000000000)
        #==============================================================================================================
        def Tol_Gold():
            var4.set(0.05)
        def Tol_Silver():
            var4.set(0.1)
        def Tol_None():
            var4.set(0.2)
        #===============================================================================================================
        def iReset():
            iReset = tmsg.askyesno("Resistor Color Code Calculator","Confirm if you want to exit?")
            if iReset > 0:
                var1.set("")
                var2.set("")
                var3.set("")
                var4.set("")
                var5.set("")
                var6.set("")
                var7.set("")
                var8.set("")
                var9.set("")
                return

        def iExit():
            iExit = tmsg.askyesno("Resistor Color Code Calculator","Confirm if you want to reset?")
            if iExit > 0:
                root.destroy()
                return

        def CalculateResistor():
            var9 = "%d%d" % ((var1.get(),var2.get()))
            t = float(var9)
            m = float(var3.get())
            s = float(var4.get())
            if (s == 0.05):
                q = (((t*m)/1000)*0.05)
                a = (q)
                var5.set(str('%.1f'%(a)))
                var6.set(str('%.1f'%(t))+ 'K ohm')
                var7.set(str('%.1f'%(t - q))+ 'K ohm')
                var8.set(str('%.1f'%(t + q))+ 'K ohm')

            elif (s == 0.1):
                q = (((t*m)/1000)*0.1)
                a = (q)
                var5.set(str('%.1f'%(a)))
                var6.set(str('%.1f'%(t))+ 'K ohm')
                var7.set(str('%.1f'%(t - q))+ 'K ohm')
                var8.set(str('%.1f'%(t + q))+ 'K ohm')

            elif (s == 0.2):
                q = (((t*m)/1000)*0.2)
                a = (q)
                var5.set(str('%.1f'%(a)))
                var6.set(str('%.1f'%(t))+ 'K ohm')
                var7.set(str('%.1f'%(t - q))+ 'K ohm')
                var8.set(str('%.1f'%(t + q))+ 'K ohm')






        mainFrame = Frame(self.root,bg="pink")
        mainFrame.grid()

        TitleFrame = Frame(mainFrame, bd=10, width =1350, padx = 20, relief = RIDGE,bg="pink")
        TitleFrame.grid(row=0,column=0,columnspan=2,sticky=W)
        self.lblTitle = Label(TitleFrame,font = "arial 40 bold", text = "Resistor Color Code Calculator",padx = 244,bg="pink")
        self.lblTitle.grid()

        ResistorFrame = Frame(mainFrame, bd=10, width =1350, padx = 20, relief = RIDGE,bg="pink")
        ResistorFrame.grid(row=1,column=0,sticky=W)

        IndicatorFrame = Frame(mainFrame, bd=10, width =1350, padx = 20, relief = RIDGE,bg="pink")
        IndicatorFrame.grid(row=1,column=1,sticky=W)

        self.lblTitle = Label(ResistorFrame,font = "arial 13 bold", text = "1st Band",bg="pink")
        self.lblTitle.grid(row=0,column=0)
        self.lblTitle = Label(ResistorFrame,font = "arial 13 bold", text = "2nd Band",bg="pink")
        self.lblTitle.grid(row=0,column=1)
        self.lblTitle = Label(ResistorFrame,font = "arial 13 bold", text = "Multiplier",bg="pink")
        self.lblTitle.grid(row=0,column=2)
        self.lblTitle = Label(ResistorFrame,font = "arial 13 bold", text = "Tolerance",bg="pink")
        self.lblTitle.grid(row=0,column=3)

        self.black1 = Button(ResistorFrame, width = 17,font = "arial 14 bold", text ="Black", fg="White",bg="black",
                             command=Band1_Black)
        self.black1.grid(row=1,column=0)
        self.black2 = Button(ResistorFrame, width=17, font="arial 14 bold", text="0", fg="White", bg="black",
                             command=Band2_Black)
        self.black2.grid(row=1, column=1)
        self.black3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="1", fg="White", bg="black",
                             command=Mult_Black)
        self.black3.grid(row=1, column=2)
        self.black4 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="White", bg="black")
        self.black4.grid(row=1, column=3)
        #=============================================================================================================
        self.brown1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="Brown", fg="black", bg="brown",
                             command=Band1_Brown)
        self.brown1.grid(row=2, column=0)
        self.brown2 = Button(ResistorFrame, width=17, font="arial 14 bold", text="1", fg="black", bg="brown",
                             command=Band2_Brown)
        self.brown2.grid(row=2, column=1)
        self.brown3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="10", fg="black", bg="brown",
                             command=Mult_Brown)
        self.brown3.grid(row=2, column=2)
        self.brown4 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="brown")
        self.brown4.grid(row=2, column=3)
        #===============================================================================================================
        self.red1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="Red", fg="black", bg="red",
                           command=Band1_Red)
        self.red1.grid(row=3, column=0)
        self.red2 = Button(ResistorFrame, width=17, font="arial 14 bold", text="2", fg="black", bg="red",
                           command=Band2_Red)
        self.red2.grid(row=3, column=1)
        self.red3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="100", fg="black",bg="red",
                           command=Mult_Red)
        self.red3.grid(row=3, column=2)
        self.red4 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="red")
        self.red4.grid(row=3, column=3)
        #===============================================================================================================
        self.orange1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="Orange", fg="black", bg="orange",
                              command=Band1_Orange)
        self.orange1.grid(row=4, column=0)
        self.orange2 = Button(ResistorFrame, width=17, font="arial 14 bold", text="3", fg="black", bg="orange",
                              command=Band2_Orange)
        self.orange2.grid(row=4, column=1)
        self.orange3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="1000", fg="black", bg="orange",
                              command=Mult_Orange)
        self.orange3.grid(row=4, column=2)
        self.orange4 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="orange")
        self.orange4.grid(row=4, column=3)
        #==============================================================================================================
        self.yellow1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="Yellow", fg="black", bg="yellow",
                              command=Band1_Yellow)
        self.yellow1.grid(row=5, column=0)
        self.yellow2 = Button(ResistorFrame, width=17, font="arial 14 bold", text="4", fg="black", bg="yellow",
                              command=Band2_Yellow)
        self.yellow2.grid(row=5, column=1)
        self.yellow3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="10000", fg="black", bg="yellow",
                              command=Mult_Yellow)
        self.yellow3.grid(row=5, column=2)
        self.yellow4 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="yellow")
        self.yellow4.grid(row=5, column=3)
        #==============================================================================================================
        self.green1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="Green", fg="black", bg="green",
                             command=Band1_Green)
        self.green1.grid(row=6, column=0)
        self.green2 = Button(ResistorFrame, width=17, font="arial 14 bold", text="5", fg="black", bg="green",
                             command=Band2_Green)
        self.green2.grid(row=6, column=1)
        self.green3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="100000", fg="black", bg="green",
                             command=Mult_Green)
        self.green3.grid(row=6, column=2)
        self.green4 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="green")
        self.green4.grid(row=6, column=3)
        #==============================================================================================================
        self.blue1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="Blue", fg="black", bg="blue",
                            command=Band1_Blue)
        self.blue1.grid(row=7, column=0)
        self.blue2 = Button(ResistorFrame, width=17, font="arial 14 bold", text="6", fg="black", bg="blue",
                            command=Band2_Blue)
        self.blue2.grid(row=7, column=1)
        self.blue3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="1000000", fg="black", bg="blue",
                            command=Mult_Blue)
        self.blue3.grid(row=7, column=2)
        self.blue4 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="blue")
        self.blue4.grid(row=7, column=3)
        #=============================================================================================================
        self.violet1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="Violet", fg="black", bg="violet",
                              command=Band1_Violet)
        self.violet1.grid(row=8, column=0)
        self.violet2 = Button(ResistorFrame, width=17, font="arial 14 bold", text="7", fg="black", bg="violet",
                              command=Band2_Violet)
        self.violet2.grid(row=8, column=1)
        self.violet3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="10000000", fg="black", bg="violet",
                              command=Mult_Violet)
        self.violet3.grid(row=8, column=2)
        self.violet4 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="violet")
        self.violet4.grid(row=8, column=3)
        #=============================================================================================================
        self.gray1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="Gray", fg="black", bg="gray",
                            command=Band1_Gray)
        self.gray1.grid(row=9, column=0)
        self.gray2 = Button(ResistorFrame, width=17, font="arial 14 bold", text="8", fg="black", bg="gray",
                            command=Band2_Gray)
        self.gray2.grid(row=9, column=1)
        self.gray3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="100000000", fg="black", bg="gray",
                            command=Mult_Gray)
        self.gray3.grid(row=9, column=2)
        self.gray4 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="gray")
        self.gray4.grid(row=9, column=3)
        #=============================================================================================================
        self.white1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="White", fg="black", bg="white",
                             command=Band1_White)
        self.white1.grid(row=10, column=0)
        self.white2 = Button(ResistorFrame, width=17, font="arial 14 bold", text="9", fg="black", bg="white",
                             command=Band2_White)
        self.white2.grid(row=10, column=1)
        self.white3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="1000000000", fg="black", bg="white",
                             command=Mult_White)
        self.white3.grid(row=10, column=2)
        self.white4 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="white")
        self.white4.grid(row=10, column=3)
        #=============================================================================================================
        self.gold1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="Gold", fg="black", bg="gold",
                            command=Tol_Gold)
        self.gold1.grid(row=11, column=0)
        self.gold2 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="gold")
        self.gold2.grid(row=11, column=1)
        self.gold3 = Button(ResistorFrame, width=17, font="arial 14 bold", text="0.1", fg="black", bg="gold")
        self.gold3.grid(row=11, column=2)
        self.gold4 = Button(ResistorFrame, width=17, font="arial 14 bold", text="5%", fg="black", bg="gold",
                            command=Tol_Gold)
        self.gold4.grid(row=11, column=3)
        #=============================================================================================================
        self.Silver1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="Silver", fg="black", bg="Silver",
                              command=Tol_Silver)
        self.Silver1.grid(row=12, column=0)
        self.Silver2 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="Silver")
        self.Silver2.grid(row=12, column=1)
        self.Silver3 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="Silver")
        self.Silver3.grid(row=12, column=2)
        self.Silver4 = Button(ResistorFrame, width=17, font="arial 14 bold", text="10%", fg="black", bg="Silver",
                              command=Tol_Silver)
        self.Silver4.grid(row=12, column=3)
        #=============================================================================================================
        self.None1 = Button(ResistorFrame, width=17, font="arial 14 bold", text="None", fg="black", bg="white",
                            command=Tol_None)
        self.None1.grid(row=13, column=0)
        self.None2 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="white")
        self.None2.grid(row=13, column=1)
        self.None3 = Button(ResistorFrame, width=17, font="arial 14 bold", fg="black", bg="white")
        self.None3.grid(row=13, column=2)
        self.None4 = Button(ResistorFrame, width=17, font="arial 14 bold", text="20%", fg="black", bg="white",
                            command=Tol_None)
        self.None4.grid(row=13, column=3)
        #=================================Indicator Frame ============================================================

        self.lblFirst = Label(IndicatorFrame,font = "arial 15 bold", text = "1st Band",bg="pink")
        self.lblFirst.grid(row=0,column=0,sticky=W,pady=10,columnspan=3)
        self.txtFirst = Entry(IndicatorFrame,font = "arial 15 bold",width = 16,textvariable=var1)
        self.txtFirst.grid(row=0,column=1,pady=10,columnspan=3)

        self.lblSecond = Label(IndicatorFrame,font = "arial 15 bold", text = "2nd Band",bg="pink")
        self.lblSecond.grid(row=1,column=0,sticky=W,pady=10,columnspan=3)
        self.txtSecond = Entry(IndicatorFrame,font = "arial 15 bold",width = 16,textvariable=var2)
        self.txtSecond.grid(row=1,column=1,pady=10,columnspan=3)


        self.lblMult = Label(IndicatorFrame,font = "arial 15 bold", text = "Multiplier",bg="pink")
        self.lblMult.grid(row=2,column=0,sticky=W,pady=10,columnspan=3)
        self.txtMult = Entry(IndicatorFrame,font = "arial 15 bold",width = 16,textvariable=var3)
        self.txtMult.grid(row=2,column=1,pady=10,columnspan=3)

        self.lblDivideBy1000 = Label(IndicatorFrame,font = "arial 15 bold", text = "Div.By1000",bg="pink")
        self.lblDivideBy1000.grid(row=4,column=0,sticky=W,pady=10,columnspan=3)
        self.txtDivideBy1000 = Entry(IndicatorFrame,font = "arial 15 bold",width = 16,textvariable=var5)
        self.txtDivideBy1000.grid(row=4,column=1,pady=10,columnspan=3)

        self.lblTolerance = Label(IndicatorFrame, font="arial 15 bold", text="Tolerance", bg="pink")
        self.lblTolerance.grid(row=3, column=0, sticky=W,pady=10,columnspan=3)
        self.txtTolerance = Entry(IndicatorFrame, font="arial 15 bold", width=16,textvariable=var4)
        self.txtTolerance.grid(row=3, column=1,pady=10,columnspan=3)

        self.lblResistorVal = Label(IndicatorFrame, font="arial 15 bold", text="Resistor Val", bg="pink")
        self.lblResistorVal.grid(row=5, column=0, sticky=W,pady=10,columnspan=3)
        self.txtResistorVal = Entry(IndicatorFrame, font="arial 15 bold", width=16,textvariable=var6)
        self.txtResistorVal.grid(row=5, column=1,pady=10,columnspan=3)

        self.lblMinRange = Label(IndicatorFrame, font="arial 15 bold", text="Min.Range", bg="pink")
        self.lblMinRange.grid(row=6, column=0, sticky=W,pady=10,columnspan=3)
        self.txtMinRange = Entry(IndicatorFrame, font="arial 15 bold", width=16,textvariable=var7)
        self.txtMinRange.grid(row=6, column=1,pady=10,columnspan=3)

        self.lblMaxRange = Label(IndicatorFrame, font="arial 15 bold", text="Max.Range", bg="pink")
        self.lblMaxRange.grid(row=7, column=0, sticky=W,pady=10)
        self.txtMaxRange = Entry(IndicatorFrame, font="arial 15 bold", width=16,textvariable=var8)
        self.txtMaxRange.grid(row=7, column=1,pady=10,columnspan=3)

        Calc = Button(IndicatorFrame,font="arial 18 bold", width=8,text="Calculate",height=3,command=CalculateResistor)
        Calc.grid(row=8, column=0,pady=10)
        Reset = Button(IndicatorFrame,font="arial 18 bold", width=8,text="Reset",height=3,command=iReset)
        Reset.grid(row=8, column=1,pady=10)
        Exit = Button(IndicatorFrame,font="arial 18 bold", width=8,text="Exit",height=3,command=iExit)
        Exit.grid(row=8, column=2,pady=10,sticky = W)



if __name__ == '__main__':
    root = Tk()
    application = Resistor(root)
    root.mainloop()
