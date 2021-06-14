"Las siete vacas flacas"
# 7 filas, N columnas
#el ciclo de afuera son las filas y el de adentro las columnas que son las que mas se mueven

matriz = []

while (True):
    N = int(input('Ingrese numero de vacas (minimo 3, maximo 50)\n'))
    if (N >= 3 and N <= 50):
        for i in range(0,7): # filas dias semana
            matriz.append([f'dia {i+1}'])
            acum = 0
            print(f'dia {i+1}')
            for j in range(0,N): # columnas numero vacas
                while (True):
                    litro = float(input(f'Ingrese cantidad de litros (debe ser un valor de 0 a 11) producidos por la vaca numero: {j+1}\n'))
                    if (litro >= 0 and litro <= 11.9):
                        matriz[i].append(litro)
                        acum = acum + litro
                        break
                    else:
                        print('Ingrese un valor valido')
            matriz[i].append(acum)
            print(f'La produccion total del dia {i+1} es de {acum} litros\n')
        break
    else:
        print('Introduzca un valor entre 3 y 50')
print(matriz)

alto = matriz[0][4]
menor = matriz[0][4]
dia = matriz[0][0]
for i in range(0,7):
    if matriz[i][4] > alto:
        alto = matriz[i][4]
        dia = matriz[i][0]
print(f'El dia con mayor produccion de litros fue el {dia} y la cantidad de litros producida fue {alto}')

for i in range(0,7):
    if (matriz[i][4] < menor):
        menor = matriz[i][4]
        dia = matriz[i][0]
print(f'El dia con menor produccion de litros fue el {dia} y la cantidad de litros producida fue {menor}')












