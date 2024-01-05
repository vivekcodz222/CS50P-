# Dictonary set up
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# create an empty list
total = [ ]

#Loop within a loop: accepts input and outputs cumulative total
while True:
    try:
            order = input("What do you want to order: ").title( )
            if order in menu:
                price = menu[order]
                total.append(price)
                bill = sum(total)
                print(f"${bill:.2f}")
#This re-prompts for input as item is not found in dictionary menu
    except KeyError:
        order
#This error makes the exit code happen
    except EOFError:
      break