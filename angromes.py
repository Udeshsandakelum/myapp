from tkinter import *
 
def addNumbers():
    Interest_rate= float(e2.get()) / 100
    value_of_an_interest_free_loan_intalment = float(e1.get()) / float(e3.get())
    interset_for_one_month = value_of_an_interest_free_loan_intalment * float(Interest_rate) * 0.0833
    numbre_of_month_units = float(e3.get()) / 2 * (float(e3.get()) + 1)
    total_interset_paid = numbre_of_month_units * interset_for_one_month
    totalammount_to_be_paid = float(e1.get()) + total_interset_paid
    the_value_of_one_instalment = float(totalammount_to_be_paid) / float(e3.get())

    #py=int(e1.get())+int(e2.get())
    res = int(the_value_of_one_instalment + 1) #+ int(e3.get())
    myText.set(res)
 
master = Tk()
master.geometry("250x150")
myText=StringVar()
Label(master, text="Loan amount").grid(row=0, sticky=W)
Label(master, text="Interest rate").grid(row=1, sticky=W)
Label(master,text="Installments").grid(row=2,sticky=W)
Label(master, text="Result:").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2,column=1)
 
b = Button(master, text="Calculate", command=addNumbers)
b.grid(row=5, column=0,columnspan=1, rowspan=1, padx=2, pady=5)
 
 
mainloop()
