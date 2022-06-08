import time

class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.atras = None

class Circulo:

    cabeza = None
    cola = None

    def __init__(self):
        pass

    def agregar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza is None:

            #hacemos la conexion con la cabeza
            self.cabeza = nodo
            nodo.atras = nodo
            nodo.siguiente = nodo

            #hacemos la conexion con la cola
            self.cola = nodo


        else:
            #significa que debemos hacer la conexion siempre con la cola

            auxiliar = self.cola

            self.cola = nodo

            auxiliar.siguiente = nodo
            nodo.atras = auxiliar

            nodo.siguiente = self.cabeza
            self.cabeza.atras = nodo


    def recorrerSiguiente(self):
        auxiliar = self.cabeza

        while  auxiliar is not None:
            print(auxiliar.data)
            time.sleep(3)
            auxiliar = auxiliar.siguiente

    def recorrerAtras(self):
        auxiliar = self.cola

        while auxiliar is not None:
            print(auxiliar.data)
            time.sleep(3)
            auxiliar = auxiliar.atras


if __name__ == '__main__':
    x = Circulo()

    x.agregar(dato=10)
    x.agregar(dato=20)
    x.agregar(dato=30)
    x.agregar(dato=40)

    x.recorrerAtras()




