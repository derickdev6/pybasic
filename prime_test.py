def main():
    for i in range(100):
        if test(i):
            print(i)


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
