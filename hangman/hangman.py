import random
import string

# Write your code here
w = [
    'python',
    'java',
    'kotlin',
    'javascript'
]

deja = []

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def menu():
    menu = "play"
    while True:
        menu = input('Type "play" to play the game, "exit" to quit: ')
        if menu == "play":
            return True
        elif menu == "exit":
            return False

def main():
    if menu():
        random.shuffle(w)
        n = len(w[0])
        print("H A N G M A N")
        x = "{}".format("-" * n)

        t = 1

        while t != 9:
            print("")
            print("{}".format(x))
            a = input("Input a letter: ")
            if not (len(a) == 1):
                print("You should input a single letter")
                continue
            if a not in string.ascii_letters.lower():
                print("It is not an ASCII lowercase letter")
                continue
            if a in deja:
                print("You already typed this letter")
                continue
            else:
                deja.append(a)
            try:
                b = list(find_all(w[0], a))
                if b == []:
                    t = t + 1
                    print("No such letter in the word")
                for bb in b:
                    xx = list(x)
                    xx[bb] = a
                    x = "".join(xx)
            except:
                pass
            if w[0] == x:
                break
        if w[0] == x:
            print("You guessed the word {}!\nYou survived!".format(w[0]))
        else:
            print("You are hanged!")

if __name__ == "__main__":
    # execute only if run as a script
    main()