from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
lst = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(lst))
    word = input("Input: ")
    print(figlet.renderText(word))
elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in lst:
        figlet.setFont(font=sys.argv[2])
        word = input("Input: ").strip()
        print(figlet.renderText(word))
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)