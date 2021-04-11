def palindromo(word):
    word = word.lower().strip().replace(' ', '')
    return word == word[::-1]


def run():
    word = input('Type the word for check: ')
    if palindromo(word):
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()
