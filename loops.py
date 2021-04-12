def run():
    LIMIT = 100000000
    counter = 0
    power = 2**counter
    while power < LIMIT:
        print('2 a la ' + str(counter) + ' = ' + str(power))
        counter += 1
        power = 2**counter


def forloop():
    name = input('Type your name: ')
    # for char in range(len(name)):
    #     print(name[char])
    for char in name:
        print(char.upper())


if __name__ == '__main__':
    forloop()
    print('End')
