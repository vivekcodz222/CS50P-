while True:
    try:
        tank_input = input("Fraction: ")
        x, y = tank_input.split("/")
        convert_x = int(x)
        convert_y = int(y)
        tank_percent = (convert_x / convert_y) * 100
        if tank_percent <= 1:
            print("E")
            break
        elif convert_x > convert_y:
            pass
        elif tank_percent >= 99:
            print("F")
            break
        else:
            print(round(tank_percent),"%", sep="")
            break
    except (ValueError, ZeroDivisionError):
        pass