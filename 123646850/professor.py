from random import randint

def main():
    level = get_level()
    count = attempt = 0
    score = 10
    while count < 10:
        x, y = generate_integer(level), generate_integer(level)
        while True:
            try:
                result = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                attempt += 1
            else:
                if result == x + y:
                    count += 1
                    attempt = 0
                    break
                else:
                    print("EEE")
                    attempt += 1
            if attempt == 3:
                print(f"{x} + {y} = {x + y}")
                score -= 1
                count += 1
                attempt = 0
                break
        if count == 10:
            print(f"Score: {score}")
            break


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
             return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        n = randint(0, 9)
    elif level == 2:
        n = randint(10, 99)
    elif level == 3:
        n = randint(100, 999)
    else:
        raise ValueError
    return n


if __name__ == "main":
    main()