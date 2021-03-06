from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from bill import *
from product import *
from database import *
from utils import *
import os

class App:
    def __init__(self, root,startscreen=None):
        self.startscreen = startscreen
        self.root = root
        self.root.title("Product management")
        self.root.geometry("1004x650")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.onClose)
        self.width,self.height = 1000,560
        self.productList = {}
        self.billList = {}
        self.selectedItemId = -1
        self.selectedBillId = -1
        self.notebook = ttk.Notebook(self.root)

        #Logout button
        self.logoutBtn = Button(self.root, text="Logout",font=("Arial",10,"bold"),bd=3,width=17, command=self.logout)
        self.logoutBtn.place(x=self.width-148,y=2)

        #Top frames
        self.productFrame = Frame(self.notebook)
        self.billFrame = Frame(self.notebook)

        self.productFrame.configure(height=self.height, width=self.width)
        self.productFrame.pack(side="top")
        
        self.billFrame.configure(height=self.height, width=self.width)
        self.billFrame.pack(side="top")
        self.billFrame.grid_propagate(0)

        self.notebook.add(self.productFrame, text="Product")
        self.notebook.add(self.billFrame, text="Bill")
        self.notebook.pack(side="top")

        #sub frames
        self.productInfoFrame = LabelFrame(self.productFrame, text="Product Information")
        self.searchFrame = LabelFrame(self.productFrame, text="Search options")
        self.tableFrame = Frame(self.productFrame)
        self.buttonsFrame = Frame(self.productFrame)

        #------------------product Info frame---------------
        #define variables
        self.productIdEntryValue = StringVar()
        self.productNameEntryValue = StringVar()
        self.productPriceEntryValue = StringVar()
        self.productCategoryEntryValue = StringVar()
        self.productSupplierEntryValue = StringVar()
        self.productQuantityEntryValue = StringVar()
        self.productDescriptionEntryValue = StringVar()

        self.productInfoFrame.configure(
            borderwidth="3", height="160", relief="groove", width=self.width
        )
        self.productInfoFrame.grid(column="0", row="0",pady=(5,10))
        self.productInfoFrame.grid_propagate(0)

        self.ProductIdLabel = Label(self.productInfoFrame)
        self.ProductIdLabel.configure(
            borderwidth="10",
            font="{Arial} 11 {bold}",
            text="Product ID:",
        )
        self.ProductIdLabel.grid(column="0", row="0", sticky="w")

        self.productIdEntry = Entry(self.productInfoFrame,readonlybackground="#E7E6E5",font=("Arial",12,"bold"),bd=2,width="20", textvariable=self.productIdEntryValue)
        self.productIdEntry.grid(padx="10",column="1", row="0", sticky="w")

        self.productNameLabel = Label(self.productInfoFrame)
        self.productNameLabel.configure(
            borderwidth="10",
            font="{Arial} 11 {bold}",
            text="Name:",
        )
        self.productNameLabel.grid(column="2", row="0", sticky="w")

        self.productNameEntry = Entry(self.productInfoFrame,readonlybackground="#E7E6E5", font=("Arial",12,"bold"),bd=2,width="27",textvariable=self.productNameEntryValue)
        self.productNameEntry.grid(column="3", padx="10", row="0", sticky="w")

        self.productCategoryLabel = Label(self.productInfoFrame)
        self.productCategoryLabel.configure(
            borderwidth="10",
            font="{Arial} 11 {bold}",
            text="Category:",
        )
        self.productCategoryLabel.grid(column="4", row="0", sticky="w")

        self.productCategoryEntry = Entry(self.productInfoFrame,readonlybackground="#E7E6E5", font=("Arial",12,"bold"),bd=2,width="18",textvariable=self.productCategoryEntryValue)
        self.productCategoryEntry.grid(column="5", padx="10", row="0", sticky="w")

        self.productPriceLabel = Label(self.productInfoFrame)
        self.productPriceLabel.configure(
            borderwidth="10",
            font="{Arial} 11 {bold}",
            text="Price ($):",
        )
        self.productPriceLabel.grid(column="0", pady="5", row="1", sticky="w")

        self.productPriceEntry = Entry(self.productInfoFrame,readonlybackground="#E7E6E5", font=("Arial",12,"bold"),bd=2,width="20",textvariable=self.productPriceEntryValue)
        self.productPriceEntry.grid(column="1", padx="10", pady="5", row="1", sticky="w")

        self.productSupplierLabel = Label(self.productInfoFrame)
        self.productSupplierLabel.configure(
            borderwidth="10",
            font="{Arial} 11 {bold}",
            text="Supplier:",
        )
        self.productSupplierLabel.grid(column="2", pady="5", row="1", sticky="w")

        self.productSupplierEntry = Entry(self.productInfoFrame,readonlybackground="#E7E6E5", font=("Arial",12,"bold"),bd=2,width="27",textvariable=self.productSupplierEntryValue)
        self.productSupplierEntry.grid(column="3", padx="10", pady="5", row="1", sticky="w")

        self.productQuantityLabel = Label(self.productInfoFrame)
        self.productQuantityLabel.configure(
            borderwidth="10",
            font="{Arial} 11 {bold}",
            text="Quantity:",
        )
        self.productQuantityLabel.grid(column="4", pady="5", row="1", sticky="w")

        self.productQuantityEntry = Entry(self.productInfoFrame,readonlybackground="#E7E6E5", font=("Arial",12,"bold"),bd=2,width="18",textvariable=self.productQuantityEntryValue)
        self.productQuantityEntry.grid(column="5", padx="10", pady="5", row="1",sticky="w")

        self.productDescriptionLabel = Label(self.productInfoFrame)
        self.productDescriptionLabel.configure(
            borderwidth="10",
            font="{Arial} 11 {bold}",
            text="Description:",
        )
        self.productDescriptionLabel.grid(column="0", row="2", sticky="w")

        self.productDescriptionEntry = Entry(self.productInfoFrame,readonlybackground="#E7E6E5", font=("Arial",12,"bold"),bd=2,width="93",textvariable=self.productDescriptionEntryValue)
        self.productDescriptionEntry.grid(
            column="1", columnspan="5", padx="10", row="2", sticky="w"
        )

        #----------------Search frame-------------
        #define variables
        self.searchEntryValue = StringVar()
        self.minPriceEntryValue = StringVar()
        self.maxPriceEntryValue = StringVar()
        self.searchCategoryBoxValue = StringVar()
        self.searchPriceOrderBoxValue = StringVar()

        #combobox options
        self.categories = []
        self.priceOrders = ["Order by","Ascending price","Descending price"]
        self.selectedCategory = "All categories"
        self.selectedPriceOrder = self.priceOrders[0]

        self.searchFrame.configure(
            borderwidth="3", height="110", relief="groove", width=self.width
        )
        self.searchFrame.grid(column="0", row="1")
        self.searchFrame.grid_propagate(0)

        self.searchLabel = Label(self.searchFrame)
        self.searchLabel.configure(font="{Arial} 11 {bold}", text="Enter a name:")
        self.searchLabel.grid(column="0", padx="10", pady="10", row="0")

        self.searchEntry = Entry(self.searchFrame, font=("Arial",12,"bold"),bd=2,width="20",textvariable=self.searchEntryValue)
        self.searchEntry.grid(column="1", row="0", sticky="w")

        self.searchCategoryBox = ttk.Combobox(self.searchFrame, textvariable=self.searchCategoryBoxValue, font=("Arial",11,"bold"))
        self.searchCategoryBox["state"] = "readonly"
        self.searchCategoryBox.configure(justify="left", width="18")
        self.searchCategoryBox.grid(column="2", padx="20", row="0", sticky="w")
        self.searchCategoryBoxValue.set(self.selectedCategory)

        self.priceOrderBox = ttk.Combobox(self.searchFrame, textvariable=self.searchPriceOrderBoxValue, font=("Arial",11,"bold"))
        self.priceOrderBox["state"] = "readonly"
        self.priceOrderBox.configure(justify="left", width="20")
        self.priceOrderBox.grid(column="3", row="0", sticky="w")
        self.searchPriceOrderBoxValue.set(self.selectedPriceOrder)

        #display combobox values
        self.displaySearchOptions()

        self.minPriceLabel = Label(self.searchFrame)
        self.minPriceLabel.configure(font="{Arial} 11 {bold}", text="Min price:")
        self.minPriceLabel.grid(column="0", padx="10", pady="5", row="1", sticky="w")

        self.minPriceEntry = Entry(self.searchFrame, font=("Arial",12,"bold"),bd=2,width="15",textvariable=self.minPriceEntryValue)
        self.minPriceEntry.grid(column="1", row="1", sticky="w")
        
        self.maxPriceLabel = Label(self.searchFrame)
        self.maxPriceLabel.configure(font="{Arial} 11 {bold}", text="Max price:")
        self.maxPriceLabel.grid(column="2", padx="20", pady="5", row="1", sticky="w")

        self.maxPriceEntry = Entry(self.searchFrame, font=("Arial",12,"bold"),bd=2,width="15",textvariable=self.maxPriceEntryValue)
        self.maxPriceEntry.grid(column="3", row="1", sticky="w")

        self.findBtn = Button(self.searchFrame,text="Find", width="20", font=("font", 10, "bold"), bd=4, command=self.displaySearchResults)
        self.findBtn.grid(column="4", padx="30", row="0")

        self.clearBtn = Button(self.searchFrame,text="Clear search", width="20", font=("font", 10, "bold"), bd=4, command=self.clearSearchFields)
        self.clearBtn.grid(column="4", padx="30", row="1")


        #------------------table frame--------------
        #scrollbar for table
        self.tableSb = Scrollbar(self.tableFrame,orient="vertical")
        self.tableSb.pack(fill="y", side="right")

        #treeview table
        self.trv = ttk.Treeview(self.tableFrame, height = 14,columns=(1,2,3,4,5,6),show="headings")
        self.trv.pack(fill="x", side="top")
        self.trv.bind('<ButtonRelease-1>', self.displayProduct)
        self.trv.config(yscrollcommand=self.tableSb.set)
        self.tableSb.config(command=self.trv.yview)

        self.trv.heading(1, text="Product ID")
        self.trv.column(1, anchor="center", minwidth=90, width=100)
        self.trv.heading(2, text="Name")
        self.trv.column(2, anchor="center", minwidth=0, width=260)
        self.trv.heading(3, text="Quantity")
        self.trv.column(3, anchor="center", minwidth=0, width=80)
        self.trv.heading(4, text="Price")
        self.trv.column(4, anchor="center", minwidth=0, width=130)
        self.trv.heading(5, text="Category")
        self.trv.column(5, anchor="center", minwidth=0, width=122)
        self.trv.heading(6, text="Supplier")
        self.trv.column(6, anchor="center", minwidth=0, width=140)

        self.tableFrame.configure(
            borderwidth="3", height="300", relief="groove", width=self.width
        )
        self.tableFrame.grid(column="0", row="2")
        self.tableFrame.pack_propagate(0)


        #---------------button frame------------
        #define variables
        self.textEditBtn = StringVar()
        self.textEditBtn.set("Edit product")
        self.textDeleteBtn = StringVar()
        self.textDeleteBtn.set("Delete product")

        self.buttonsFrame.configure(borderwidth="3", height="40", relief="groove", width=self.width)
        self.buttonsFrame.grid(column="0", row="3")
        self.buttonsFrame.grid_propagate(0)

        self.addProductBtn = Button(self.buttonsFrame,text="Add product", width="23", font=("font", 10, "bold"), bd=4, command=self.addProduct)
        self.addProductBtn.grid(column="0", row="0", sticky="ew")

        self.editProductBtn = Button(self.buttonsFrame,textvariable=self.textEditBtn, width="23", font=("font", 10, "bold"), bd=4, command=self.editProduct)
        self.editProductBtn.grid(column="1", row="0", sticky="ew")

        self.deleteProductBtn = Button(self.buttonsFrame,textvariable=self.textDeleteBtn, width="23", font=("font", 10, "bold"), bd=4, command=self.deleteProduct)
        self.deleteProductBtn.grid(column="2", row="0", sticky="ew")

        self.clearInfoBtn = Button(self.buttonsFrame,text="Clear product", width="23", font=("font", 10, "bold"), bd=4, command=self.clearProductFields)
        self.clearInfoBtn.grid(column="3", row="0", sticky="ew")

        self.manageCategoryBtn = Button(self.buttonsFrame,text="Clear table", width="23", font=("font", 10, "bold"), bd=4, command=self.clearProductTable)
        self.manageCategoryBtn.grid(column="4", row="0", sticky="ew")


        # ------------------Bill Window ------------------

        self.billInfoFrame = LabelFrame(self.billFrame, text="Bill information")
        self.billInfoFrame.configure(
            borderwidth="3", height="160", relief="groove", width="1000"
        )
        self.billInfoFrame.grid(column="0", row="0",pady=(5,10))
        self.billInfoFrame.grid_propagate(0)

        #define variables
        self.billIdEntryValue = StringVar()
        self.billDateEntryValue = StringVar()
        self.customerNameEntryValue = StringVar()
        self.customerPhoneEntryValue = StringVar()
        self.customerAddressEntryValue = StringVar()

        self.billIdLabel = Label(self.billInfoFrame)
        self.billIdLabel.configure(
            borderwidth="10",
            cursor="based_arrow_down",
            font="{Arial} 12 {bold}",
            text="Bill ID:",
        )
        self.billIdLabel.grid(column="0", row="0", sticky="w")

        self.billIdEntry = Entry(self.billInfoFrame,readonlybackground="#E7E6E5", textvariable=self.billIdEntryValue)
        self.billIdEntry.configure(font=("Arial",12,"bold"),bd=2, justify="left",width="28")
        self.billIdEntry.grid(column="1", row="0", sticky="w")

        self.billDateLabel = Label(self.billInfoFrame)
        self.billDateLabel.configure(
            borderwidth="10",
            cursor="based_arrow_down",
            font="{Arial} 12 {bold}",
            text="Bill Date:",
        )
        self.billDateLabel.grid(column="2", row="0", sticky="w")

        self.billDateEntry = Entry(self.billInfoFrame,readonlybackground="#E7E6E5", textvariable=self.billDateEntryValue)
        self.billDateEntry.configure(font=("Arial",12,"bold"),bd=2, justify="left", width="30")
        self.billDateEntry.grid(column="3", padx="10", row="0", sticky="w")
        self.customerNameLabel = Label(self.billInfoFrame)
        self.customerNameLabel.configure(
            borderwidth="10",
            cursor="based_arrow_down",
            font="{Arial} 12 {bold}",
            text="Customer name:",
        )
        self.customerNameLabel.grid(column="0", pady="5", row="1", sticky="w")
        self.customerNameEntry = Entry(self.billInfoFrame,readonlybackground="#E7E6E5", textvariable=self.customerNameEntryValue)
        self.customerNameEntry.configure(font=("Arial",12,"bold"),bd=2, justify="left", width="28")
        self.customerNameEntry.grid(column="1",padx=(0,30), pady="5", row="1", sticky="w")

        self.customerPhoneLabel = Label(self.billInfoFrame)
        self.customerPhoneLabel.configure(
            borderwidth="10",
            cursor="based_arrow_down",
            font="{Arial} 12 {bold}",
            text="Customer phone number:",
        )
        self.customerPhoneLabel.grid(column="2", pady="5", row="1", sticky="w")
        self.customerPhoneEntry = Entry(self.billInfoFrame,readonlybackground="#E7E6E5", textvariable=self.customerPhoneEntryValue)
        self.customerPhoneEntry.configure(
            font=("Arial",12,"bold"),bd=2, justify="left", width="30"
        )
        self.customerPhoneEntry.grid(
            column="3", padx="10", pady="5", row="1", sticky="w"
        )
        self.customerAddressLabel = Label(self.billInfoFrame)
        self.customerAddressLabel.configure(
            borderwidth="10",
            cursor="based_arrow_down",
            font="{Arial} 12 {bold}",
            text="Customer address:",
        )
        self.customerAddressLabel.grid(column="0", row="2", sticky="w")

        self.customerAddressEntry = Entry(self.billInfoFrame,readonlybackground="#E7E6E5", textvariable=self.customerAddressEntryValue)
        self.customerAddressEntry.configure(
            font=("Arial",12,"bold"),bd=2, justify="left", width="88"
        )
        self.customerAddressEntry.grid(column="1", columnspan="3", row="2", sticky="w")

        # ------------------Bill Table frame ------------------
        self.billTableFrame = Frame(self.billFrame)
        self.billTableFrame.configure(height="370", width="1000")
        self.billTableFrame.grid(column="0", row="2")
        self.billTableFrame.grid_propagate(0)

        #sub frames
        self.leftFrame = Frame(self.billTableFrame)
        self.rightFrame = Frame(self.billTableFrame)

        self.leftFrame.configure(
            borderwidth="3", height="370", relief="groove", width="600"
        )
        self.leftFrame.grid(column="0", row="0", sticky="w")
        self.leftFrame.pack_propagate(0)
        self.rightFrame.configure(
            borderwidth="3", height="370", relief="groove", width="400"
        )
        self.rightFrame.grid(column="1", row="0", sticky="e")
        self.rightFrame.pack_propagate(0)

        #define variables
        self.searchBillIdEntryValue = StringVar()

        self.billSearchFrame = Frame(self.leftFrame)
        self.searchBillIdLabel = Label(self.billSearchFrame)
        self.searchBillIdLabel.configure(borderwidth="10", font="{Arial} 12 {bold}", text="Enter Bill ID:")
        self.searchBillIdLabel.grid(column="0", pady="5", row="0", sticky="w")
        self.searchBillIdEntry = Entry(self.billSearchFrame, textvariable=self.searchBillIdEntryValue)
        self.searchBillIdEntry.configure(font=("Arial",12,"bold"),bd=2, justify="left", width="27")
        self.searchBillIdEntry.grid(column="1", row="0", sticky="w")
        self.billSearchBtn = Button(self.billSearchFrame, font=("font", 10, "bold"), bd=4, command=self.displayBillSearchResults)
        self.billSearchBtn.configure(text="Find", width="20")
        self.billSearchBtn.grid(column="2", padx="20", row="0")
        self.billSearchFrame.configure(height="60", width="600")
        self.billSearchFrame.pack(side="top")
        self.billSearchFrame.grid_propagate(0)

        self.resultTableSb = Scrollbar(self.leftFrame,orient="vertical")
        self.resultTableSb.pack(fill="y", side="right")

        self.resultTableTrv = ttk.Treeview(self.leftFrame, height=20,columns=(1,2,3),show="headings")
        self.resultTableTrv.pack(fill="x", side="top")
        self.resultTableTrv.bind("<ButtonRelease-1>", self.displayBill)
        self.resultTableTrv.config(yscrollcommand=self.resultTableSb.set)
        self.resultTableSb.config(command=self.resultTableTrv.yview)

        self.resultTableTrv.heading(1, text="Bill ID")
        self.resultTableTrv.column(1, anchor="center", minwidth=90, width=100)
        self.resultTableTrv.heading(2, text="Date")
        self.resultTableTrv.column(2, anchor="center", minwidth=0, width=80)
        self.resultTableTrv.heading(3, text="Customer Name")
        self.resultTableTrv.column(3, anchor="center", minwidth=0, width=200)

        self.billTitleLabel = Label(self.rightFrame,text="Bill Information")
        self.billTitleLabel.configure(
            anchor="n", font="{Arial} 18 {bold}", justify="center"
        )
        self.billTitleLabel.pack(fill="x", side="top")

        self.billSb = ttk.Scrollbar(self.rightFrame)
        self.billSb.configure(orient="vertical")
        self.billSb.pack(expand="false", fill="y", side="right")

        self.billText = Text(self.rightFrame, yscrollcommand=self.billSb.set)
        self.billText.configure(height="10", width="50")
        self.billText.pack(expand="true", fill="y", side="top")
        self.billSb.configure(command=self.billText.yview)
        self.initBill()

        self.generateBillBtn = Button(self.rightFrame, font=("font", 10, "bold"), command=self.generateBill)
        self.generateBillBtn.configure(text="Generate bill", width="20")
        self.generateBillBtn.pack(side="bottom",fill="x")


        # ------------------Bill menu frame ------------------
        self.billMenuFrame = Frame(self.billFrame)
        self.billMenuFrame.configure(height="80", width="1000")
        self.billMenuFrame.grid(column="0", row="3")
        self.billMenuFrame.grid_propagate(0)

        #sub frame
        self.billMenuFrame_leftFrame = Frame(self.billMenuFrame)
        self.billMenuFrame_rightFrame = Frame(self.billMenuFrame)

        self.billMenuFrame_leftFrame.configure(
            borderwidth="3", height="80", relief="groove", width="500"
        )
        self.billMenuFrame_leftFrame.grid(column="0", row="0", sticky="w")
        self.billMenuFrame_leftFrame.grid_propagate(0)
        self.billMenuFrame_rightFrame.configure(
            borderwidth="3", height="80", relief="groove", width="500"
        )
        self.billMenuFrame_rightFrame.grid(column="1", row="0", sticky="e")
        self.billMenuFrame_rightFrame.grid_propagate(0)

        #define variables
        self.billProductIdEntryValue = StringVar()
        self.billProductQuantityEntryValue = StringVar()
        self.textEditBillBtn = StringVar()
        self.textEditBillBtn.set("Edit bill")
        self.textDeleteBillBtn = StringVar()
        self.textDeleteBillBtn.set("Delete bill")

        self.addBillBtn = Button(self.billMenuFrame_leftFrame, font=("font", 10, "bold"), bd=4, command=self.addBill)
        self.addBillBtn.configure(text="Add bill",width=11)
        self.addBillBtn.grid(column="0", padx="10", pady="19", row="0")
        self.editBillBtn = Button(self.billMenuFrame_leftFrame, font=("font", 10, "bold"), bd=4, command=self.editBill)
        self.editBillBtn.configure(textvariable=self.textEditBillBtn,width=11)
        self.editBillBtn.grid(column="1", padx="10", pady="19", row="0")
        self.deleteBillBtn = Button(self.billMenuFrame_leftFrame, font=("font", 10, "bold"), bd=4, command=self.deleteBill)
        self.deleteBillBtn.configure(textvariable=self.textDeleteBillBtn,width=11)
        self.deleteBillBtn.grid(column="2", padx="10", pady="19", row="0")
        self.clearBillBtn = Button(self.billMenuFrame_leftFrame, font=("font", 10, "bold"), bd=4, command=self.clearBillFields)
        self.clearBillBtn.configure(text="Clear bill",width=11)
        self.clearBillBtn.grid(column="3", padx="10", pady="19", row="0")

        self.billProductIdLabel = ttk.Label(self.billMenuFrame_rightFrame)
        self.billProductIdLabel.configure(font="{Arial} 12 {bold}", text="Product Id: ")
        self.billProductIdLabel.grid(column="0", padx="5", pady=(5,2), row="0", sticky="w")
        self.billProductIdEntry = Entry(self.billMenuFrame_rightFrame,font=("Arial",12,"bold"),bd=2)
        self.billProductIdEntry.configure(width="20",textvariable=self.billProductIdEntryValue)
        self.billProductIdEntry.grid(column="1", row="0", sticky="w", pady=(5,2))

        self.addProductBillBtn = Button(self.billMenuFrame_rightFrame, font=("font", 10, "bold"), bd=3, padx=10, command=self.addProductToBill)
        self.addProductBillBtn.configure(text="Add product", width="16")
        self.addProductBillBtn.grid(column="3", row="0", sticky="w",padx="20", pady=(5,2))

        self.billProductQuantity = ttk.Label(self.billMenuFrame_rightFrame)
        self.billProductQuantity.configure(font="{Arial} 12 {bold}", text="Quantity:")
        self.billProductQuantity.grid(column="0", padx="5", pady="5", row="1", sticky="w")

        self.billProductQuantityEntry = Entry(self.billMenuFrame_rightFrame,font=("Arial",12,"bold"),bd=2)
        self.billProductQuantityEntry.configure(width="20",textvariable=self.billProductQuantityEntryValue)
        self.billProductQuantityEntry.grid(column="1", row="1", sticky="w")

        self.removeProductBillBtn = Button(self.billMenuFrame_rightFrame, font=("font", 10, "bold"), bd=3, command=self.removeProductFromBill)
        self.removeProductBillBtn.configure(text="Remove product", width="18")
        self.removeProductBillBtn.grid(column="3", row="1", sticky="w",padx="20")

        #set initial state
        self.displayAllProducts()
        self.displayAllBills()

    def run(self):
        self.root.mainloop()

    def logout(self):
        self.root.destroy()
        if self.startscreen is not None: 
            self.startscreen.deiconify()

    def onClose(self):
        self.root.destroy()
        if self.startscreen is not None: 
            self.startscreen.destroy()

    def displayProduct(self, event):
        curItem = self.trv.focus()
        if (curItem != ""):
            self.selectedItemId = self.trv.item(curItem)["values"][0]
            product = self.productList[self.selectedItemId]
            self.productIdEntryValue.set(product.getId())
            self.productNameEntryValue.set(product.getName())
            self.productQuantityEntryValue.set(product.getQuantity())
            self.productPriceEntryValue.set(product.getPrice())
            self.productCategoryEntryValue.set(product.getCategory())
            self.productSupplierEntryValue.set(product.getSupplierName())
            self.productDescriptionEntryValue.set(product.getDescription())
            self.setState("readonly","product")
            self.textDeleteBtn.set("Delete product")
            self.textEditBtn.set("Edit product")

    def displaySearchOptions(self):
        try:
            #get the categories from db
            self.categories = getCategories()
            self.categories.insert(0,"All categories")
            #Combobox
            self.searchCategoryBox["values"] = self.categories
            self.priceOrderBox["values"] = self.priceOrders
        except Exception as e:
            print(e)

    def setState(self, mode, type):
        if type == "product":
            self.productIdEntry["state"] = mode
            self.productNameEntry["state"] = mode
            self.productCategoryEntry["state"] = mode
            self.productPriceEntry["state"] = mode
            self.productSupplierEntry["state"] = mode
            self.productQuantityEntry["state"] = mode
            self.productDescriptionEntry["state"] = mode
        else:
            self.billIdEntry["state"] = mode
            self.billDateEntry["state"] = mode
            self.customerNameEntry["state"] = mode
            self.customerPhoneEntry["state"] = mode
            self.customerAddressEntry["state"] = mode

    def clearProductTable(self):
        self.selectedItemId = -1
        self.setState("normal","product")
        self.textDeleteBtn.set("Delete product")
        self.textEditBtn.set("Edit product")
        self.trv.delete(*self.trv.get_children())

    def getProductFields(self):
        list = {}
        list["productId"] = self.productIdEntryValue.get()
        list["productName"] = self.productNameEntryValue.get()
        list["productPrice"] = self.productPriceEntryValue.get()
        list["productCategory"] = self.productCategoryEntryValue.get()
        list["productSupplier"] = self.productSupplierEntryValue.get()
        list["productQuantity"] = self.productQuantityEntryValue.get()
        list["productDescription"] = self.productDescriptionEntryValue.get()
        return list

    def getSearchFields(self):
        list = {}
        list["name"] = self.searchEntryValue.get()
        list["minPrice"] = self.minPriceEntryValue.get()
        list["maxPrice"] = self.maxPriceEntryValue.get()
        list["category"] = self.searchCategoryBoxValue.get()
        list["priceOrder"] = self.searchPriceOrderBoxValue.get()
        return list

    def clearProductFields(self):
        self.deselectTrvItem(self.trv,"product")
        self.setState("normal","product")
        self.textDeleteBtn.set("Delete product")
        self.textEditBtn.set("Edit product")
        self.productIdEntryValue.set("")
        self.productNameEntryValue.set("")
        self.productPriceEntryValue.set("")
        self.productCategoryEntryValue.set("")
        self.productSupplierEntryValue.set("")
        self.productQuantityEntryValue.set("")
        self.productDescriptionEntryValue.set("")
    
    def clearSearchFields(self):
        self.searchEntryValue.set("")
        self.minPriceEntryValue.set("")
        self.maxPriceEntryValue.set("")
        self.searchCategoryBoxValue.set(self.categories[0])
        self.searchPriceOrderBoxValue.set(self.priceOrders[0])

    def addProduct(self):
        try:
            data = self.getProductFields()
            if (verifyProductInfo(data)):
                if (addProductDB(data)):
                    self.displaySearchResults()
                    self.displaySearchOptions()
                    self.textDeleteBtn.set("Delete product")
                    self.textEditBtn.set("Edit product")
                else: messagebox.showerror("Error","Id already exists")
            else: messagebox.showerror("Error","Invalid Product")
        except Exception as e:
            print(e)


    def editProduct(self):
        if (self.selectedItemId == -1):
            messagebox.showerror("Error","Select a product first!")
            return
        if self.textEditBtn.get() == "Edit product":
            self.setState("normal","product")
            self.textEditBtn.set("Save")
            self.textDeleteBtn.set("Cancel")
        else:
            try:
                data = self.getProductFields()
                if (verifyProductInfo(data)):
                    if editProductDB(self.selectedItemId,data):
                        self.displaySearchResults()
                        self.displaySearchOptions()
                        self.setState("readonly","product")
                        self.textDeleteBtn.set("Delete product")
                        self.textEditBtn.set("Edit product")
                    else: messagebox.showerror("Error","Id already exists")
                else: messagebox.showerror("Error","Invalid Product")   
            except Exception as e:
                print(e)     

    def deleteProduct(self):
        if (self.selectedItemId == -1):
            messagebox.showerror("Error","Select a product first!")
            return
        if self.textDeleteBtn.get() == "Delete product":
            try:
                data = self.getProductFields()
                if (verifyProductInfo(data)):
                    #delete in db
                    deleteProductDB(self.selectedItemId)
                    self.displaySearchResults()
                    self.displaySearchOptions()
                    self.setState("normal","product")
                else: messagebox.showerror("Error","Invalid Product")
            except Exception as e:
                print(e)
        else:
            self.displayProduct(None)
            self.textDeleteBtn.set("Delete product")
            self.textEditBtn.set("Edit product")
            self.setState("readonly","product")

    def displaySearchResults(self):
        list = self.getSearchFields()
        if (verifySearchFields(list)):
            try:
                #Update selectedCategory and selectedPriceOrder
                self.selectedCategory = list["category"]
                self.selectedPriceOrder = list["priceOrder"]
                data = getSearchResults(list)
                self.clearProductTable()
                for item in data:
                    product = Product(item[0],item[1],item[2],item[3],item[4],item[5],item[6])
                    self.productList[product.getId()] = product
                    productDisplayed = item[0:6]
                    self.trv.insert("", "end", values=productDisplayed)
            except Exception as e:
                print(e)
        else: messagebox.showerror("Error","Invalid prices")

    def displayAllProducts(self):
        try:
            data = getAllProducts()
            for item in data:
                product = Product(item[0],item[1],item[2],item[3],item[4],item[5],item[6])
                self.productList[product.getId()] = product
                productDisplayed = item[0:6]
                self.trv.insert("", "end", values=productDisplayed)
        except Exception as e:
            print(e)

    def deselectTrvItem(self,trv,type):
        if (type == "product"): self.selectedItemId = -1
        else: self.selectedBillId = -1
        for item in trv.selection():
            trv.selection_remove(item)

    #---------------- Bill methods ----------------

    def generateBill(self):
        #create a text file with name = bill id
        if (self.selectedBillId == -1):
            messagebox.showerror("Error","Select a bill first!")
            return
        txt = self.billText.get("1.0",END)
        path = "./bills/"
        fileName = "bill#"+str(self.selectedBillId)+".txt"
        file = open(os.path.join(path, fileName),"w")
        file.write(txt)
        file.close()
        messagebox.showinfo("Success","Bill generated with name = "+fileName)

    def initBill(self, bill=None):
        self.billText.config(state=NORMAL)
        self.billText.delete('1.0', END)
        id = bill.getId() if bill is not None else ""
        customerName = bill.getCustomerName() if bill is not None else ""
        date = bill.getDate() if bill is not None else ""
        totalPrice = 0
        self.billText.insert(END,f"Bill Id: {id}\n")
        self.billText.insert(END,f"Date: {date}\n")
        self.billText.insert(END,f"Customer name: {customerName}\n\n")
        self.billText.insert(END,"----------------------------------------------\n")
        self.billText.insert(END,"Product".ljust(20) + "Quantity".rjust(12) + "Price".rjust(13) + "\n")
        self.billText.insert(END,"----------------------------------------------\n")
        if bill is not None:
            for product in bill.getListProduct().values():
                name,quantity,price = product[0],product[1],product[2]
                self.billText.insert(END,f"{name}".ljust(25) + f"{quantity}".ljust(10) + f"{price}".rjust(10) + "\n")
                totalPrice += price * quantity
        self.billText.insert(END,"\nTotal price($):".ljust(25) + f"{totalPrice}".rjust(21) + "\n")
        self.billText.config(state=DISABLED)

    def displayBillSearchResults(self):
        try:
            res = self.getBillSearchField()
            data = getBillSearchResults(res)
            self.clearBillTable()
            for item in data:
                bill = Bill(item[0],item[1],item[2],item[3],item[4])
                bill.setListProduct(item[5])
                self.billList[item[0]] = bill
                billDisplayed = item[0:3]
                self.resultTableTrv.insert("", "end", values=billDisplayed)
        except Exception as e:
            print(e)

    def displayAllBills(self):
        try:
            data = getAllBills()
            for item in data:
                bill = Bill(item[0],item[1],item[2],item[3],item[4])
                bill.setListProduct(item[5])
                self.billList[item[0]] = bill
                billDisplayed = item[0:3]
                self.resultTableTrv.insert("", "end", values=billDisplayed)
        except Exception as e:
            print(e)

    def clearBillTable(self):
        self.selectedBillId = -1
        self.setState("normal","bill")
        self.textDeleteBillBtn.set("Delete bill")
        self.textEditBillBtn.set("Edit bill")
        self.resultTableTrv.delete(*self.resultTableTrv.get_children())

    def addBill(self):
        data = self.getBillFields()
        try:
            if (verifyBillInfo(data)):
                if (addBillDB(data)):
                    self.displayBillSearchResults()
                    self.textDeleteBillBtn.set("Delete bill")
                    self.textEditBillBtn.set("Edit bill")
                else: messagebox.showerror("Error","Id already exists")
            else: messagebox.showerror("Error","Invalid Bill")
        except Exception as e:
            print(e)

    def editBill(self):
        if (self.selectedBillId == -1):
            messagebox.showerror("Error","Select a bill first!")
            return
        if self.textEditBillBtn.get() == "Edit bill":
            self.setState("normal","bill")
            self.textEditBillBtn.set("Save")
            self.textDeleteBillBtn.set("Cancel")
        else:
            data = self.getBillFields()
            try:
                if (verifyBillInfo(data)):
                    if editBillDB(self.selectedBillId,data):
                        self.displayBillSearchResults()
                        self.setState("readonly","bill")
                        self.textDeleteBillBtn.set("Delete bill")
                        self.textEditBillBtn.set("Edit bill")
                    else: messagebox.showerror("Error","Id already exists")
                else: messagebox.showerror("Error","Invalid Bill")
            except Exception as e:
                print(e)

    def deleteBill(self):
        if (self.selectedBillId == -1):
            messagebox.showerror("Error","Select a bill first!")
            return
        if self.textDeleteBillBtn.get() == "Delete bill":
            data = self.getBillFields()
            if (verifyBillInfo(data)):
                #delete in db
                try:
                    deleteBillDB(self.selectedBillId)
                    self.displayBillSearchResults()
                    self.setState("normal","bill")
                except Exception as e:
                    print(e)
            else: messagebox.showerror("Error","Invalid Bill")
        else:
            self.displayBill(None)
            self.textDeleteBillBtn.set("Delete bill")
            self.textEditBillBtn.set("Edit bill")
            self.setState("readonly","bill")

    def clearBillFields(self):
        self.deselectTrvItem(self.resultTableTrv,"bill")
        self.textDeleteBillBtn.set("Delete bill")
        self.textEditBillBtn.set("Edit bill")
        self.setState("normal","bill")
        self.billIdEntryValue.set("")
        self.billDateEntryValue.set("")
        self.customerNameEntryValue.set("")
        self.customerPhoneEntryValue.set("")
        self.customerAddressEntryValue.set("")

    def addProductToBill(self):
        if (self.selectedBillId == -1):
            messagebox.showerror("Error","Select a bill first!")
            return
        bill = self.billList[self.selectedBillId]
        productId = self.billProductIdEntryValue.get()
        quantity = self.billProductQuantityEntryValue.get()
        if (not verifyProductBill(productId,quantity)):
            messagebox.showerror("Error","Invalid product Id or quantity")
            return
        productId,quantity = int(productId),int(quantity)
        try:
            product = deductProductDB(productId,quantity)
            if (product is not None):
                name,price = product[0],product[1]
                #if product already exists in bill then increase quantity, else add product to bill
                if productId in bill.getListProduct().keys():
                    bill.getListProduct()[productId][1] += int(quantity)
                else: bill.addProduct(productId,name,quantity,price)
                #update DB
                updateBillProduct(self.selectedBillId,productId,bill.getListProduct()[productId][1])
                self.initBill(bill)
            else: messagebox.showerror("Error","Cant find product or invalid quantity")
        except Exception as e:
            print(e)

    def removeProductFromBill(self):
        if (self.selectedBillId == -1):
            messagebox.showerror("Error","Select a bill first!")
            return
        bill = self.billList[self.selectedBillId]
        productId = self.billProductIdEntryValue.get()
        if (not verifyProductBill(productId)):
            messagebox.showerror("Error","Invalid product Id")
            return
        productId = int(productId)
        #if product exists in bill then remove it
        try:
            if productId in bill.getListProduct().keys():
                bill.getListProduct().pop(productId)
                self.initBill(bill)
                removeBillProduct(self.selectedBillId,productId)
            else: messagebox.showerror("Error","Product not in bill")
        except Exception as e:
            print(e)

    def displayBill(self, event):
        curItem = self.resultTableTrv.focus()
        if (curItem != ""):
            self.selectedBillId = self.resultTableTrv.item(curItem)["values"][0]
            bill = self.billList[self.selectedBillId]
            self.initBill(bill)
            self.billIdEntryValue.set(bill.getId())
            self.billDateEntryValue.set(bill.getDate())
            self.customerNameEntryValue.set(bill.getCustomerName())
            self.customerPhoneEntryValue.set(bill.getCustomerPhone())
            self.customerAddressEntryValue.set(bill.getCustomerAddress())
            self.setState("readonly","bill")
            self.textDeleteBillBtn.set("Delete bill")
            self.textEditBillBtn.set("Edit bill")

    def getBillFields(self):
        list = {}
        list["billId"] = self.billIdEntryValue.get()
        list["billDate"] = self.billDateEntryValue.get()
        list["customerName"] = self.customerNameEntryValue.get()
        list["customerPhone"] = self.customerPhoneEntryValue.get()
        list["customerAddress"] = self.customerAddressEntryValue.get()
        return list

    def getBillSearchField(self):
        return self.searchBillIdEntryValue.get()

if __name__ == "__main__":
    root = Tk()
    App(root).run()