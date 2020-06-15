# machine_a_cafe.py
"""
The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money
"""

tab = {
    "water": 400,
    "milk": 540,
    "coffee beans": 120,
    "disposable cups": 9,
    "money": 550 
}


"""
buy:

If a user wants to buy some coffee, the input is "buy".

They must choose one of three types of coffee that the coffee machine can make: 
- espresso ;
- latte ; 
- cappuccino. 
"""
def buy():
    choose = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
    if choose == 1:
        """
        For one espresso, the coffee machine needs : 
        - 250 ml of water ;
        - 16 g of coffee beans. 

        It costs $4.
        """
        tab["water"] = tab["water"] - 250
        tab["coffee beans"] = tab["coffee beans"] - 16
        tab["money"] = tab["money"] + 4
        
    elif choose == 2:
        """
        For a latte, the coffee machine needs :
        - 350 ml of water ; 
        - 75 ml of milk ; 
        - 20 g of coffee beans. 

        It costs $7.
        """
        tab["water"] = tab["water"] - 350
        tab["milk"] = tab["milk"] - 75
        tab["coffee beans"] = tab["coffee beans"] - 20
        tab["money"] = tab["money"] + 7
    elif choose == 3:
        """
        For a cappuccino, the coffee machine needs : 
        - 200 ml of water ;
        - 100 ml of milk ; 
        - 12 g of coffee beans. 

        It costs $6.
        """
        tab["water"] = tab["water"] - 200
        tab["milk"] = tab["milk"] - 100
        tab["coffee beans"] = tab["coffee beans"] - 12
        tab["money"] = tab["money"] + 6
    tab["disposable cups"] = tab["disposable cups"] - 1
    return tab

"""
file:
If a special worker thinks that it is time to fill out all the supplies for the coffee machine, 
the input line will be "fill". 
"""
def fill():
    """
    If the user writes "fill", the program should ask them how much :
    - water ; 
    - milk ;
    - coffee ;
    - how many disposable cups.
    they want to add into the coffee machine.
    """
    water = int(input("Write how many ml of water do you want to add:\n"))
    milk = int(input("Write how many ml of milk do you want to add:\n"))
    beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    
    tab["water"] = tab["water"] + water
    tab["milk"] = tab["milk"] + milk
    tab["coffee beans"] = tab["coffee beans"] + beans
    tab["disposable cups"] = tab["disposable cups"] + cups
    return tab
"""
take:
If another special worker decides that it is time to take out the money from the coffee machine, 
you'll get the input "take".
"""
def take():
    """
    The program should give all the money that it earned from selling coffee.
    """
    print("I gave you ${}".format(tab["money"]))
    tab["money"] = 0
    return tab
"""
The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money
"""
def coffemachine_state():
    print("The coffee machine has:")
    for a,b in tab.items():
        print("{} of {}".format(b, a))

def main():
    coffemachine_state()
    print()
    action = input("Write action (buy, fill, take):\n")
    if action == "buy":
        buy()
        print()
        coffemachine_state()
    elif action == "fill":
        fill()
        print()
        coffemachine_state()
    elif action == "take":
        take()
        print()
        coffemachine_state()
    else:
        print(None)

if __name__ == "__main__":
    # execute only if run as a script
    main()
