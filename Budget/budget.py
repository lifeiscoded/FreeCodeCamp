from typing import List

class Category :
    
    def __init__(self, name: str):
        self.__categoryName = name
        self.__ledger = []
        self.__balance = 0.0
        self.__desc = ""
        self.__withdrawCount = 0        
    
    def deposit(self,amount: float, description: str = ""):
        
        self.__balance += amount
        self.__ledger.append({"amount" : amount, "description" : description})
    
    def withdraw(self,amount: float, description: str = ""):
        isEnough = self.check_funds(amount)
        
        if isEnough:
            self.__withdrawCount += 1
            self.__balance -= amount
            self.__ledger.append({"amount" : amount * -1, "description" : description})
            return True
        else:
            return False
    
    def get_balance(self):
        return self.__balance
    
    def transfer(self,amount: float,cat: "Category"):
        isEnough = self.check_funds(amount)
        if not isEnough:
            return False
        else:
            self.__desc = "Transfer to {0}".format(cat.categoryName)
            to = "Transfer from {0}".format(self.__categoryName)
            self.withdraw(amount, self.__desc)
            cat.deposit(amount,to)
            return True
        
    def check_funds(self,amount: float):
        if self.__balance  < amount :
            return False
        else:
            return True
    def Print(self):
        l = len(self.__categoryName)
        ind = int((30 - l)/2) 
        firstLine = ""
        
        for i in range(ind): firstLine += "*"
        firstLine += self.__categoryName
        for k in range(30 - len(firstLine)): firstLine += "*"
        print(firstLine)        
        
        for i in self.__ledger:
            d = i["description"]
            amount = "{:.2f}".format(i["amount"])
            amountLenght = len(amount)
            descLenght = len(d)
            if descLenght + amountLenght > 29: 
                d = d[0:(29- amountLenght)]
                descLenght = len(d)
            if amountLenght > 7:
                amount = amount[0:7]
                amountLenght = len(amount)
            totalLenght = amountLenght + descLenght
            for j in range(30 - totalLenght): 
                d += " " 
            d += amount
            print(d)
        print ("Total : ", self.__balance)
        
def create_spend_chart(catList: List[Category]):
    print("Percentage spent by category")
    withdraws = []
    wTotal = 0
    
    for c in catList:
        wOnce = 0
        for w in c.ledger:
            if w["amount"] < 0:
              wTotal += w["amount"]
              wOnce += w["amount"]
        withdraws.append({"category" : c.categoryName,"withdraw" : wOnce})

    for i in reversed(range(0,110,10)):
        ch = ""
        perc = str(i)
        blanks = ""
        for j in range(3-len(perc)):
            blanks += " "
        finalStr = perc + "| "
        
        for w in withdraws:
            rounded = int(round((((-1 * w["withdraw"]) / wTotal * -1) * 100),-1))            
            if(rounded >= i):
                finalStr += "o  "
            else:
                finalStr += "   "
        print(blanks + finalStr)
    
    maxL = 0
    
    #Dash creation
    leftOver = "    "
    for i in range(len(catList) + 2): leftOver += "--"
    
    #find max lenght of category name
    for c in catList:
        if maxL < len(c.categoryName): maxL = len(c.categoryName)
    
    #Start writing category names
    leftOver += "\n     "
    for x in range(0,maxL):
        for c in catList:
            try:
                leftOver += c.categoryName[x] + "  "
            except IndexError:
                leftOver += "   "
        leftOver += "\n     "
    print(leftOver)
    
