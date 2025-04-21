class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def agregar_nodo(cabeza, valor):
    nuevo = Nodo(valor)
    if cabeza is None:
        return nuevo #Esto quiere decir que si la no hay un nodo anterior entonce este nuevo nodo es la "cabeza".
    actual = cabeza
    while actual.siguiente:
        actual = actual.siguiente
    actual.siguiente = nuevo
    return cabeza

def mostrar_lista(cabeza):
    actual = cabeza
    lista = []
    while actual:
        lista.append(str(actual.valor))
        actual = actual.siguiente
    return " -> ".join(lista) if lista else "Lista vacía"

def intercambiar_pares(cabeza):
    intercambiado = Nodo(0)
    intercambiado.siguiente = cabeza #lo conecta al nodo cabeza
    actual = intercambiado

    while actual.siguiente and actual.siguiente.siguiente:
        primero = actual.siguiente # este sería el primer numero porque el "actual" es el 0 que acaba de crearse 
        segundo = primero.siguiente

        primero.siguiente = segundo.siguiente #Esto signfica que la flecha que señala al siguiente por parte del primer nodo señalaria al tercer nodo
        segundo.siguiente = primero # y aca el segundo nodo señalaria al primero 
        actual.siguiente = segundo #el actual era el 0 entonces el siguiente sería el primero pero pasaria a ser el segundo nodo
        actual = primero # actual ahora es 1(segunda posición) para que pueda intercambiar los siguientes pares

    return intercambiado.siguiente # saltearíamos el 0 entonces nos quedaría intercambiados

# aca va el menu 
cabeza = None

while True:
    menu = input("\n1. Ingresar números\n2. Mostrar lista original\n3. Mostrar original e intercambiar de a pares\n4. Salir\nElija una opción: ")

    if menu == '1':
        while True:
            try:
                num = int(input("Ingrese un número: "))
                cabeza = agregar_nodo(cabeza, num)
                continuar = input("¿Desea agregar otro número? (s/n): ")
                if continuar.lower() != 's':
                    break
            except ValueError:
                print("Eso no es un número válido.")

    elif menu == '2':
        print("Lista original:")
        print(mostrar_lista(cabeza))

    elif menu == '3':
        print("Lista original:")
        print(mostrar_lista(cabeza))

        cabeza = intercambiar_pares(cabeza)

        print("Lista después de intercambiar nodos de a pares:")
        print(mostrar_lista(cabeza))

    elif menu == '4':
        print("Saliendo.")
        break

    else:
        print("Por favor elegí entre 1 y 4")
