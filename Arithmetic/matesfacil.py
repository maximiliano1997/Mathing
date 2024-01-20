from Fraccion.fraccion import Fraccion, FraccionMixta
counter = 0


def counterAdd():
    global counter
    counter += 1
    return counter


# SUMA Y RESTA DE FRACCIONES
''' Parte 1: denominador comun'''


suma1 = [Fraccion(4, 3), Fraccion(11, 3)]
resultado3 = f' Ejercicio {counterAdd()} \n {suma1[0].suma(suma1[1]).simplifica()}'
print(resultado3)


ejercicio2 = [Fraccion(3, 2), Fraccion(9, 2)]
resultado2 = f'Ejercicio {counterAdd()} \n Resultado de la fraccion: {ejercicio2[0].resta(ejercicio2[1]).simplifica()}'
print(resultado2)


ejercicio3 = [Fraccion(11, 7), Fraccion(23, 7)]
resultado3 = f'Ejercicio {counterAdd()} \n {ejercicio3[0].suma(ejercicio3[1]).simplifica()}'
print(resultado3)


ejercicio4 = [Fraccion(1, 5), Fraccion(2, 5)]
resultado4 = f'Ejercicio {counterAdd()} \n {ejercicio4[0].resta(ejercicio4[1]).simplifica()}'
print(resultado4)


ejercicio5 = [Fraccion(15, 14), Fraccion(13, 14)]
resultado5 = f'Ejercicio {counterAdd()} \n {ejercicio5[0].suma(ejercicio5[1]).simplifica()}'
print(resultado5)


ejercicio6 = [Fraccion(13, 2), Fraccion(31, 2)]
resultado6 = f'Ejercicio {counterAdd()} \n {ejercicio6[0].resta(ejercicio6[1]).simplifica()}'
print(resultado6)


ejercicio7 = [Fraccion(1, 6), Fraccion(2, 6), Fraccion(3, 6)]
resultado7 = f'Ejercicio {counterAdd()} \n {ejercicio7[0].suma(ejercicio7[1].suma(ejercicio7[2])).simplifica()}'
print(resultado7)


ejercicio8 = [Fraccion(40, 5), Fraccion(10, 5), Fraccion(5, 5)]
resultado8 = f'Ejercicio {counterAdd()} \n {ejercicio8[0].suma(ejercicio8[1].resta(ejercicio8[2])).simplifica()}'
print(resultado8)


ejercicio9 = [Fraccion(66, 4), Fraccion(33, 4), Fraccion(1, 4)]
resultado9 = f'Ejercicio {counterAdd()} \n {ejercicio9[0].resta(ejercicio9[1]).simplifica().resta(ejercicio9[2]).simplifica()}'
print(resultado9)


ejercicio10 = [Fraccion(-3, 9), Fraccion(3, 9)]
resultado10 = f'Ejercicio {counterAdd()} \n {ejercicio10[0].suma(ejercicio10[1]).simplifica()}'
print(resultado10)


ejercicio11 = [Fraccion(-5, 3), Fraccion(4, 3)]
resultado11 = f'Ejercicio {counterAdd()} \n {ejercicio11[0].resta(ejercicio11[1]).simplifica()}'
print(resultado11)


ejercicio12 = [Fraccion(-3, 10), Fraccion(2, 10), Fraccion(4, 10)]
resultado12 = f'Ejercicio {counterAdd()} \n {ejercicio12[0].resta(ejercicio12[1]).simplifica().suma(ejercicio12[2]).simplifica()}'
print(resultado12)


ejercicio13 = [Fraccion(-12, 11), Fraccion(1, 11), Fraccion(2, 11)]
resultado13 = f'Ejercicio {counterAdd()} \n {ejercicio13[0].suma(ejercicio13[1]).simplifica().resta(ejercicio13[2]).simplifica()}'
print(resultado13)


ejercicio14 = [Fraccion(-7, 8), Fraccion(5, 8), Fraccion(4, 8)]
resultado14 = f'Ejercicio {counterAdd()} \n {ejercicio14[0].resta(ejercicio14[1]).simplifica().resta(ejercicio14[2]).simplifica()}'
print(resultado14)


ejercicio15 = [Fraccion(34, 31), Fraccion(-3, 31)]
resultado15 = f'Ejercicio {counterAdd()} \n {ejercicio15[0].suma(ejercicio15[1]).simplifica()}'
print(resultado15)


ejercicio16 = [Fraccion(-12, 5), Fraccion(7, 5)]
resultado16 = f'Ejercicio {counterAdd()} \n {ejercicio16[0].suma(ejercicio16[1]).simplifica()}'
print(resultado16)


ejercicio17 = [Fraccion(-3, 16), Fraccion(-4, 16)]
resultado17 = f'Ejercicio {counterAdd()} \n {ejercicio17[0].suma(ejercicio17[1]).simplifica()}'
print(resultado17)


ejercicio18 = [Fraccion(2, 7), Fraccion(-1, 7)]
resultado18 = f'Ejercicio {counterAdd()} \n {ejercicio18[0].resta(ejercicio18[1]).simplifica()}'
print(resultado18)


ejercicio19 = [Fraccion(-12, 100), Fraccion(-8, 100)]
resultado19 = f'Ejercicio {counterAdd()} \n {ejercicio19[0].suma(ejercicio19[1]).simplifica()}'
print(resultado19)


ejercicio20 = [Fraccion(-89, -121), Fraccion(-32, 121)]
resultado20 = f'Ejercicio {counterAdd()} \n {ejercicio20[0].resta(ejercicio20[1]).simplifica()}'
print(resultado20)

''' Parte 2: distinto denominador'''
print('\n Parte 2: distinto denominador \n')

ejercicio21 = [Fraccion(7, 9), Fraccion(2, 15)]
resultado21 = f'Ejercicio {counterAdd()} \n {ejercicio21[0].suma(ejercicio21[1]).simplifica()}'
print(resultado21)


ejercicio22 = [Fraccion(5, 6), Fraccion(3, 8)]
resultado22 = f'Ejercicio {counterAdd()} \n {ejercicio22[0].resta(ejercicio22[1]).simplifica()}'
print(resultado22)


ejercicio23 = [Fraccion(3, 4), Fraccion(3, 10)]
resultado23 = f'Ejercicio {counterAdd()} \n {ejercicio23[0].suma(ejercicio23[1]).simplifica()}'
print(resultado23)


ejercicio24 = [Fraccion(3, 5), Fraccion(1, 3)]
resultado24 = f'Ejercicio {counterAdd()} \n {ejercicio24[0].resta(ejercicio24[1]).simplifica()}'
print(resultado24)


ejercicio25 = [Fraccion(6, 7), Fraccion(8, 3)]
resultado25 = f'Ejercicio {counterAdd()} \n {ejercicio25[0].suma(ejercicio25[1]).simplifica()}'
print(resultado25)


ejercicio26 = [Fraccion(31, 21), Fraccion(3, 14)]
resultado26 = f'Ejercicio {counterAdd()} \n {ejercicio26[0].resta(ejercicio26[1]).simplifica()}'
print(resultado26)


ejercicio27 = [Fraccion(3, 4), Fraccion(2, 5), Fraccion(1, 6)]
resultado27 = f'Ejercicio {counterAdd()} \n {ejercicio27[0].suma(ejercicio27[1]).simplifica().suma(ejercicio27[2]).simplifica()}'


ejercicio28 = [Fraccion(3, 5), Fraccion(3, 15), Fraccion(3, 10)]
resultado28 = f'Ejercicio {counterAdd()} \n {ejercicio28[0].suma(ejercicio28[1]).simplifica().resta(ejercicio28[2]).simplifica()}'
print(resultado28)


ejercicio29 = [Fraccion(13, 2), Fraccion(1, 4), Fraccion(5, 6)]
resultado29 = f'Ejercicio {counterAdd()} \n {ejercicio29[0].resta(ejercicio29[1]).simplifica().resta(ejercicio29[2]).simplifica()}'
print(resultado29)


ejercicio30 = [Fraccion(-2, 3), Fraccion(3, 2)]
resultado30 = f'Ejercicio {counterAdd()} \n {ejercicio30[0].suma(ejercicio30[1]).simplifica()}'
print(resultado30)


ejercicio31 = [Fraccion(-3, 12), Fraccion(1, 8)]
resultado31 = f'Ejercicio {counterAdd()} \n {ejercicio31[0].resta(ejercicio31[1]).simplifica()}'
print(resultado31)


ejercicio32 = [Fraccion(-2, 10), Fraccion(5, 100), Fraccion(1, 2)]
resultado32 = f'Ejercicio {counterAdd()} \n {ejercicio32[0].resta(ejercicio32[1]).simplifica().suma(ejercicio32[2]).simplifica()}'
print(resultado32)


ejercicio33 = [Fraccion(-2, 11), Fraccion(11, 2), Fraccion(12, 11)]
resultado33 = f'Ejercicio {counterAdd()} \n {ejercicio33[0].suma(ejercicio33[1]).simplifica().resta(ejercicio33[2]).simplifica()}'
print(resultado33)


ejercicio34 = [Fraccion(-6, 4), Fraccion(4, 6), Fraccion(1, 8)]
resultado34 = f'Ejercicio {counterAdd()} \n {ejercicio34[0].resta(ejercicio34[1]).simplifica().resta(ejercicio34[2]).simplifica()}'
print(resultado34)


ejercicio35 = [Fraccion(-3, 2), Fraccion(-2, 3)]
resultado35 = f'Ejercicio {counterAdd()} \n {ejercicio35[0].suma(ejercicio35[1]).simplifica()}'
print(resultado35)


'''Problemas para pensar: '''
print(f'\n Problemas para pensar: \n')


print('\n Ejercicio 1: \b')
ej1 = 'Hallar el numerador "a" para que la suam de fracciones sea forrecta: \b'
print(ej1)
print('(2/3) + (a/3) = (7/3)')
print(f'Respuesta:  a = {7-2}')


print('\n Ejercicio 2: \b')
ej2 = '¿La suma de dos fracciones negativas es siempre negativa?'
print(ej2)
print(f'Respuesta: NO')


print('\n Ejercicio 3: \b')
ej3 = 'Calcular la siguiente suma de uan fraccion y un numero natural: '
print(ej3)
print('(3/5) + 2')

print(f'Respuesta: {FraccionMixta(2, Fraccion(3,5)).a_impropia()}')


print('\n Ejercicio 4: \b')
ej4 = 'Hallar el numerador "a" para que lasiguiente resta de fracciones sea correcta: '
print(ej4)
print('(17/5) - (a/5) = 3/1')

print(f'Respuesta: a = {2}')


print('\n Ejercicio 5: \b')
ej5 = 'Hallar el numerador "a" para que la siguiente suma de fracciones sea correcta:  '
print(ej5)
print('(2/3) + (a/2) = 13/6')

print(f'Respuesta: a = {13-2}')
