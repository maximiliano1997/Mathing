from Fraccion.fraccion import Fraccion, FraccionMixta


''' SUMA DE FRACCIONES'''

# Suma 1
# s1f1 = Fraccion(3, 5)
# s1f2 = Fraccion(1, 4)

# resultado1 = f'{s1f1.suma(s1f2)}'
# print(resultado1)


sumaFracciones = [
    [Fraccion(3, 5), Fraccion(1, 4)],  # '''1'''
    [Fraccion(7, 2), Fraccion(5, 3)],  # '''2'''
    [Fraccion(1, 3), Fraccion(2, 7)],  # '''3'''
    [Fraccion(5, 4), Fraccion(3, 8)],  # '''4'''
    [Fraccion(2, 7), Fraccion(1, 6)],  # '''5'''
    [Fraccion(8, 9), Fraccion(2, 5)],  # '''6'''
    [Fraccion(6, 11), Fraccion(4, 9)],  # '''7'''
    [Fraccion(9, 2), Fraccion(5, 3)],  # '''8'''
    [Fraccion(4, 5), Fraccion(7, 8)],  # '''9'''
    [Fraccion(7, 3), Fraccion(1, 2)],  # '''10'''
    [Fraccion(5, 8), Fraccion(3, 10)],  # '''11'''
    [Fraccion(1, 6), Fraccion(4, 9)],  # '''12'''
    [Fraccion(3, 4), Fraccion(1, 5)],  # '''13'''
    [Fraccion(2, 11), Fraccion(5, 6)],  # '''14'''
    [Fraccion(5, 6), Fraccion(2, 9)],  # '''15'''
    [Fraccion(7, 9), Fraccion(3, 4)],  # '''16'''
    [Fraccion(4, 3), Fraccion(2, 7)],  # '''17'''
    [Fraccion(1, 8), Fraccion(7, 12)],  # '''18'''
    [Fraccion(11, 5), Fraccion(2, 3)],  # '''19'''
    [Fraccion(9, 7), Fraccion(5, 8)],  # '''20'''
]

counter = 0
for fraccion in sumaFracciones:
    counter += 1
    # print(
    #     f'Ejercicio.{counter} \n Resultado Suma {fraccion[0]} + {fraccion[1]} = {fraccion[0].suma(fraccion[1].simplifica())}')


restaFracciones = [
    [Fraccion(3, 5), Fraccion(1, 4)],  # '''1'''
    [Fraccion(7, 2), Fraccion(5, 3)],  # '''2'''
    [Fraccion(1, 3), Fraccion(2, 7)],  # '''3'''
    [Fraccion(5, 4), Fraccion(3, 8)],  # '''4'''
    [Fraccion(2, 7), Fraccion(1, 6)],  # '''5'''
    [Fraccion(8, 9), Fraccion(2, 5)],  # '''6'''
    [Fraccion(6, 11), Fraccion(4, 9)],  # '''7'''
    [Fraccion(9, 2), Fraccion(5, 3)],  # '''8'''
    [Fraccion(4, 5), Fraccion(7, 8)],  # '''9'''
    [Fraccion(7, 3), Fraccion(1, 2)],  # '''10'''
    [Fraccion(5, 8), Fraccion(3, 10)],  # '''11'''
    [Fraccion(1, 6), Fraccion(4, 9)],  # '''12'''
    [Fraccion(3, 4), Fraccion(1, 5)],  # '''13'''
    [Fraccion(2, 11), Fraccion(5, 6)],  # '''14'''
    [Fraccion(5, 6), Fraccion(2, 9)],  # '''15'''
    [Fraccion(7, 9), Fraccion(3, 4)],  # '''16'''
    [Fraccion(4, 3), Fraccion(2, 7)],  # '''17'''
    [Fraccion(1, 8), Fraccion(7, 12)],  # '''18'''
    [Fraccion(11, 5), Fraccion(2, 3)],  # '''19'''
    [Fraccion(9, 7), Fraccion(5, 8)],  # '''20'''
]
restaCounter = 0
for fraccion in restaFracciones:
    restaCounter += 1
    # print(
    #     f'Ejercicio.{restaCounter} \n Resultado Resta: {fraccion[0]} - {fraccion[1]} = {fraccion[0].resta(fraccion[1]).simplifica()}')

# MULTIPLICACION

multiplicaFracciones = [
    [Fraccion(3, 5), Fraccion(1, 4)],  # '''1'''
    [Fraccion(7, 2), Fraccion(5, 3)],  # '''2'''
    [Fraccion(1, 3), Fraccion(2, 7)],  # '''3'''
    [Fraccion(5, 4), Fraccion(3, 8)],  # '''4'''
    [Fraccion(2, 7), Fraccion(1, 6)],  # '''5'''
    [Fraccion(8, 9), Fraccion(2, 5)],  # '''6'''
    [Fraccion(6, 11), Fraccion(4, 9)],  # '''7'''
    [Fraccion(9, 2), Fraccion(5, 3)],  # '''8'''
    [Fraccion(4, 5), Fraccion(7, 8)],  # '''9'''
    [Fraccion(7, 3), Fraccion(1, 2)],  # '''10'''
    [Fraccion(5, 8), Fraccion(3, 10)],  # '''11'''
    [Fraccion(1, 6), Fraccion(4, 9)],  # '''12'''
    [Fraccion(3, 4), Fraccion(1, 5)],  # '''13'''
    [Fraccion(2, 11), Fraccion(5, 6)],  # '''14'''
    [Fraccion(5, 6), Fraccion(2, 9)],  # '''15'''
    [Fraccion(7, 9), Fraccion(3, 4)],  # '''16'''
    [Fraccion(4, 3), Fraccion(2, 7)],  # '''17'''
    [Fraccion(1, 8), Fraccion(7, 12)],  # '''18'''
    [Fraccion(11, 5), Fraccion(2, 3)],  # '''19'''
    [Fraccion(9, 7), Fraccion(5, 8)],  # '''20'''
]

multiCounter = 0
for fraccion in multiplicaFracciones:
    multiCounter += 1
    # print(
    #     f'Ejercicio.{multiCounter} \n Resultado multiplicacion: {fraccion[0]} * {fraccion[1]} = {fraccion[0].producto(fraccion[1]).simplifica()}')


# DIVISION DE FRACCIONES

divisionFracciones = [
    [Fraccion(3, 5), Fraccion(1, 4)],  # '''1'''
    [Fraccion(7, 2), Fraccion(5, 3)],  # '''2'''
    [Fraccion(1, 3), Fraccion(2, 7)],  # '''3'''
    [Fraccion(5, 4), Fraccion(3, 8)],  # '''4'''
    [Fraccion(2, 7), Fraccion(1, 6)],  # '''5'''
    [Fraccion(8, 9), Fraccion(2, 5)],  # '''6'''
    [Fraccion(6, 11), Fraccion(4, 9)],  # '''7'''
    [Fraccion(9, 2), Fraccion(5, 3)],  # '''8'''
    [Fraccion(4, 5), Fraccion(7, 8)],  # '''9'''
    [Fraccion(7, 3), Fraccion(1, 2)],  # '''10'''
    [Fraccion(5, 8), Fraccion(3, 10)],  # '''11'''
    [Fraccion(1, 6), Fraccion(4, 9)],  # '''12'''
    [Fraccion(3, 4), Fraccion(1, 5)],  # '''13'''
    [Fraccion(2, 11), Fraccion(5, 6)],  # '''14'''
    [Fraccion(5, 6), Fraccion(2, 9)],  # '''15'''
    [Fraccion(7, 9), Fraccion(3, 4)],  # '''16'''
    [Fraccion(4, 3), Fraccion(2, 7)],  # '''17'''
    [Fraccion(1, 8), Fraccion(7, 12)],  # '''18'''
    [Fraccion(11, 5), Fraccion(2, 3)],  # '''19'''
    [Fraccion(9, 7), Fraccion(5, 8)],  # '''20'''
]

divisionCounter = 0
for fraccion in divisionFracciones:
    divisionCounter += 1
    # print(
    #     f'Ejercicio.{divisionCounter} \n Resultado division: {fraccion[0]} / {fraccion[1]} = {fraccion[0].cociente(fraccion[1]).simplifica()}')


'''Fracciones Mixtas A Impropias'''
fracciones_mixtas_a_impropias = [
    FraccionMixta(2, Fraccion(2, 5)),
    FraccionMixta(7, Fraccion(3, 6)),
    FraccionMixta(1, Fraccion(2, 9)),
    FraccionMixta(15, Fraccion(14, 5)),
]

for fraccionMixta in fracciones_mixtas_a_impropias:
    print(f'{fraccionMixta} a impropia: {fraccionMixta.a_impropia()}')

'''Fracciones Impropias a Mixtas'''

fracciones_impropias_a_mixtas = [
    Fraccion(15, 5),
    Fraccion(105, 9),
    Fraccion(2, 2),
    Fraccion(3001, 10),
    Fraccion(18, 9),
]

for fraccion in fracciones_impropias_a_mixtas:
    print(f'{fraccion} a mixta: {fraccion.a_mixta()}')


# BONUES EXTRAS

f1 = Fraccion(1, 6)
f2 = Fraccion(2, 6)
f3 = Fraccion(3, 6)

print(f'{f1.suma(f2).suma(f3).simplifica()}')
