class Bill:
    def __init__(self,id,date,customerName,customerPhone,customerAddress):
        self.__id = id
        self.__date = date
        self.__customerName = customerName
        self.__customerPhone = customerPhone
        self.__customerAddress = customerAddress
        self.__listProduct = {}

    def getId(self):
        return self.__id

    def getDate(self):
        return self.__date

    def getCustomerName(self):
        return self.__customerName

    def getCustomerPhone(self):
        return self.__customerPhone

    def getCustomerAddress(self):
        return self.__customerAddress

    def getListProduct(self):
        return self.__listProduct

    def addProduct(self,id,name,quantity,price):
        self.__listProduct[id] = [name,quantity,price]

    def setId(self,id):
        self.__id = id

    def setDate(self,date):
        self.__date = date

    def setCustomerName(self,customerName):
        self.__customerName = customerName

    def setCustomerPhone(self,customerPhone):
        self.__customerPhone = customerPhone

    def setCustomerAddress(self,customerAddress):
        self.__customerAddress = customerAddress

    def setListProduct(self,listProduct):
        self.__listProduct = listProduct