from node import Nodo

class ListaEnlazada:

    cabeza = None

    def __init__(self):
        pass

    def agregar(self, dato):
        #debo preguntarme si es el primer nodo
        if self.cabeza is None:
            self.cabeza = Nodo(dato)
        else:
            #Debo encontrar quien va apuntar al nuevo nodo
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = Nodo(dato)

    def agregarInicio(self, dato):
        if self.cabeza is not None:
            auxiliar = self.cabeza
            self.cabeza = Nodo(dato)
            self.cabeza.siguiente = auxiliar


    def obtenerDatos(self):
        if self.cabeza is not None:
            auxiliar = self.cabeza

            while auxiliar.siguiente is not None:
                yield auxiliar.dato
                auxiliar = auxiliar.siguiente


    def eliminarPrimero(self):
        if self.cabeza is not None:
            if self.totalDatos() == 1:
                #singifica que solo tenemos un nodo
                self.cabeza = None
                pass
            else:
                #significa que tenemos mas nodos
                self.cabeza = self.cabeza.siguiente

    def eliminarUltimo(self):
        if self.cabeza is not None:
            if self.totalDatos() == 1:
                self.cabeza = None
            else:
                counter = 1
                auxiliar = self.cabeza
                while counter  != self.totalDatos()  - 1:
                    auxiliar = auxiliar.siguiente
                    counter += 1

                auxiliar.siguiente = None

    def totalDatos(self):
        counter = 0
        if self.cabeza is not None:
            auxiliar = self.cabeza
            while auxiliar is not None:
                counter += 1
                auxiliar = auxiliar.siguiente

        return counter


    def eliminarDato(self, dato):
        if self.cabeza is not None:
            seEncuentra = False
            auxiliar = self.cabeza
            izquierda = None
            while auxiliar is not None:
                if auxiliar.dato == dato:
                    derecha = auxiliar.siguiente
                    seEncuentra = True
                    break
                izquierda = auxiliar
                auxiliar = auxiliar.siguiente

            if seEncuentra:
                izquierda.siguiente = derecha
            else:
                print('El Dato no existe')

    def mostrar(self):
        if self.cabeza is not None:
            auxiliar = self.cabeza
            while auxiliar is not None:
                print(auxiliar.dato, end='-')
                auxiliar = auxiliar.siguiente

if __name__ == '__main__':
    n = ListaEnlazada()
    n.agregar(10)
    n.agregar(20)
    n.agregar(30)
    n.agregar(20)
    n.agregar(34)
    n.agregar(80)

    datos = n.obtenerDatos()

    for _ in datos:
        print(_)

