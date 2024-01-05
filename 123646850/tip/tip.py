'''def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    doller=d.replace("$","")
    doller=float(d)
    return doller

def percent_to_float(p):
    percent=p.replace("%","")
    percent=float(p)/100
    return percent


main()'''
def main():
    dollars = dollars_to_float(input("How much was the meal? ").replace("$",""))
    percent = percent_to_float(input("What percentage would you like to tip? ").replace("%",""))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d)

def percent_to_float(p):
    return float(p) / 100

main()

