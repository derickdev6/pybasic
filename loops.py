def run():
    LIMIT = 100000000
    counter = 0
    power = 2**counter
    while power < LIMIT:
        print('2 a la ' + str(counter) + ' = ' + str(power))
        counter += 1
        power = 2**counter


def forloop():
    a = range(50, 101)
    for i in a:
        print(i)
    a = list(a)
    print(a)


if __name__ == '__main__':
    run()
    forloop()
    print('End')
