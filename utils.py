def verifyProductInfo(list):
    id = list["productId"].strip()
    name = list["productName"].strip()
    price = list["productPrice"].strip()
    supplier = list["productSupplier"].strip()
    quantity = list["productQuantity"].strip()
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
