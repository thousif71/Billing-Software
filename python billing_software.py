from tkinter import *
import random
import os
import sys
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        self.root.configure(bg="#f0f0f0")  # changed background color

        # Top frame
        top_frame = Frame(self.root, bg="#333", height=50)
        top_frame.pack(fill=X)
        title = Label(top_frame, text="Billing System", font=("Arial Black", 20), fg="white", bg="#333")
        title.pack(pady=10)

        #===================================variables=======================================================================================
        self.nutella=IntVar()
        self.noodles=IntVar()
        self.lays=IntVar()
        self.oreo=IntVar()
        self.muffin=IntVar()
        self.silk=IntVar()
        self.namkeen=IntVar()
        self.atta=IntVar()
        self.pasta=IntVar()
        self.rice=IntVar()
        self.oil=IntVar()
        self.sugar=IntVar()
        self.dal=IntVar()
        self.tea=IntVar()
        self.soap=IntVar()
        self.shampoo=IntVar()
        self.lotion=IntVar()
        self.cream=IntVar()
        self.foam=IntVar()
        self.mask=IntVar()
        self.sanitizer=IntVar()
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

        # Customer details frame
        customer_frame = LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#f0f0f0", fg="#333")
        customer_frame.place(x=0, y=50, relwidth=1, height=100)

        cust_name = Label(customer_frame, text="Customer Name", font=("Arial Black", 14), bg="#f0f0f0", fg="#333")
        cust_name.grid(row=0, column=0, padx=15)
        cust_entry = Entry(customer_frame, borderwidth=4, width=30, textvariable=self.c_name)
        cust_entry.grid(row=0, column=1, padx=8)

        contact_name = Label(customer_frame, text="Contact No.", font=("Arial Black", 14), bg="#f0f0f0", fg="#333")
        contact_name.grid(row=0, column=2, padx=10)
        contact_entry = Entry(customer_frame, borderwidth=4, width=30, textvariable=self.phone)
        contact_entry.grid(row=0, column=3, padx=8)

        bill_name = Label(customer_frame, text="Bill.No.", font=("Arial Black", 14), bg="#f0f0f0", fg="#333")
        bill_name.grid(row=0, column=4, padx=10)
        bill_no = random.randint(1000, 9999)
        bill_entry = Label(customer_frame, borderwidth=4, width=30, text=f"Bill No. {bill_no}", relief="ridge")
        bill_entry.grid(row=0, column=5, padx=8)

        #=======================================snacks label frame=================================================================
        snacks_frame = LabelFrame(self.root, text="Snacks", font=("Arial Black", 12), bg="#f0f0f0", fg="#333")
        snacks_frame.place(x=5, y=150, height=380, width=325)

        item1 = Label(snacks_frame, text="Nutella Choco Spread", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item1.grid(row=0, column=0, pady=11)
        item1_entry = Entry(snacks_frame, borderwidth=2, width=15, textvariable=self.nutella)
        item1_entry.grid(row=0, column=1, padx=10)

        item2 = Label(snacks_frame, text="Noodles(1 Pack)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item2.grid(row=1, column=0, pady=11)
        item2_entry = Entry(snacks_frame, borderwidth=2, width=15, textvariable=self.noodles)
        item2_entry.grid(row=1, column=1, padx=10)

        item3 = Label(snacks_frame, text="Lays(10Rs)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item3.grid(row=2, column=0, pady=11)
        item3_entry = Entry(snacks_frame, borderwidth=2, width=15, textvariable=self.lays)
        item3_entry.grid(row=2, column=1, padx=10)

        item4 = Label(snacks_frame, text="Oreo(20Rs)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item4.grid(row=3, column=0, pady=11)
        item4_entry = Entry(snacks_frame, borderwidth=2, width=15, textvariable=self.oreo)
        item4_entry.grid(row=3, column=1, padx=10)

        item5 = Label(snacks_frame, text="Chocolate Muffin", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item5.grid(row=4, column=0, pady=11)
        item5_entry = Entry(snacks_frame, borderwidth=2, width=15, textvariable=self.muffin)
        item5_entry.grid(row=4, column=1, padx=10)

        item6 = Label(snacks_frame, text="Dairy Milk Silk(60Rs)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item6.grid(row=5, column=0, pady=11)
        item6_entry = Entry(snacks_frame, borderwidth=2, width=15, textvariable=self.silk)
        item6_entry.grid(row=5, column=1, padx=10)

        item7 = Label(snacks_frame, text="Namkeen(15Rs)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item7.grid(row=6, column=0, pady=11)
        item7_entry = Entry(snacks_frame, borderwidth=2, width=15, textvariable=self.namkeen)
        item7_entry.grid(row=6, column=1, padx=10)

        #===================================GROCERY=====================================================================================
        grocery_frame = LabelFrame(self.root, text="Grocery", font=("Arial Black", 12), bg="#f0f0f0", fg="#333")
        grocery_frame.place(x=340, y=150, height=380, width=325)

        item8 = Label(grocery_frame, text="Aashirvaad Atta(1kg)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item8.grid(row=0, column=0, pady=11)
        item8_entry = Entry(grocery_frame, borderwidth=2, width=15, textvariable=self.atta)
        item8_entry.grid(row=0, column=1, padx=10)

        item9 = Label(grocery_frame, text="Pasta(1kg)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item9.grid(row=1, column=0, pady=11)
        item9_entry = Entry(grocery_frame, borderwidth=2, width=15, textvariable=self.pasta)
        item9_entry.grid(row=1, column=1, padx=10)

        item10 = Label(grocery_frame, text="Basmathi Rice(1kg)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item10.grid(row=2, column=0, pady=11)
        item10_entry = Entry(grocery_frame, borderwidth=2, width=15, textvariable=self.rice)
        item10_entry.grid(row=2, column=1, padx=10)

        item11 = Label(grocery_frame, text="Sunflower Oil(1ltr)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item11.grid(row=3, column=0, pady=11)
        item11_entry = Entry(grocery_frame, borderwidth=2, width=15, textvariable=self.oil)
        item11_entry.grid(row=3, column=1, padx=10)

        item12 = Label(grocery_frame, text="Refined Sugar(1kg)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item12.grid(row=4, column=0, pady=11)
        item12_entry = Entry(grocery_frame, borderwidth=2, width=15, textvariable=self.sugar)
        item12_entry.grid(row=4, column=1, padx=10)

        item13 = Label(grocery_frame, text="Daal(1kg)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item13.grid(row=5, column=0, pady=11)
        item13_entry = Entry(grocery_frame, borderwidth=2, width=15, textvariable=self.dal)
        item13_entry.grid(row=5, column=1, padx=10)

        item14 = Label(grocery_frame, text="Tea Powder(1kg)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item14.grid(row=6, column=0, pady=11)
        item14_entry = Entry(grocery_frame, borderwidth=2, width=15, textvariable=self.tea)
        item14_entry.grid(row=6, column=1, padx=10)

        #========================================beauty and hygine===============================================================================
        hygine_frame = LabelFrame(self.root, text="Beauty & Hygine", font=("Arial Black", 12), bg="#f0f0f0", fg="#333")
        hygine_frame.place(x=677, y=150, height=380, width=325)

        item15 = Label(hygine_frame, text="Bathing Soap", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item15.grid(row=0, column=0, pady=11)
        item15_entry = Entry(hygine_frame, borderwidth=2, width=15, textvariable=self.soap)
        item15_entry.grid(row=0, column=1, padx=10)

        item16 = Label(hygine_frame, text="Shampoo(1ltr)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item16.grid(row=1, column=0, pady=11)
        item16_entry = Entry(hygine_frame, borderwidth=2, width=15, textvariable=self.shampoo)
        item16_entry.grid(row=1, column=1, padx=10)

        item17 = Label(hygine_frame, text="Body Lotion(1ltr)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item17.grid(row=2, column=0, pady=11)
        item17_entry = Entry(hygine_frame, borderwidth=2, width=15, textvariable=self.lotion)
        item17_entry.grid(row=2, column=1, padx=10)

        item18 = Label(hygine_frame, text="Face Cream", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item18.grid(row=3, column=0, pady=11)
        item18_entry = Entry(hygine_frame, borderwidth=2, width=15, textvariable=self.cream)
        item18_entry.grid(row=3, column=1, padx=10)

        item19 = Label(hygine_frame, text="Shaving Foam", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item19.grid(row=4, column=0, pady=11)
        item19_entry = Entry(hygine_frame, borderwidth=2, width=15, textvariable=self.foam)
        item19_entry.grid(row=4, column=1, padx=10)

        item20 = Label(hygine_frame, text="Face Mask(1piece)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item20.grid(row=5, column=0, pady=11)
        item20_entry = Entry(hygine_frame, borderwidth=2, width=15, textvariable=self.mask)
        item20_entry.grid(row=5, column=1, padx=10)

        item21 = Label(hygine_frame, text="Hand Sanitizer(50ml)", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        item21.grid(row=6, column=0, pady=11)
        item21_entry = Entry(hygine_frame, borderwidth=2, width=15, textvariable=self.sanitizer)
        item21_entry.grid(row=6, column=1, padx=10)

        #=====================================================billarea==============================================================================
        bill_area = Frame(self.root, bd=10, relief=GROOVE, bg="#f0f0f0")
        bill_area.place(x=1010, y=150, width=330, height=372)

        bill_title = Label(bill_area, text="Bill Area", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#f0f0f0", fg="#333")
        bill_title.pack(fill=X)

        scrol_y = Scrollbar(bill_area, orient=VERTICAL)
        self.txtarea = Text(bill_area, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #=================================================billing menu=========================================================================================
        billing_menu = LabelFrame(self.root, text="Billing Summery", font=("Arial Black", 12), bg="#f0f0f0", fg="#333")
        billing_menu.place(x=0, y=530, relwidth=1, height=137)

        total_snacks = Label(billing_menu, text="Total Snacks Price", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        total_snacks.grid(row=0, column=0)
        total_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_sna)
        total_snacks_entry.grid(row=0, column=1, padx=10, pady=7)

        total_grocery = Label(billing_menu, text="Total Grocery Price", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        total_grocery.grid(row=1, column=0)
        total_grocery_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_gro)
        total_grocery_entry.grid(row=1, column=1, padx=10, pady=7)

        total_hygine = Label(billing_menu, text="Total Beauty & Hygine Price", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        total_hygine.grid(row=2, column=0)
        total_hygine_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_hyg)
        total_hygine_entry.grid(row=2, column=1, padx=10, pady=7)

        tax_snacks = Label(billing_menu, text="Snacks Tax", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        tax_snacks.grid(row=0, column=2)
        tax_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a)
        tax_snacks_entry.grid(row=0, column=3, padx=10, pady=7)

        tax_grocery = Label(billing_menu, text="Grocery Tax", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        tax_grocery.grid(row=1, column=2)
        tax_grocery_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b)
        tax_grocery_entry.grid(row=1, column=3, padx=10, pady=7)

        tax_hygine = Label(billing_menu, text="Beauty & Hygine Tax", font=("Arial Black", 11), bg="#f0f0f0", fg="#333")
        tax_hygine.grid(row=2, column=2)
        tax_hygine_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.c)
        tax_hygine_entry.grid(row=2, column=3, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#333")
        button_frame.place(x=830, width=500, height=95)

        button_total = Button(button_frame, text="Total Bill", font=("Arial Black", 15), pady=10, bg="#f0f0f0", fg="#333", command=lambda: self.total())
        button_total.grid(row=0, column=0, padx=12)

        button_clear = Button(button_frame, text="Clear Field", font=("Arial Black", 15), pady=10, bg="#f0f0f0", fg="#333", command=lambda: self.clear())
        button_clear.grid(row=0, column=1, padx=10, pady=6)

        button_exit = Button(button_frame, text="Exit", font=("Arial Black", 15), pady=10, bg="#f0f0f0", fg="#333", width=8, command=lambda: self.exit1())
        button_exit.grid(row=0, column=2, padx=10, pady=6)

        self.intro()

    def total(self):
        if (self.c_name.get() == "" or self.phone.get() == ""):
            messagebox.showerror("Error", "Fill the complete Customer Details!!")
        self.nu = self.nutella.get() * 120
        self.no = self.noodles.get() * 40
        self.la = self.lays.get() * 10
        self.ore = self.oreo.get() * 20
        self.mu = self.muffin.get() * 30
        self.si = self.silk.get() * 60
        self.na = self.namkeen.get() * 15
        total_snacks_price = (
                self.nu +
                self.no +
                self.la +
                self.ore +
                self.mu +
                self.si +
                self.na)
        self.total_sna.set(str(total_snacks_price) + " Rs")
        self.a.set(str(round(total_snacks_price * 0.05, 3)) + " Rs")

        self.at = self.atta.get() * 42
        self.pa = self.pasta.get() * 120
        self.oi = self.oil.get() * 113
        self.ri = self.rice.get() * 160
        self.su = self.sugar.get() * 55
        self.te = self.tea.get() * 480
        self.da = self.dal.get() * 76
        total_grocery_price = (
            self.at +
            self.pa +
            self.oi +
            self.ri +
            self.su +
            self.te +
            self.da)

        self.total_gro.set(str(total_grocery_price) + " Rs")
        self.b.set(str(round(total_grocery_price * 0.01, 3)) + " Rs")

        self.so = self.soap.get() * 30
        self.sh = self.shampoo.get() * 180
        self.cr = self.cream.get() * 130
        self.lo = self.lotion.get() * 500
        self.fo = self.foam.get() * 85
        self.ma = self.mask.get() * 100
        self.sa = self.sanitizer.get() * 20

        total_hygine_price = (
            self.so +
            self.sh +
            self.cr +
            self.lo +
            self.fo +
            self.ma +
            self.sa)

        self.total_hyg.set(str(total_hygine_price) + " Rs")
        self.c.set(str(round(total_hygine_price * 0.10, 3)) + " Rs")
        self.total_all_bill = (total_snacks_price +
                               total_grocery_price +
                               total_hygine_price +
                               (round(total_grocery_price * 0.01, 3)) +
                               (round(total_hygine_price * 0.10, 3)) +
                               (round(total_snacks_price * 0.05, 3)))
        self.total_all_bil = str(self.total_all_bill) + " Rs"
        self.billarea()

    def intro(self):
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, "\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
        self.txtarea.insert(END, f"\n\nBill no. : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone No. : {self.phone.get()}")
        self.txtarea.insert(END, "\n====================================\n")
        self.txtarea.insert(END, "\nProduct\t\tQty\tPrice\n")
        self.txtarea.insert(END, "\n====================================\n")

    def billarea(self):
        self.intro()
        if self.nutella.get() != 0:
            self.txtarea.insert(END, f"Nutella\t\t {self.nutella.get()}\t{self.nu}\n")
        if self.noodles.get() != 0:
            self.txtarea.insert(END, f"Noodles\t\t {self.noodles.get()}\t{self.no}\n")
        if self.lays.get() != 0:
            self.txtarea.insert(END, f"Lays\t\t {self.lays.get()}\t{self.la}\n")
        if self.oreo.get() != 0:
            self.txtarea.insert(END, f"Oreo\t\t {self.oreo.get()}\t{self.ore}\n")
        if self.muffin.get() != 0:
            self.txtarea.insert(END, f"Muffins\t\t {self.muffin.get()}\t{self.mu}\n")
        if self.silk.get() != 0:
            self.txtarea.insert(END, f"Silk\t\t {self.silk.get()}\t{self.si}\n")
        if self.namkeen.get() != 0:
            self.txtarea.insert(END, f"Namkeen\t\t {self.namkeen.get()}\t{self.na}\n")
        if self.atta.get() != 0:
            self.txtarea.insert(END, f"Atta\t\t {self.atta.get()}\t{self.at}\n")
        if self.pasta.get() != 0:
            self.txtarea.insert(END, f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"Rice\t\t {self.rice.get()}\t{self.ri}\n")
        if self.oil.get() != 0:
            self.txtarea.insert(END, f"Oil\t\t {self.oil.get()}\t{self.oi}\n")
        if self.sugar.get() != 0:
            self.txtarea.insert(END, f"Sugar\t\t {self.sugar.get()}\t{self.su}\n")
        if self.dal.get() != 0:
            self.txtarea.insert(END, f"Daal\t\t {self.dal.get()}\t{self.da}\n")
        if self.tea.get() != 0:
            self.txtarea.insert(END, f"Tea\t\t {self.tea.get()}\t{self.te}\n")
        if self.soap.get() != 0:
            self.txtarea.insert(END, f"Soap\t\t {self.soap.get()}\t{self.so}\n")
        if self.shampoo.get() != 0:
            self.txtarea.insert(END, f"Shampoo\t\t {self.shampoo.get()}\t{self.sh}\n")
        if self.lotion.get() != 0:
            self.txtarea.insert(END, f"Lotion\t\t {self.lotion.get()}\t{self.lo}\n")
        if self.cream.get() != 0:
            self.txtarea.insert(END, f"Cream\t\t {self.cream.get()}\t{self.cr}\n")
        if self.foam.get() != 0:
            self.txtarea.insert(END, f"Foam\t\t {self.foam.get()}\t{self.fo}\n")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"Mask\t\t {self.mask.get()}\t{self.ma}\n")
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"Sanitizer\t\t {self.sanitizer.get()}\t{self.sa}\n")

        self.txtarea.insert(END, f"------------------------------------\n")
        if self.a.get() != "0.0 Rs":
            self.txtarea.insert(END, f"Total Snacks Tax : {self.a.get()}\n")
        if self.b.get() != "0.0 Rs":
            self.txtarea.insert(END, f"Total Grocery Tax : {self.b.get()}\n")
        if self.c.get() != "0.0 Rs":
            self.txtarea.insert(END, f"Total Beauty&Hygine Tax : {self.c.get()}\n")
        self.txtarea.insert(END, f"Total Bill Amount : {self.total_all_bil}\n")
        self.txtarea.insert(END, f"------------------------------------\n")

    def clear(self):
        self.txtarea.delete(1.0, END)
        self.nutella.set(0)
        self.noodles.set(0)
        self.lays.set(0)
        self.oreo.set(0)
        self.muffin.set(0)
        self.silk.set(0)
        self.namkeen.set(0)
        self.atta.set(0)
        self.pasta.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.sugar.set(0)
        self.dal.set(0)
        self.tea.set(0)
        self.soap.set(0)
        self.shampoo.set(0)
        self.lotion.set(0)
        self.cream.set(0)
        self.foam.set(0)
        self.mask.set(0)
        self.sanitizer.set(0)
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

root = Tk()
obj = Bill_App(root)
root.mainloop()