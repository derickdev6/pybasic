import random


def passgen():
    minus = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    mayus = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    symbol = ('!', '?', '.', ',')
    items = []
    for i in range(10):
        opt = random.randint(1, 4)
        if opt == 1:
            pick = random.randint(0, 25)
            items.append(minus[pick])
        elif opt == 2:
            pick = random.randint(0, 25)
            items.append(mayus[pick])
        elif opt == 3:
            pick = random.randint(0, 3)
            items.append(symbol[pick])
        elif opt == 4:
            pick = random.randint(0, 9)
            items.append(str(pick))
    password = items[0] + items[1] + items[2] + items[3] + \
        items[4] + items[5] + items[6] + items[7] + items[8] + items[9]
    return password


def run():
    password = passgen()
    print('Your new password is ' + password)


if __name__ == '__main__':
    run()
