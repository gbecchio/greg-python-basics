# caffe.py

"""
The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money
"""

class Caffe:
    tab = {
        "water": 400,
        "milk": 540,
        "coffee beans": 120,
        "disposable cups": 9,
        "money": 550 
    }
    def __init__(self, message):
        self.action = message

    def action_go(self):
        if self.action == "buy":
            a = self.buy()
            if a == "continue":
                pass
            print(a)
            print()
        elif self.action == "fill":
            self.fill()
            print()
        elif self.action == "take":
            self.take()
            print()
        elif self.action == "remaining":
            print()
            self.coffemachine_state()
            print()
        elif self.action == "exit":
            self.exit_coffe()
            exit()
        else:
            print(None)

    def verif_qty(self, element, quantity):
        if self.tab[element] - quantity <= 0:
            return "Sorry, not enough {}!".format(element)

    """
    buy:

    If a user wants to buy some coffee, the input is "buy".

    They must choose one of three types of coffee that the coffee machine can make: 
    - espresso ;
    - latte ; 
    - cappuccino. 
    """
    def buy(self):
        print()
        choose = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        try:
            if int(choose) == 1:
                a = self.verif_qty("water", 250)
                if a is not None:
                    return a
                a = self.verif_qty("coffee beans", 16)
                if a is not None:
                    return a
                """
                For one espresso, the coffee machine needs : 
                - 250 ml of water ;
                - 16 g of coffee beans. 

                It costs $4.
                """
                self.tab["water"] = self.tab["water"] - 250
                self.tab["coffee beans"] = self.tab["coffee beans"] - 16
                self.tab["money"] = self.tab["money"] + 4
                
            elif int(choose) == 2:
                a = self.verif_qty("water", 350)
                if a is not None:
                    return a
                a = self.verif_qty("milk", 75)
                if a is not None:
                    return a
                a = self.verif_qty("coffee beans", 20)
                if a is not None:
                    return a
                """
                For a latte, the coffee machine needs :
                - 350 ml of water ; 
                - 75 ml of milk ; 
                - 20 g of    coffee beans. 

                It costs $7.
                """
                self.tab["water"] = self.tab["water"] - 350
                self.tab["milk"] = self.tab["milk"] - 75
                self.tab["coffee beans"] = self.tab["coffee beans"] - 20
                self.tab["money"] = self.tab["money"] + 7
            elif int(choose) == 3:
                a = self.verif_qty("water", 200)
                if a is not None:
                    return a
                a = self.verif_qty("milk", 100)
                if a is not None:
                    return a
                a = self.verif_qty("coffee beans", 12)
                if a is not None:
                    return a
                """
                For a cappuccino, the coffee machine needs : 
                - 200 ml of water ;
                - 100 ml of milk ; 
                - 12 g of coffee beans. 

                It costs $6.
                """
                self.tab["water"] = self.tab["water"] - 200
                self.tab["milk"] = self.tab["milk"] - 100
                self.tab["coffee beans"] = self.tab["coffee beans"] - 12
                self.tab["money"] = self.tab["money"] + 6
        except ValueError:
            if choose == "back":
                return "continue"
        self.tab["disposable cups"] = self.tab["disposable cups"] - 1
        return "I have enough resources, making you a coffee!"

    """
    file:
    If a special worker thinks that it is time to fill out all the supplies for the coffee machine, 
    the input line will be "fill". 
    """
    def fill(self):
        """
        If the user writes "fill", the program should ask them how much :
        - water ; 
        - milk ;
        - coffee ;
        - how many disposable cups.
        they want to add into the coffee machine.
        """
        print()
        water = int(input("Write how many ml of water do you want to add:\n"))
        milk = int(input("Write how many ml of milk do you want to add:\n"))
        beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        
        self.tab["water"] = self.tab["water"] + water
        self.tab["milk"] = self.tab["milk"] + milk
        self.tab["coffee beans"] = self.tab["coffee beans"] + beans
        self.tab["disposable cups"] = self.tab["disposable cups"] + cups
        return self.tab
    """
    take:
    If another special worker decides that it is time to take out the money from the coffee machine, 
    you'll get the input "take".
    """
    def take(self):
        """
        The program should give all the money that it earned from selling coffee.
        """
        print()
        print("I gave you ${}".format(self.tab["money"]))
        self.tab["money"] = 0
        return self.tab
    """
    The coffee machine has:
    400 of water
    540 of milk
    120 of coffee beans
    9 of disposable cups
    550 of money
    """
    def coffemachine_state(self):
        print("The coffee machine has:")
        for a,b in self.tab.items():
            print("{} of {}".format(b, a))

    def exit_coffe(self):
        exit()

#def main():
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    caffe = Caffe(action)
    caffe.action_go()

#if __name__ == "__main__":
    # execute only if run as a script
#    main()
