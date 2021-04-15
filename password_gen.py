import random


def passgen(size):
    password = []
    minus = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    mayus = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    symbols = ('!', '?', '.', ',', '_', '#')
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    chars = minus + mayus + numbers + symbols
    for i in range(size):
        randchar = random.choice(chars)
        password .append(randchar)
    return ''.join(password)


def run():
    password = passgen(15)
    print('Your new password is ' + password)


if __name__ == '__main__':
    run()
