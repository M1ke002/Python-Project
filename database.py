import mysql.connector as connector
USERNAME = "root"
PASSWORD = "root"
DATABASE = "Furniture_store_management"

def connectDatabase():
    mydb = connector.connect(
        host="localhost",
        user= USERNAME,
        passwd= PASSWORD,
        database=DATABASE
    )
    return mydb

def getCategories():
    mydb = connectDatabase()
    myCursor = mydb.cursor()
    myCursor.execute("SELECT DISTINCT Product.Category FROM Product")
    result = myCursor.fetchall()
    myCursor.close()
    for i in range(len(result)): result[i] = result[i][0]
    return list(result)

def getSearchResults(list):
    added = False
    mydb = connectDatabase()
    myCursor = mydb.cursor()
    query = """SELECT * FROM Product"""

    #get product name
    if list["name"] != "":
        query += " WHERE Product.nameProduct LIKE '%" + list["name"] + "%'"
        added = True
        
    #get category
    if list["category"] != "All categories":
        if added: query += " AND "
        else:
            query += " WHERE "
            added = True
        query += "Product.Category = '" + list["category"] + "'"
    
    #get min price limit
    if list["minPrice"] != "":
        if added: query += " AND "
        else:
            query += " WHERE "
            added = True
        query += "Product.Price >= " + str(list["minPrice"])

    #get max price limit
    if list["maxPrice"] != "":
        if added: query += " AND "
        else:
            query += " WHERE "
            added = True
        query += "Product.Price <= " + str(list["maxPrice"])

    #get price order
    query += " ORDER BY "
    if list["priceOrder"] == "Descending price":
        query += "Product.Price DESC"
    else:
        query += "Product.Price ASC"

    # print(query)
    myCursor.execute(query)
    result = myCursor.fetchall()
    # print(result)
    myCursor.close()
    return result

def editProductDB(id, product):
    mydb = connectDatabase()
    myCursor = mydb.cursor()
    #if changed id then check if the product id already exists
    if (id != int(product["productId"])):
        myCursor.execute("SELECT * FROM Product WHERE Product.idProduct = %s", (product["productId"],))        
        result = myCursor.fetchall()
        if len(result) > 0:
            myCursor.close()
            return False
    #update the product where id is id
    myCursor.execute(
        """UPDATE Product SET Product.idProduct = %s, Product.nameProduct = %s, Product.Quantity = %s, Product.Price = %s, 
        Product.Category = %s, Product.Supplier = %s, Product.Description = %s WHERE Product.idProduct = %s""", 
        (product["productId"],product["productName"],product["productQuantity"],product["productPrice"],product["productCategory"],product["productSupplier"],product["productDescription"],id)
    )
    mydb.commit()
    myCursor.close()
    return True

def addProductDB(product):
    #check if the product id already exists
    mydb = connectDatabase()
    myCursor = mydb.cursor()
    myCursor.execute("SELECT * FROM Product WHERE Product.idProduct = %s", (product["productId"],))
    result = myCursor.fetchall()
    if len(result) > 0:
        myCursor.close()
        return False
    #add the product
    myCursor.execute(
        """INSERT INTO Product (Product.idProduct, Product.nameProduct, Product.Quantity, Product.Price, Product.Category, Product.Supplier, Product.Description)
        VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
        (product["productId"],product["productName"],product["productQuantity"],product["productPrice"],product["productCategory"],product["productSupplier"],product["productDescription"])
    )
    mydb.commit()
    myCursor.close()
    return True

def deleteProductDB(productId):
    mydb = connectDatabase()
    myCursor = mydb.cursor()
    myCursor.execute("DELETE FROM Product WHERE Product.idProduct = %s", (productId,))
    mydb.commit()
    myCursor.close()

def getProductDB(productId,quantity):
    mydb = connectDatabase()
    myCursor = mydb.cursor()
    myCursor.execute("SELECT Product.idProduct, Product.nameProduct, Product.Quantity, Product.Price FROM Product WHERE Product.idProduct = %s", (productId,))
    result = myCursor.fetchall()
    # print(result)
    if (len(result) <= 0 or int(quantity) > result[0][2]):
        myCursor.close()
        return None
    #deduct product quantity
    myCursor.execute("UPDATE Product SET Product.Quantity = Product.Quantity - %s WHERE Product.idProduct = %s", (quantity,productId))
    mydb.commit()
    myCursor.close()
    result[0] = list(result[0])
    result[0][2] = int(quantity)
    return result

def getBillSearchResults(id):
    mydb = connectDatabase()
    myCursor = mydb.cursor()
    query = "SELECT * FROM Invoice"
    if (id != ""):
        query += " WHERE Invoice.idInvoice  = '" + id + "'"
    myCursor.execute(query)
    result = myCursor.fetchall()
    for i in range(len(result)):
        result[i] = list(result[i])
        listProduct = {}
        billId = result[i][0]
        myCursor.execute("SELECT Product_idProduct, Product_quantity FROM Invoice_Detail WHERE Invoice_Detail.Invoice_idInvoice = %s", (billId,))
        billDetails = myCursor.fetchall()
        for item in billDetails:
            myCursor.execute("SELECT Product.nameProduct, Product.Price FROM Product WHERE Product.idProduct = %s", (item[0],))
            product = myCursor.fetchall()
            productId,billQuantity,productName,productPrice = item[0],item[1],product[0][0],product[0][1]
            # print(product)
            listProduct[productId] = [productName,billQuantity,productPrice]
        # print(listProduct)
        result[i].append(listProduct)
    # print(result)
    myCursor.close()
    return result

def updateBillProduct(billId,productId,quantity):
    mydb = connectDatabase()
    myCursor = mydb.cursor()
    myCursor.execute("SELECT Product_idProduct FROM Invoice_Detail WHERE Invoice_Detail.Invoice_idInvoice = %s AND Invoice_Detail.Product_idProduct = %s", (billId,productId))
    result = myCursor.fetchall()
    if len(result) > 0:
        #update the quantity in the bill
        myCursor.execute("UPDATE Invoice_Detail SET Invoice_Detail.Product_quantity = %s WHERE Invoice_Detail.Invoice_idInvoice = %s AND Invoice_Detail.Product_idProduct = %s", (quantity,billId,productId))
    else:
        myCursor.execute("INSERT INTO Invoice_Detail (Invoice_Detail.Invoice_idInvoice, Invoice_Detail.Product_idProduct, Invoice_Detail.Product_quantity) VALUES (%s, %s, %s)", (billId,productId,quantity))
    mydb.commit()
    myCursor.close()

def removeBillProduct(billId,productId):
    mydb = connectDatabase()
    myCursor = mydb.cursor()
    myCursor.execute("DELETE FROM Invoice_Detail WHERE Invoice_Detail.Invoice_idInvoice = %s AND Invoice_Detail.Product_idProduct = %s", (billId,productId))
    mydb.commit()
    myCursor.close()