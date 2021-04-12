def run():
    for counter in range(20):
        if counter % 2 != 0:
            continue
        print(counter)
        if counter == 10:
            break


if __name__ == '__main__':
    run()
