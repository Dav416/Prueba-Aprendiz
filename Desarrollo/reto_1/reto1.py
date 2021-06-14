vector1 = []
vector2 = []


N = int(input('Indique cuantos elementos desea leer (el numero maximo de elementos a leer es de 15)\n'))
if (N > 0 and N <= 15):
    for i in range(0,N): 
        vector = int(input('\nIngrese los elementos del primer vector, deben ser numeros positivos entre 1 y 30\n')) 
        if (vector > 0 and vector <= 30):
            vector1.append(vector) 
            print(f'El valor agregado fue: {vector}') 
        else:
            print('\nIngresaste un valor no valido')
            break      
else:
    print('\nHas ingresado un valor no valido')
    vector = 0
    
#Vector2
if(vector > 0 and vector < 31):   
    for i in range(0,N): 
        vector = int(input('\nIngrese los elementos del segundo vector, deben ser numeros positivos entre 1 y 30\n')) 
        if (vector > 0 and vector <= 30):
            vector2.append(vector) 
            print(f'El valor agregado fue: {vector}') 
        else:
            print('\nIngresaste un valor no valido')
            break
if (N <= 0 or N > 15) or (vector <= 0 or vector > 30):
    print("\nNo es posible realizar una accion")
else:
    vector1.sort()
    vector2.sort() 
    print(f'\nLos elementos del vector 1 son: {vector1} y los elementos del vector dos son: {vector2}')

    for i in range(0,N):
        sumvec = vector1[i] + vector2[i]
        print(f'La suma de los vectores en la posicion {i+1} es: {sumvec}')  