def run():
    number = 2
    counter = 2
    while number * 2 < 1000000:
        number = number * 2
        print(str(counter) + ' ' + str(number))
        counter += 1


if __name__ == '__main__':
    run()
    print('End')
