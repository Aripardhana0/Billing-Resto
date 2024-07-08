from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#000035")
        self.root.title("Billing Resto")
        title=Label(self.root,text="INDO RESTO",bd=12,relief=RIDGE,font=("Monstserrat Black",20),bg="#D54E21",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.Pempek=IntVar()
        self.Batagor=IntVar()
        self.Rawon=IntVar()
        self.Lumpia=IntVar()
        self.Tempe=IntVar()
        self.Keripik=IntVar()
        self.Rujak=IntVar()
        self.Nasi=IntVar()
        self.Rendang=IntVar()
        self.Siomay=IntVar()
        self.Gudeg=IntVar()
        self.Kare=IntVar()
        self.Tongseng=IntVar()
        self.Soto=IntVar()
        self.Martabak=IntVar()
        self.Klepon=IntVar()
        self.Serabi=IntVar()
        self.Nagasari=IntVar()
        self.Pastel=IntVar()
        self.Kroket=IntVar()
        self.Combro=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Monstserrat Black",12),bg="#D54E21",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Monstserrat Black",14),bg="#D54E21",fg="white").grid(row=0,column=0,padx=15)

        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        contact_name=Label(details,text="Contact No.",font=("Monstserrat Black",14),bg="#D54E21",fg="white").grid(row=0,column=2,padx=10)

        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Monstserrat Black",14),bg="#D54E21",fg="white").grid(row=0,column=4,padx=10)

        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================Resturant Menu=================================================================
        snacks=LabelFrame(self.root,text="Starter",font=("Monstserrat Black",12),bg="#D54E21",fg="#FFFFFF",relief=GROOVE,bd=10)
        snacks.place(x=5,y=180,height=380,width=325)

        item1=Label(snacks,text="Pempek",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=0,column=0,pady=11)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Pempek).grid(row=0,column=1,padx=10)

        item2=Label(snacks,text="Batagor",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=1,column=0,pady=11)
        item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Batagor).grid(row=1,column=1,padx=10)

        item3=Label(snacks,text="Siomay",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=2,column=0,pady=11)
        item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Siomay).grid(row=2,column=1,padx=10)

        item4=Label(snacks,text="Lumpia",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=3,column=0,pady=11)
        item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Lumpia).grid(row=3,column=1,padx=10)

        item5=Label(snacks,text="Tempe",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=4,column=0,pady=11)
        item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Tempe).grid(row=4,column=1,padx=10)

        item6=Label(snacks,text="Keripik",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=5,column=0,pady=11)
        item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Keripik).grid(row=5,column=1,padx=10)

        item7=Label(snacks,text="Rujak",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=6,column=0,pady=11)
        item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Rujak).grid(row=6,column=1,padx=10)
        #=================================== Main Course =====================================================================================
        grocery=LabelFrame(self.root,text="Main Course",font=("Monstserrat Black",12),relief=GROOVE,bd=10,bg="#D54E21",fg="#FFFFFF")
        grocery.place(x=340,y=180,height=380,width=325)

        item8=Label(grocery,text="Nasi",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=0,column=0,pady=11)
        item8_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Nasi).grid(row=0,column=1,padx=10)

        item9=Label(grocery,text="Rendang",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=1,column=0,pady=11)
        item9_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Rendang).grid(row=1,column=1,padx=10)

        item10=Label(grocery,text="Rawon",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=2,column=0,pady=11)
        item10_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Rawon).grid(row=2,column=1,padx=10)

        item11=Label(grocery,text="Gudeg",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=3,column=0,pady=11)
        item11_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Gudeg).grid(row=3,column=1,padx=10)

        item12=Label(grocery,text="Kare",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=4,column=0,pady=11)
        item12_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Kare).grid(row=4,column=1,padx=10)

        item13=Label(grocery,text="Tongseng",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=5,column=0,pady=11)
        item13_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Tongseng).grid(row=5,column=1,padx=10)

        item14=Label(grocery,text="Soto",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=6,column=0,pady=11)
        item14_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.Soto).grid(row=6,column=1,padx=10)
        #========================================Snacks===============================================================================
        hygine=LabelFrame(self.root,text="Snacks",font=("Monstserrat Black",12),relief=GROOVE,bd=10,bg="#D54E21",fg="#FFFFFF")
        hygine.place(x=677,y=180,height=380,width=325)

        item15=Label(hygine,text="Martabak",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=0,column=0,pady=11)
        item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Martabak).grid(row=0,column=1,padx=10)

        item16=Label(hygine,text="Klepon",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=1,column=0,pady=11)
        item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Klepon).grid(row=1,column=1,padx=10)

        item17=Label(hygine,text="Serabi",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=2,column=0,pady=11)
        item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Serabi).grid(row=2,column=1,padx=10)

        item18=Label(hygine,text="Nagasari",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=3,column=0,pady=11)
        item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Nagasari).grid(row=3,column=1,padx=10)

        item19=Label(hygine,text="Pastel",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=4,column=0,pady=11)
        item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Pastel).grid(row=4,column=1,padx=10)

        item20=Label(hygine,text="Kroket",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=5,column=0,pady=11)
        item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Kroket).grid(row=5,column=1,padx=10)

        item21=Label(hygine,text="Combro",font=("Monstserrat Black",11),bg="#D54E21",fg="#FFFFFF").grid(row=6,column=0,pady=11)
        item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Combro).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#D54E21")
        billarea.place(x=1010,y=188,width=330,height=372)

        bill_title=Label(billarea,text="Bill Area",font=("Monstserrat Black",17),bd=7,relief=GROOVE,bg="#D54E21",fg="#FFFFFF").pack(fill=X)

        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Monstserrat Black",12),relief=GROOVE,bd=10,bg="#D54E21",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)

        total_snacks=Label(billing_menu,text="Total Snacks Price",font=("Monstserrat Black",11),bg="#D54E21",fg="white").grid(row=0,column=0)
        total_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)

        total_grocery=Label(billing_menu,text="Total Grocery Price",font=("Monstserrat Black",11),bg="#D54E21",fg="white").grid(row=1,column=0)
        total_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_gro).grid(row=1,column=1,padx=10,pady=7)


        total_hygine=Label(billing_menu,text="Total Beauty & Hygine Price",font=("Monstserrat Black",11),bg="#D54E21",fg="white").grid(row=2,column=0)
        total_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_hyg).grid(row=2,column=1,padx=10,pady=7)

        tax_snacks=Label(billing_menu,text="Snacks Tax",font=("Monstserrat Black",11),bg="#D54E21",fg="white").grid(row=0,column=2)
        tax_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)

        tax_grocery=Label(billing_menu,text="Grocery Tax",font=("Monstserrat Black",11),bg="#D54E21",fg="white").grid(row=1,column=2)
        tax_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)


        tax_hygine=Label(billing_menu,text="Beauty & Hygine Tax",font=("Monstserrat Black",11),bg="#D54E21",fg="white").grid(row=2,column=2)
        tax_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#000035")
        button_frame.place(x=830,width=500,height=95)

        button_total=Button(button_frame,text="Total Bill",font=("Monstserrat Black",15),pady=10,bg="#00cc00",fg="#FFFFFF",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Monstserrat Black",15),pady=10,bg="#808080",fg="#FFFFFF",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Monstserrat Black",15),pady=10,bg="#FF0000",fg="#FFFFFF",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.nu=self.Pempek.get()*3
    self.no=self.Batagor.get()*2
    self.la=self.Rawon.get()*1
    self.ore=self.Lumpia.get()*1
    self.mu=self.Tempe.get()*1
    self.si=self.Keripik.get()*1
    self.na=self.Rujak.get()*2
    total_snacks_price=(
                self.nu+
                self.no+
                self.la+
                self.ore+
                self.mu+
                self.si+
                self.na)
    self.total_sna.set("$ "+str(total_snacks_price))
    self.a.set("$ "+str(round(total_snacks_price*0.05,3)))

    self.at=self.Nasi.get()*3
    self.pa=self.Rendang.get()*6
    self.oi=self.Gudeg.get()*6
    self.ri=self.Siomay.get()*6
    self.su=self.Kare.get()*5
    self.te=self.Soto.get()*4
    self.da=self.Tongseng.get()*3
    total_grocery_price=(
        self.at+
        self.pa+
        self.oi+
        self.ri+
        self.su+
        self.te+
        self.da)

    self.total_gro.set("$ "+str(total_grocery_price))
    self.b.set("$ "+str(round(total_grocery_price*0.01,3)))

    self.so=self.Martabak.get()*1
    self.sh=self.Klepon.get()*1
    self.cr=self.Nagasari.get()*1
    self.lo=self.Serabi.get()*1
    self.fo=self.Pastel.get()*2
    self.ma=self.Kroket.get()*2
    self.sa=self.Combro.get()*3

    total_hygine_price=(
        self.so+
        self.sh+
        self.cr+
        self.lo+
        self.fo+
        self.ma+
        self.sa)

    self.total_hyg.set("$ "+str(total_hygine_price))
    self.c.set("$ "+str(round(total_hygine_price*0.10,3)))
    self.total_all_bill=(total_snacks_price+
                total_grocery_price+
                total_hygine_price+
                (round(total_grocery_price*0.01,3))+
                (round(total_hygine_price*0.10,3))+
                (round(total_snacks_price*0.05,3)))
    self.total_all_bil="$ "+str(self.total_all_bill)
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO INDO RESTO\n\tPhone-No.0832432342")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.Pempek.get()!=0:
        self.txtarea.insert(END,f"Pempek\t\t {self.Pempek.get()}\t{self.nu}\n")
    if self.Batagor.get()!=0:
        self.txtarea.insert(END,f"Batagor\t\t {self.Batagor.get()}\t{self.no}\n")
    if self.Rawon.get()!=0:
        self.txtarea.insert(END,f"Rawon\t\t {self.Rawon.get()}\t{self.la}\n")
    if self.Lumpia.get()!=0:
        self.txtarea.insert(END,f"Lumpia\t\t {self.Lumpia.get()}\t{self.ore}\n")
    if self.Tempe.get()!=0:
        self.txtarea.insert(END,f"Tempe\t\t {self.Tempe.get()}\t{self.mu}\n")
    if self.Keripik.get()!=0:
        self.txtarea.insert(END,f"Keripik\t\t {self.Keripik.get()}\t{self.si}\n")
    if self.Rujak.get()!=0:
        self.txtarea.insert(END,f"Rujak\t\t {self.Rujak.get()}\t{self.na}\n")
    if self.Nasi.get()!=0:
        self.txtarea.insert(END,f"Nasi\t\t {self.Nasi.get()}\t{self.at}\n")
    if self.Rendang.get()!=0:
        self.txtarea.insert(END,f"Rendang\t\t {self.Rendang.get()}\t{self.pa}\n")
    if self.Siomay.get()!=0:
        self.txtarea.insert(END,f"Siomay\t\t {self.Siomay.get()}\t{self.ri}\n")
    if self.Gudeg.get()!=0:
        self.txtarea.insert(END,f"Gudeg\t\t {self.Gudeg.get()}\t{self.oi}\n")
    if self.Kare.get()!=0:
        self.txtarea.insert(END,f"Kare\t\t {self.Kare.get()}\t{self.su}\n")
    if self.Tongseng.get()!=0:
        self.txtarea.insert(END,f"Tongseng\t\t {self.Tongseng.get()}\t{self.da}\n")
    if self.Soto.get()!=0:
        self.txtarea.insert(END,f"Soto\t\t {self.Soto.get()}\t{self.te}\n")
    if self.Martabak.get()!=0:
        self.txtarea.insert(END,f"Martabak\t\t {self.Martabak.get()}\t{self.so}\n")
    if self.Klepon.get()!=0:
        self.txtarea.insert(END,f"Klepon\t\t {self.Klepon.get()}\t{self.sh}\n")
    if self.Serabi.get()!=0:
        self.txtarea.insert(END,f"Serabi\t\t {self.Serabi.get()}\t{self.lo}\n")
    if self.Nagasari.get()!=0:
        self.txtarea.insert(END,f"Nagasari\t\t {self.Nagasari.get()}\t{self.cr}\n")
    if self.Pastel.get()!=0:
        self.txtarea.insert(END,f"Pastel\t\t {self.Pastel.get()}\t{self.fo}\n")
    if self.Kroket.get()!=0:
        self.txtarea.insert(END,f"Kroket\t\t {self.Kroket.get()}\t{self.ma}\n")
    if self.Combro.get()!=0:
        self.txtarea.insert(END,f"Combro\t\t {self.Combro.get()}\t{self.sa}\n")

    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="$ 0.0":
        self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")
    if self.b.get()!="$ 0.0":
        self.txtarea.insert(END,f"Total Grocery Tax : {self.b.get()}\n")
    if self.c.get()!="$ 0.0":
        self.txtarea.insert(END,f"Total Beauty&Hygine Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.Pempek.set(0)
        self.Batagor.set(0)
        self.Rawon.set(0)
        self.Lumpia.set(0)
        self.Tempe.set(0)
        self.Keripik.set(0)
        self.Rujak.set(0)
        self.Nasi.set(0)
        self.Rendang.set(0)
        self.Siomay.set(0)
        self.Gudeg.set(0)
        self.Kare.set(0)
        self.Tongseng.set(0)
        self.Soto.set(0)
        self.Martabak.set(0)
        self.Klepon.set(0)
        self.Serabi.set(0)
        self.Nagasari.set(0)
        self.Pastel.set(0)
        self.Kroket.set(0)
        self.Combro.set(0)
        self.total_sna.set(0)
        self.total_gro.set(0)
        self.total_hyg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()