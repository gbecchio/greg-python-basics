# credit.py
import math
import sys
import argparse

calculate = "What do you want to calculate?\n" \
            "type \"n\" - for count of months,\n" \
            "type \"a\" - for annuity monthly payment,\n" \
            "type \"p\" - for credit principal:\n"
enter_credit_principal = "Enter credit principal:\n"
enter_monthly_payment = "Enter monthly payment:\n"
enter_credit_interest = "Enter credit interest:\n"
enter_count_of_periods = "Enter credit interest:\n"

type_p = ''
principal = ''
periods = ''
interest = ''

def init():
    parser = argparse.ArgumentParser(prog = 'top', description = 'Cool program')
    parser.add_argument("--type", type=str)
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--payment", type=float)
    args = parser.parse_args()
    return args

def credit(p, pr, i):
    n = math.ceil(math.log((p / (p - i * pr)), (1 + i)))
    return n

def annuity_principal(p, n, i):
    haut = (i * math.pow((1 + i), n))
    bas = math.pow((1 + i), (n)) - 1

    principal = int((p) / ((haut) / (bas)))
    return principal

def annuity_payments(p, n, i):
    haut = (i * math.pow((1 + i), n))
    bas = math.pow((1 + i), (n)) - 1

    annuity_p = math.ceil(p * ((haut) / (bas)))
    return annuity_p

def diff_payment(p, n, i, m):
    a = p/n
    b = i * (p - (((p * (m -1))) / (n)))
    return math.ceil(a + b)

def mess_error(args):
    if len(sys.argv) < 5:
        print("Incorrect parameters.")
        sys.exit(10)

    if (args.periods != None and args.periods < 0)\
        or (args.payment != None and args.payment < 0)\
        or (args.principal != None and args.principal < 0)\
        or (args.interest != None and args.interest < 0):
        print("Incorrect parameters.")
        sys.exit(20)

    if args.type not in ("annuity", "diff"):
        print("Incorrect parameters.")
        sys.exit(1)

    if args.type == "diff" and args.payment != None:
        print("Incorrect parameters.")
        sys.exit(2)

    if args.type in ("diff", "annuity") and args.interest == None:
        print("Incorrect parameters.")
        sys.exit(3)




def main():
    args = init()
    mess_error(args)

    if args.type == "diff":
        interest = (args.interest / 100) / (12 * 1)
        payd_out = 0
        sum_payd_out = 0
        for i in range(1, args.periods + 1):
            payd_out = diff_payment(
                args.principal,
                args.periods,
                interest,
                i
            )
            sum_payd_out = sum_payd_out + payd_out
            print("Month {}: paid out {}".format(i, payd_out))
        print()
        print("Overpayment = {}".format(int(sum_payd_out - args.principal)))
    elif args.type == "annuity" and args.payment != None and args.principal != None:
        i = (args.interest / 100) / (12 * 1)
        n = credit(args.payment, args.principal, i)

        years = int(n / 12)
        months = int(((n / 12) - years) * 12)
        # years = months
        if years == 0:
            print("You need {} months to repay this credit!".format(months))
        elif months == 0:
            print("You need {} years to repay this credit!".format(years))
        else:
            print("You need {} years and {} months to repay this credit!".format(years, months))
        print("Overpayment = {}".format(int(((n * args.payment) - args.principal))))
    elif args.type == "annuity" and args.principal != None:
        interest = (args.interest / 100) / (12 * 1)

        a_p = annuity_payments(args.principal, args.periods, interest)
        print("Your annuity payment = {}!".format(a_p))
        print("Overpayment = {}".format(int((a_p * args.periods) - args.principal)))
    elif args.type == "annuity" and args.payment != None:
        interest = (args.interest / 100) / (12 * 1)

        a_p = annuity_principal(args.payment, args.periods, interest)
        print("Your credit principal = {}!".format(a_p * args.periods))
        print("Overpayment = {}".format(int((a_p * args.periods) - args.payment)))

if __name__ == "__main__":
    main()
