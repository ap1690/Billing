from tkinter import *
import tkinter as tk 
from tkinter import ttk 
window=Tk()
c_name=StringVar()
item_quantity=StringVar()
c_phn=StringVar()
bill_number=StringVar()
def print_bill():
    # have to add functionality to  print the bill for current user correspoding to bill_number
    x=0
def add_item():
    #have to add functionality to add the item to current cart correspoding to item_quantity,item_name,item_name_id
    x=0
def remove_item():
    #have to add functionality to remove the last item from the cart correspoding to item_quantity,item_name,item_name_id
    x=0
def clear_data():
    #have to add functionality to reset values for next customer
    x=0

def Exit_app():
    # have to add functionality to close this tkinter app
    x=0

def total():
    # have to add functionality to make total bill i.e item_quanity*item_price(correspoding to item_name_id)+item_quanity*item_price(correspoding to item_name_id)+....
    x=0
def bill_area():
    #have to generate and send the billl to the bill area box
    # Example 
    # Customer Name: Akshey
    #Customer Contact:
    #Store Name:
    #Date/Time:
    #Items:
    #Total:
    x=0

#This will create the header note of the page
lbl=Label(window, text="BILLING SOFTWARE", fg='blue', font=("Helvetica", 50))
lbl.place(x=window.winfo_screenwidth()/3, y=50)

#This will create A Subframe in the page to enter customer details
F1 = LabelFrame(window,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="red")
F1.place(x=0,y=150,relwidth=1)
c_name_lbl=Label(F1,text="Customer Name",fg="blue",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
c_name_txt=Entry(F1,width=15,textvariable=c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
c_phn_lbl=Label(F1,text="Phone number",fg="blue",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
c_php_txt=Entry(F1,width=15,textvariable=c_phn,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)
c_bill_lbl=Label(F1,text="Bill Number ",fg="blue",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
c_bill_txt=Entry(F1,width=15,textvariable=bill_number,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

#This will create Another Subframe in the page to view the bill generated
F5=Frame(window,bd=10,relief=GROOVE)
F5.place(x=window.winfo_screenwidth()/2,y=window.winfo_screenheight()/3,width=650,height=450)

bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F5,orient=VERTICAL)
txtarea=Text(F5,yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=txtarea.yview)
txtarea.pack()
print_bill_btn=Button(window,text="Print Bill", command=print_bill,bg="cadetblue",fg="white",bd=5,pady=10, width=9, font=("arial 14 bold")).place(x=window.winfo_screenwidth()/2+200,y=window.winfo_screenheight()/3+450)

#This will create another subframe in the page to select item,prodcut,quantity
F6=LabelFrame(window,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="red")
F6.place(x=0,y=window.winfo_screenheight()/3,height=300,width=600)
item=Label(F6,text="Item Name",fg="blue",font=("times new roman",18,"bold")).grid(column = 0, row = 5, padx = 10, pady = 20) 
n = tk.StringVar() 
item_name = ttk.Combobox(F6, width = 27, textvariable = n) 
item_name['values'] = (' Item1',  
                          ' Item2', 
                          ' Item3', 
                          ' Item4', 
                          ' Item5') 
  
item_name.grid(column = 1, row = 5) 
item_name.current()
item_id=Label(F6,text="Item ID",fg="blue",font=("times new roman",18,"bold")).grid(column = 0, row = 8, padx = 10, pady = 10) 
item_n = tk.StringVar() 
item_name_id= ttk.Combobox(F6, width = 27, textvariable = item_n) 
item_name_id['values'] = (' #01',  
                          ' #02', 
                          ' #03', 
                          ' #04', 
                          ' #05')
item_name_id.grid(column = 1, row = 8) 
item_name_id.current()
item_quantity_labl=Label(F6,text="Item Quantity",fg="blue",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=5)
item_quantity_labl=Entry(F6,width=15,textvariable=item_quantity,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
add_item=Button(F6,command=add_item,text="Add Item",bg="cadetblue",fg="white",bd=5,pady=10, width=9, font=("arial 14 bold")).grid(row=10,column=0,padx=2,pady=5)
remove_item=Button(F6,text="Remove Item",command=remove_item,bg="cadetblue",fg="white",bd=5,pady=9, width=10, font=("arial 14 bold")).grid(row=10,column=1,padx=2,pady=5)

#This will create another subframe in the page to view the various buttons like Total,Generate Bill, Exit,Clear

F7=LabelFrame(window,bd=10,relief=GROOVE,text="Operations",font=("times new roman",15,"bold"),fg="red")
F7.place(x=0,y=window.winfo_screenheight()/3+400,height=100,width=600)

Total_btn=Button(F7,command=total,text="Total",bg="cadetblue",fg="white",bd=5,pady=10, width=9, font=("arial 14 bold")).grid(row=0,column=0,padx=2,pady=5)
Generate_Bill=Button(F7,text="Generate Bill",command=bill_area,bg="cadetblue",fg="white",bd=5,pady=9, width=10, font=("arial 14 bold")).grid(row=0,column=1,padx=2,pady=5)
Clear_btn=Button(F7,text="Clear",command=clear_data,bg="cadetblue",fg="white",bd=5,pady=10, width=9, font=("arial 14 bold")).grid(row=0,column=2,padx=2,pady=5)
Exit_btn=Button(F7,text="Exit", command=Exit_app,bg="cadetblue",fg="white",bd=5,pady=10, width=9, font=("arial 14 bold")).grid(row=0,column=3,padx=2,pady=5)

window.title('Billing APP')
window.state('zoomed')
window.mainloop()
