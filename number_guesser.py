import random


def run():
    lifes = 5
    rand_number = random.randint(0, 100)
    while True:
        if lifes == 0:
            print('You lost :(')
            break
        print('Try to guess')
        chosen = int(input(': '))
        if rand_number > chosen:
            lifes -= 1
            print('> - Lifes left: ' + str(lifes))
        elif rand_number < chosen:
            lifes -= 1
            print('< - Lifes left: ' + str(lifes))
        else:
            print('Congratulations!')
            break


if __name__ == '__main__':
    run()
    print('\nEnd of program... \n')
