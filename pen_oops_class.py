import time  #used only for beautification 

'''This is a pen vending machine implemented using object oriented programming
I have debugged it as much as possible but there may be some corner cases where it generates issues
'''

class shop:
    earn = 0
    def __init__(self, pens, cost):
        self.npen = pens
        self.cost = cost
    def buy(self, money, qty):
        if self.npen<qty:
            print("Sorry, out of stock for your order.\n")
        else:
            price = self.cost*qty
            if money< price:
                print("Sorry, cost is higher.\n")
            else:
                print("Transaction successful.\n", qty , " pens bought.")
                print(money-price , " money returned as change.\n")
                self.npen -= qty
                self.earn += price

print("Initialising machine....\n")
pens , cost = int(input("Enter stock of pens : ")), int(input("Enter unit cost : "))
print("LOADING....\n---------------------------\n")
obj = shop(pens , cost)  #starting the machine from user's point of view
print("Note : Machine will close as soon as its stock gets 0.\n")
while obj.npen>0:    #verifying that there is some pens left unsold
    print("To close enter 0. To continue ordering enter 1. Any other entry is invalid.\n")
    val = input("Enter 0/1 : ") #giving choice to user to close the machine before all pens are sold
    if val == "0":
        break
    elif val == "1":
        print("Your transaction begins....\n")
        qty , mon = int(input("Enter quantity : ")),int(input("Insert money : "))
        obj.buy(mon, qty)
time.sleep(2)
print("\nTrasactions closed........\n")
print("Amount earned : ", obj.earn) #showing the total earnings of machine in that session. can be saved in a text/dat file or a mysql database 
print("Machine closing")
for i in range(5):
    print(" . ", end = "")
    time.sleep(0.2)

