def input_coffe(message):
	return int(input(message))

tab = {
    "water": 200,
    "milk": 50,
    "beans": 15
}

def main():
    water = input_coffe("Write how many ml of water the coffee machine has:\n")
    milk = input_coffe("Write how many ml of milk the coffee machine has:\n")
    beans = input_coffe("Write how many grams of coffee beans the coffee machine has:\n")
    cups = input_coffe("Write how many cups of coffee you will need:\n")

    print(water)
    print(milk)
    print(beans)
    print(cups)

    minimum = min((water // tab["water"]), (milk // tab["milk"]), (beans // tab["beans"]))

    if water >= tab["water"] and milk >= tab["milk"] and beans >= tab["beans"]:
        if minimum > cups:
            return "Yes, I can make that amount of coffee (and even {} more than that)".format(minimum - cups)
        else:
            return "Yes, I can make that amount of coffee"
    else:
        return "No, I can make only {} cups of coffee".format(minimum)

if __name__ == "__main__":
    # execute only if run as a script
    print(main())