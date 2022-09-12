from Coches import Coche
from Bicicletas import Bicicleta
from Motocicletas import Motocicleta
from Camionetas import Camioneta


def catalogar(lista, ruedas = False):

    if ruedas:

        s = 0

        for i in lista:

            if i.obtenerRuedas() == ruedas:
                s +=1

        print("Hay {} vehiculos con {} ruedas".format(s,ruedas))
    else:
        print(*lista, sep = "\n")



if __name__ == '__main__':
    
    tacoma = Camioneta('Negro', 4, 260, 8, 8654)
    yamaha = Motocicleta('Rosado', 3, 'Deportiva', 125, 20)
    corsa = Coche('Rojo', 4, 450, 25)
    giant = Bicicleta('Blanco', 2, 'Urbana')
    

    vehiculos = [tacoma,yamaha,corsa,giant]

    # Creamos un pequeno menu
    print('''Que deseas haces?\n
    [1] - Listar Nuestros Vehiculos\n
    [2] - Buscar segun el numero de ruedas\n
    [3] - Salir
    \n''')

    opcion = int(input("Eliga un numero: "))
    
    if opcion == 1:
        catalogar(vehiculos)
    elif opcion == 2:
        n = int(input("Eliga el numero de ruedas: "))
        catalogar(vehiculos,n)
    else:
        print("Adios")
    
    
    



