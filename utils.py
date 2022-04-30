def verifyProductInfo(product):
    id = product["productId"].strip()
    name = product["productName"].strip()
    price = product["productPrice"].strip()
    supplier = product["productSupplier"].strip()
    quantity = product["productQuantity"].strip()
    if not id.isnumeric() or name == "" or not price.isnumeric() or supplier == "" or not quantity.isnumeric() or int(quantity) <= 0:
        return False
    return True

def verifySearchFields(list):
    minPrice = list["minPrice"].strip()
    maxPrice = list["maxPrice"].strip()
    if minPrice != "":
        if not minPrice.isnumeric():
            return False
    if maxPrice != "":
        if not maxPrice.isnumeric():
            return False
    return True

def verifyProductBill(productId,quantity=None):
    if (not productId.isnumeric()):
        return False
    if (quantity is not None and not quantity.isnumeric()):
        return False
    return True

def verifyBillInfo(bill):
    id = bill["billId"].strip()
    date = bill["billDate"].strip()
    customerName = bill["customerName"].strip()
    customerPhone = bill["customerPhone"].strip()
    customerAddress = bill["customerAddress"].strip()
    if not id.isnumeric() or date == "" or customerName == "" or not customerPhone.isnumeric() or customerAddress == "":
        return False
    return True