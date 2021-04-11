# def salute(name, age):
#     print('Hello ' + name + '. Happy ' + str(age) + 'th birthday')


# derick = ['Derick', 19]
# salute(derick[0], derick[1])

# --------------------------------------------

# def conversation(opt):
#     print('Hey\nYou chose option '+str(opt))


# opt = int(input('Option: '))
# conversation(opt)

# ---------------------------------------------

def convert_to_dls(currency, cuantity):
    if currency == 1:
        dls = cuantity * 0.00027
    elif currency == 2:
        dls = cuantity * 0.0014
    elif currency == 3:
        dls = cuantity * 0.050
    else:
        return
    return round(dls, 2)


print('Select a currency: \n1. COP💵\n2. CHI💵\n3. MEX💵')

opt = int(input('Option: '))
while (opt > 3) or (opt < 1):
    opt = int(input('Option: '))

pesos = float(input('Pesos: $'))

dls = convert_to_dls(opt, pesos)
print('$' + str(dls))
