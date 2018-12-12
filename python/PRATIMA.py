from tkinter import*
import tkinter.messagebox
from tkinter import Tk,StringVar,ttk
import time
import datetime
root=Tk()
root.geometry("1350x750+0+0")
frame1=Frame(root,width=1350,height=90,bd=10,relief="raise")
frame1.pack(side=TOP)
labelTitle=Label(frame1,text="TICKET BOOKING SYSTEM",font=("arial",80),anchor='w')

frame2=Frame(root,width=750,height=1000,bd=10,relief="raise",bg="black")
frame2.pack(side=LEFT)
frame3=Frame(root,width=650,height=1000,bd=10,relief="raise",bg="black")
frame3.pack(side=RIGHT)
frame2a=Frame(frame2,width=750,height=400,bd=10,relief="raise",bg="black")
frame2a.pack(side=TOP)
frame2b=Frame(frame2,width=750,height=700,bd=10,relief="raise",bg="black")
frame2b.pack(side=BOTTOM)

frame2a1=Frame(frame2a,width=250,height=300,bd=9,relief="raise")
frame2a1.pack(side=LEFT)
frame2a2=Frame(frame2a,width=250,height=300,bd=9,relief="raise")
frame2a2.pack(side=RIGHT)
frame2a3=Frame(frame2a,width=250,height=300,bd=9,relief="raise")
frame2a3.pack(side=RIGHT)

frame2b1=Frame(frame2b,width=500,height=700,bd=9,relief="raise")
frame2b1.pack(side=LEFT)
frame2b2=Frame(frame2b,width=200,height=700,bd=9,relief="raise")
frame2b2.pack(side=RIGHT)


#-------------------------------variable----------------------------------------------#
time1=StringVar()
date1=StringVar()
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var7.set("select")
var8=StringVar()
var9=StringVar()
var10=StringVar()
var11=StringVar()
item1=IntVar()
a=IntVar()

var12=IntVar()
class1=StringVar()
From3=StringVar()
From3.set(" ")
To=StringVar()
Total=StringVar()
Route=StringVar()
Child=StringVar()
Adult=StringVar()
Ticket=StringVar()
Refno=StringVar()
Tax=StringVar()
Time=StringVar()
date=StringVar()
Total=StringVar()
variable13=StringVar()
variable14=StringVar()

nticket=StringVar()
subtotal=StringVar()
total=StringVar()
From3.set(" ")
To.set("  ")
var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("Rs 10")
var10.set("Rs 5")
var11.set(" ")
var12=IntVar()
nticket.set("0")
subtotal.set("0")
Tax.set("Rs 2")

total.set("0")

Label1=Label(frame1,text="TICKET BOOKING SYSTEM",font=("italic",50,"bold"),bd=5)
Label1.grid(row=0,column=0)
#-------------------------create widge top left-----------------------------------------------#
labelclass=Label(frame2a1,text="CLASS",font=("arrial",25,"bold"),fg="black",pady=20)
labelclass.grid(row=0,column=0,sticky=W)

ckstandard=Checkbutton(frame2a1,text="STANDARD\t",onvalue=1,offvalue=0,font=("arial",20,"bold"),fg="black",pady=10,variable=var1)
ckstandard.grid(row=1,column=0,sticky=W)
ckeconomy=Checkbutton(frame2a1,text="ECONOMY\t",onvalue=1,offvalue=0,font=("arial",20,"bold"),fg="black",pady=10,variable=var2)
ckeconomy.grid(row=2,column=0,sticky=W)
ckfirstclass=Checkbutton(frame2a1,text="FIRST CLASS\t",onvalue=1,offvalue=0,font=("arial",20,"bold"),fg="black",pady=10,variable=var3)
ckfirstclass.grid(row=3,column=0,sticky=W)


#---------------------create widge top right-----------------------------------------------------#

label=Label(frame2a2,text="person",font=("arrial",20,"bold"),bd=5,pady=5)
label.grid(row=0,column=0,sticky=W)

check=Checkbutton(frame2a2,text="Adult\t\t",font=("arial",20,"bold"),onvalue=1,offvalue=0,pady=5,variable=var4)
check.grid(row=1,column=0,sticky=W)
checkchild=Checkbutton(frame2a2,text="child\t\t",font=("arial",20,"bold"),onvalue=1,offvalue=0,pady=15,variable=var5)
checkchild.grid(row=2,column=0,sticky=W)
label=Label(frame2a2,text="no of ticket",font=("arrial",20,"bold"),bd=5,pady=5)
label.grid(row=3,column=0)
ticketselect=ttk.Combobox(frame2a2,text="no.",font=("arrial",20,"bold"),width=10,textvariable=var12)
ticketselect['value']=['0','1','2','3','4','5']
ticketselect.current(0)
ticketselect.grid(row=4,column=0)

#----------------------craete widge top left2------------------------------------------------------#
labelsource=Label(frame2a3,text="source selector",font=("arrial",25,"bold"),bd=5,pady=20)
labelsource.grid(row=0,column=0,sticky=W)
cmbsource=ttk.Combobox(frame2a3,text="Source",font=("arrial",25,"bold"),width=15,textvariable=var7)
cmbsource['value']=['select','ambernaath','airoli','pune']
cmbsource.current(0)
cmbsource.grid(row=1,column=0)
labeldestination=Label(frame2a3,text="DESTINATION selector",font=("arrial",20,"bold"),bd=5,pady=30,)
labeldestination.grid(row=2,column=0,sticky=W)
cmbdestination=ttk.Combobox(frame2a3,text="destination",font=("arrial",20,"bold"),width=15,textvariable=var8)
cmbdestination['value']=['select','ghatkopar','kurla','vidyavihar']
cmbdestination.current(0)
cmbdestination.grid(row=3,column=0)

#------------------------Tax,SubTotal and Total--------------------------------------------------------------------------------------------------------------------



LblStateTax=Label(frame2b2,text="STATE TAX\t\t",font=("arial",20,"bold"),bd=5,pady=20,anchor=W)
LblStateTax.grid(row=0,column=0)
txtStateTax=Entry(frame2b2,font=("arial",10,"bold"),width=15,bd=10,textvariable=Tax,state='disabled')
txtStateTax.grid(row=0,column=1)


LblSubTotal=Label(frame2b2,text="NO OF TICKET\t\t",font=("arial",20,"bold"),bd=5,pady=20)
LblSubTotal.grid(row=1,column=0)
txtSubTotal=Entry(frame2b2,font=("arial",10,"bold"),width=15,bd=10,textvariable=nticket)
txtSubTotal.grid(row=1,column=1)


lblTotalTax=Label(frame2b2,text="TOTAL PRICE\t\t",font=("arial",20,"bold"),bd=5,pady=20)
lblTotalTax.grid(row=2,column=0)
txtTotalTax=Entry(frame2b2,font=("arial",10,"bold"),width=15,bd=10,textvariable=Total)
txtTotalTax.grid(row=2,column=1)


#-----------------------------------Ticket-----------------------------------------------------------------------------------------------------------------------------------------------

Label1=Label(frame2b1,text="TICKET TYPE",font=("arial",25,"bold"),bd=5,pady=15)
Label1.grid(row=0,column=0,sticky=W)
single=Radiobutton(frame2b1,text="SINGLE\t",value=1,font=("arial",20,"bold"),pady=10,variable=a)
single.grid(row=1,column=0,sticky=W)
entry=Entry(frame2b1,font=("arial",15,"bold"),width=5,bd=10,textvariable=var10,state='disabled')
entry.grid(row=1,column=1,sticky=W)


rdreturn=Radiobutton(frame2b1,text="RETURN\t",font=("arial",20,"bold"),value=2,pady=5,variable=a)
rdreturn.grid(row=2,column=0,sticky=W)
entry=Entry(frame2b1,font=("arial",15,"bold"),width=5,bd=10,textvariable=var9,state='disabled')
entry.grid(row=2,column=1,sticky=W)

labelcomment=Label(frame2b1,text="COMMENT",font=("arrial",20,"bold"),pady=10)
labelcomment.grid(row=3,column=0,sticky=W)
entrycomment=Entry(frame2b1,font=("arial",10,"bold"),width=10,bd=10,textvariable=var11)
entrycomment.grid(row=3,column=1,sticky=W)

frame31=Frame(frame3,width=650,height=100,bd=9,relief="raise")
frame31.pack(side=TOP)
labelReceipt=Label(frame31,text="TRAVELLING  TICKETING SYSTEM",bd=20,font=("arial",20,"bold"))
labelReceipt.pack()

frame32=Frame(frame3,width=650,height=800,bd=9,relief="raise")
frame32.pack(side=BOTTOM)

frame34=Frame(frame32,width=650,height=400,bd=0,relief="raise")
frame34.pack(side=TOP)
frame35=Frame(frame32,width=650,height=600,bd=0,relief="raise")
frame35.pack(side=BOTTOM)



lblClass=Label(frame34,text="Class",font=("arial",14,"bold"),relief='sunken',width=9,bd=5,height=2)
lblClass.grid(row=0,column=1)
labelTicket1=Label(frame34,text="Ticket",font=("arial",14,"bold"),relief='sunken',width=9,height=2)
labelTicket1.grid(row=0,column=2)
labelAdult1=Label(frame34,text="Adult",font=("arial",14,"bold"),relief='sunken',width=9,height=2)
labelAdult1.grid(row=0,column=3)
labelChild1=Label(frame34,text="Child",font=("arial",14,"bold"),relief='sunken',width=9,height=2)
labelChild1.grid(row=0,column=4)


TicketClass=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=9,height=2,textvariable=class1)
TicketClass.grid(row=1,column=1)
labelTicket2=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=9,height=2,textvariable=Ticket)
labelTicket2.grid(row=1,column=2)
labelAdult2=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=9,height=2,textvariable=Adult)
labelAdult2.grid(row=1,column=3)
labelChild2=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=9,height=2,textvariable=Child)
labelChild2.grid(row=1,column=4)


label=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=40,height=2,justify="center")
label.grid(row=2,columnspan=5)


labelFrom1=Label(frame34,text="from",font=("arial",14,"bold"),relief='sunken',width=9,height=2)
labelFrom1.grid(row=3,column=2)
labelTo1=Label(frame34,text="To",font=("arial",14,"bold"),relief='sunken',width=9,height=2)
labelTo1.grid(row=4,column=2)
labelPrice1=Label(frame34,text="price",font=("arial",14,"bold"),relief='sunken',width=9,height=2)
labelPrice1.grid(row=5,column=2)


labelFrom2=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=9,height=2,textvariable=From3)
labelFrom2.grid(row=3,column=3)
labelTo2=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=9,height=2,textvariable=To)
labelTo2.grid(row=4,column=3)
labelPrice2=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=9,height=2,textvariable=Total)
labelPrice2.grid(row=5,column=3)

label=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=40,height=2,justify="center")
label.grid(row=6,columnspan=5)

labelRef1=Label(frame34,text="ref no",font=("arial",14,"bold"),relief='sunken',width=9,height=2)
labelRef1.grid(row=7,column=1)
labelTime1=Label(frame34,text="time",font=("arial",14,"bold"),relief='sunken',width=9,height=2)
labelTime1.grid(row=7,column=2)
labelDate1=Label(frame34,text="date",font=("arial",14,"bold"),relief='sunken',width=9,height=2)
labelDate1.grid(row=7,column=3)
labelRoute1=Label(frame34,text="route",font=("arial",14,"bold"),relief='sunken',width=9,height=2)
labelRoute1.grid(row=7,column=4)

labelRef2=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=10,height=2,textvariable=Refno)
labelRef2.grid(row=8,column=1)
labelTime2=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=10,height=2,textvariable=Time)
labelTime2.grid(row=8,column=2)
labelDate2=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=10,height=2,textvariable=date)
labelDate2.grid(row=8,column=3)
labelRoute2=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=10,height=2,textvariable=Route)
labelRoute2.grid(row=8,column=4)

label=Label(frame34,font=("arial",14,"bold"),relief='sunken',width=40,height=2,justify="center")
label.grid(row=9,columnspan=5)

def Exit():
    qExit=tkinter.messagebox.askyesno("quit syatem","DO YOU WANT TO QUIT")
    if qExit > 0:
     root.destroy()
     return
def reset():
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("select")
    var8.set("select ")
   
    var11.set("0")
    var12.set("select")
    class1.set(" ")
    Adult.set(" ")
    Child.set(" ")
    nticket.set("0")
    Refno.set(" ")
    Route.set(" ")
    Time.set(" ")
    date.set(" ")
    From3.set(" ")
    To.set("  ")
    Ticket.set(" ")
    Tax.set("RS 2 ")
    Total.set(" ")
    
def Travel_Cost():
    if var1.get()=='1':
        class1.set("standard")
   
    elif var2.get()=='1':
        class1.set("Economy")
    elif var3.get()=='1':
        class1.set("first class")
    else:
        class1.set("standard")

    if var4.get()=='1':
        Adult.set("Yes")
    elif var4.get()=='0':
        Adult.set("No")
    else:
        Adult.set(" ")

    if var5.get()=='1':
        Child.set("yes")
    elif var5.get()=='0':
        Child.set("No")
    else:
        Child.set(" ")

    
    Refno.set("TFL4322")
    Route.set("Direct")
    Time.set(time.strftime("%I:%M:%S"))
    date.set(time.strftime("%d/%m/%Y"))
    Ticket.set(var12.get())
    
    nticket.set(var12.get())
    From3.set(var7.get())
    To.set(var8.get())  
    Tax.set("2 RS")
    item1=var12.get()*2
    item2=var12.get()
    if str(a.get())=="1":
        
        Total.set((5*item2+item1))
    elif str(a.get())=="2":
        
        Total.set((10*item2+item1))
    else:
        
        Total.set(" ")
    if str(a.get())=="1":
        var11.set("single")
    elif str(a.get())=="2":
         
         var11.set("return")
    else:
         var11.set(" ")
    
    entrycomment=Entry(frame2b1,font=("arial",10,"bold"),width=10,bd=10,textvariable=var11,state='disabled')
    entrycomment.grid(row=3,column=1,sticky=W)
    txtTotalTax=Entry(frame2b2,font=("arial",10,"bold"),width=15,bd=10,textvariable=Total,state='disabled')
    txtTotalTax.grid(row=2,column=1)


    
btn=Button(frame35,text="total",padx=7,pady=9,font=("arial",14),width=10,height=2,command=Travel_Cost)
btn.grid(row=10,column=1)
btn=Button(frame35,text="clear",padx=2,pady=4,width=10,font=("arial",14),height=2,command=reset)
btn.grid(row=10,column=2)
btn=Button(frame35,text="reset",padx=2,pady=4,width=10,font=("arial",14),height=2,command=reset)
btn.grid(row=10,column=3)
btn=Button(frame35,text="exit",padx=2,pady=4,width=10,font=("arial",14),height=2,command=Exit)
btn.grid(row=10,column=4)
root.geometry("2350x2350")


























root.mainloop()



