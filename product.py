class Product:
    def __init__(self,id,name,quantity,price,category,supplierName,description):
        self.__id = id
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__category = category
        self.__supplierName = supplierName
        self.__description = description

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getQuantity(self):
        return self.__quantity

    def getPrice(self):
        return self.__price

    def getCategory(self):
        return self.__category

    def getSupplierName(self):
        return self.__supplierName

    def getDescription(self):
        return self.__description

    def setId(self,id):
        self.__id = id

    def setName(self,name):
        self.__name = name

    def setPrice(self,price):
        self.__price = price

    def setQuantity(self,quantity):
        self.__quantity = quantity

    def setCategory(self,category):
        self.__category = category

    def setSupplierName(self,supplierName):
        self.__supplierName = supplierName

    def setDescription(self,description):
        self.__description = description
