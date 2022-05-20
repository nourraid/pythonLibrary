class category:

    counter = 0

    def __init__(self,name):
        category.counter += 1
        self.id = category.counter
        self.name = name

    def setName(self, name):
        self.name = name

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def __str__(self):
        return f"{self.getId()}_ {self.getName()}"
