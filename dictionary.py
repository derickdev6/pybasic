def run():
    # dictionary = {
    #     'k1': 1,
    #     'k2': 'Two',
    #     'k3': True,
    # }
    # print(dictionary['k1'])

    popul = {
        'ARG': 44938712,
        'BRA': 210147125,
        'COL': 50372424
    }
    # print(popul['ARG'])

    for country in popul.keys():
        print(country)

    for pop in popul.values():
        print(pop)
    for country, pop in popul.items():
        print(country + ' ' + str(pop))


if __name__ == '__main__':
    run()
    print('\nEnd of program...\n')
