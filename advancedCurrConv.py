print('Select a currency: \n1. COP💵\n2. CHI💵\n3. MEX💵')

opt = int(input('Option: '))
while (opt > 3) or (opt < 1):
    opt = int(input('Option: '))

pesos = float(input('Pesos: $'))

if(opt == 1):
    dls = pesos * 0.00027
elif opt == 2:
    dls = pesos * 0.0014
elif opt == 3:
    dls = pesos * 0.050

dls = round(dls, 2)
print('$' + str(dls))
