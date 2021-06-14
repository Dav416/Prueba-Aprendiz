class Productomodel:
    def __init__(self,codigo,nombre,precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    def mostrarinfo(self):
        print(f'Codigo del producto: {self.codigo}, nombre del producto: {self.nombre}, precio del producto: {self.precio}')

class Clientemodel():
    def __init__(self,nit,nombre,telefono,direccion,email):
        self.nit = nit
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email
    
    def mostrarinfo(self):
        print(f'El numero de nit es: {self.nit}, su nombre es: {self.nombre}, su telefono es: {self.telefono}, su direccion es: {self.direccion}, su email es: {self.email}')

cont = 1
mayor550 = 0
ma200_me550 = 0
totalventas = 0
mayorventa = 0
lista = []

ventas = int(input('ingrese la cantidad de ventas generadas en el mes\n'))
while cont <= ventas:
    pagado = int(input(f'ingrese valor de la venta {cont}\n'))
    if (pagado > 550000):
        print(f'La venta número {cont} es mayor a 550000')
        mayor550 += 1 
    elif (pagado > 200000 and pagado <= 550000 ):
        print(f'La venta {cont} es mayor a 200.000 y menor o igual a 550.000')
        ma200_me550 += 1
    else:
        print(f'La venta {cont} fue menor a 200.000')
    lista.append(pagado) 
    cont += 1
    totalventas = totalventas + pagado
    lista.sort()
for i in range(len(lista)):
    if (lista[i] > mayorventa):
        mayorventa = lista[i]
print(f'\nLa mayor compra fue de {mayorventa}')
for i in range(len(lista)):
    menorventa = lista[0]
    if (lista[i] < menorventa):
        menorventa = lista[i]
print(f'La menor compra fue de {menorventa}')
prommayor550 = (mayor550/ventas)
prom200_550 = (ma200_me550/ventas)
print(f'\nEl total de las ventas mayores a 550.000 es de {mayor550} y el promedio de ventas fue de {prommayor550}')
print(f'\nEl total de las ventas mayores a 200.000 y menores o iguales a 550.000 es de {ma200_me550} y el promedio de ventas fue de {prom200_550}')
print(f'\nLa cantidad de ventas en el mes fue de {ventas} y el total de las ventas fue de {totalventas}')




# p = Productomodel(111,'lavadora',800000)
# p.mostrarinfo()

# cliente = Clientemodel(2343452,'luis alberto',3232224545,'cra 4 #32b- 52','luis_al@gmail.com')
# cliente.mostrarinfo()