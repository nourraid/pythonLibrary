class book:
    counter = 0

    def __init__(self , name , author , page_number , id_cat):
        book.counter += 1
        self.name = name
        self.author = author
        self.page_number = page_number
        self.id_cat = id_cat

    def setName(self, name):
        self.name = name

    def setAuthor(self, author):
        self.author = author

    def setPageNum(self , page_number):
        self.page_number = page_number

    def setIdCat(self, id_cat):
        self.id_cat = id_cat

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def getAuthor(self):
        return self.author

    def getPageNum(self):
        return self.page_number

    def getIdCat(self):
        return self.id_cat

    def getId(self):
        return self.id

    def __str__(self):
        return f"{self.getName()},{self.getAuthor()},{self.getPageNum()},{self.getIdCat()}"
