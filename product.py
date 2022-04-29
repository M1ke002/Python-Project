class Product:
    def __init__(self,id,name,category,price,supplierName,importDate,description):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__category = category
        self.__supplierName = supplierName
        self.__importDate = importDate
        self.__description = description

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getCategory(self):
        return self.__category

    def getSupplierName(self):
        return self.__supplierName

    def getImportDate(self):
        return self.__importDate

    def getDescription(self):
        return self.__description

    def setName(self,name):
        self.__name = name

    def setPrice(self,price):
        self.__price = price

    def setCategory(self,category):
        self.__category = category

    def setSupplierName(self,supplierName):
        self.__supplierName = supplierName
    
    def setImportDate(self,importDate):
        self.__importDate = importDate

    def setDescription(self,description):
        self.__description = description
