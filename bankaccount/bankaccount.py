# bankaccount.py
import random
import sys

tab = {
    "4000008721279422": "1916"
}

def create_card():
    while True:
        _tmp_0 = 4000000000000000
        _tmp_1 = random.randint(0, 9999999999)
        _tmp_2 = random.randint(0, 9999)

        ind = "{0:16}".format(_tmp_0 + _tmp_1)
        if luhn_algorithm(ind):
            tab["{}".format(ind)] = '{0:04}'.format(_tmp_2)
            return ind
        else:
            continue

def logging():
    a = input("\nEnter your card number:\n")
    b = input("Enter your PIN:\n")
    if a in tab and luhn_algorithm(a):
        if b == tab[a]:
            return a
    return False

def balance():
    return 0

def luhn_algorithm(id_number):
    x = list(id_number).pop()  # Drop the last digit
    u = id_number[:-1]
    # multiply odd digits by two
    tab_i = []
    aa = 1
    for i in list(u):
        if not aa % 2 == 0:
            tab_i.append(int(i) * 2)
        else:
            tab_i.append(int(i))
        aa = aa + 1
    # Substract 9 to numbers ovr 9
    a = 0
    for ii in tab_i:
        if ii > 9:
            tab_i[a] = ii - 9
        a = a + 1
    tab_i.append(int(x))
    b = sum(tab_i)
    if b % 10 == 0:
        return True
    return False

def main():
    while True:
        a = input("1. Create an account\n2. Log into account\n0. Exit\n")
        if a == "1":
            _tmp_id = create_card()
            if _tmp_id == False:
                continue
            print("\nYour card has been created")
            print("Your card number:\n{}".format(_tmp_id))
            print("Your card PIN:\n{}\n".format(tab[_tmp_id]))
        elif a == "2":
            ind = logging()
            if ind:
                print("\nYou have successfully logged in!\n")
                while True:
                    aa = input("1. Balance\n2. Log out\n0. Exit\n")
                    if aa == "0":
                        print("\nBye!")
                        exit(0)
                    elif aa == "2":
                        print("\nYou have successfully logged out!\n")
                        break
                    elif aa == "1":
                        print("\nBalance: {}\n".format(balance()))
            else:
                print("\nWrong card number or PIN!\n")
        else:
            break
    print("\nBye!")

if __name__ == "__main__":
    # execute only if run as a script
    main()
