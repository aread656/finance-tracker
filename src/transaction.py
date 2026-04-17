import uuid
class Transaction:
    def __init__(self,amount,category,date,description,type):
        self.id = str(uuid.uuid4().hex[:8]) 
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.type = type
        return
    
    def __str__(self):
        type_str = "Income" if self.type else "Expense"
        return f"{self.id} | {self.date} | {type_str} | {self.category} | {self.amount} | {self.description}"
    
    def setAmount(self,amt):
        return
    def setCategory(self,cat):
        return
    def setDate(self,date):
        return
    def setDescription(self,desc):
        return

    def getDescription(self):
        return self.description
    def getDate(self):
        return self.date
    def getCategory(self):
        return self.category
    def getAmount(self):
        return self.amount
#initialise a new transaction object, validating the input