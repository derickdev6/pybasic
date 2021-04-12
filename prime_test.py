def main():
    number = int(input('Type a number to test: '))
    print(test(number))


def test(number):
    is_prime = True

    if number == 1:
        return False
    for i in range(2, round(number/2) + 1):
        if number % i == 0:
            is_prime = False

    return is_prime


if __name__ == '__main__':
    main()
