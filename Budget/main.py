from budget import *

def main():
    f = Category("Food")
    c = Category("Clothing")
    a = Category("Auto")
    
    f.deposit(1000,"Initial deposit")
    c.deposit(1000,"Initial deposit")
    a.deposit(1000,"Initial deposit")
    
    f.withdraw(10.15,"groceries")
    f.withdraw(15.89,"restaurant and more foo1234")
    f.transfer(50,c)
    
    c.withdraw(10.15,"groceries")
    c.withdraw(15.89,"restaurant and more foo1234")
    
    a.withdraw(10.15,"groceries")
    
    f.Print()    
    
    create_spend_chart([f,c,a])
        
if __name__ == "__main__":
    main()
