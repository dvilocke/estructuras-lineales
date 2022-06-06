class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    head = None
    final = None

    def __init__(self):
        pass

    def add(self, data):
        node = Nodo(data)
        if self.head is None:
            #Significa que es el primero
            self.head = node
        else:
            #Significa que existen muchos mas nodos, debo encontrar donde conectarme
            auxiliar = self.head
            while auxiliar.next is not None:
                auxiliar = auxiliar.next

            #Hacemos la conexion
            auxiliar.next = node
            node.prev = auxiliar

            self.final = node

    def walk_ahead(self):
        auxiliar = self.head

        while auxiliar is not None:
            yield auxiliar.data
            auxiliar = auxiliar.next

    def go_backwards(self):
        auxiliar = self.final
        while auxiliar is not None:
            yield  auxiliar.data
            auxiliar = auxiliar.prev

    def check_existence(self, data):
        indice = 0
        for i in self.walk_ahead():
            if i == data:
                return indice, True
            indice += 1

        return indice, False

    def delete(self, data):
        if self.head is not None:
            indice, result = self.check_existence(data)
            if result:
                auxiliar = self.head
                counter = 0
                while counter != indice:
                    auxiliar = auxiliar.next
                    counter += 1

                #Hacemos el proceso de desconexion
                previous = auxiliar.prev
                previous.next = auxiliar.next

                next_node = auxiliar.next
                next_node.prev = previous

            else:
                print(f'El {data} no se encuentra')

if __name__ == '__main__':
    x = DoublyLinkedList()

    x.add(10)
    x.add(20)
    x.add(30)
    x.add(40)
    x.add(50)

    #Recorrer hacia adelante

    x.delete(40)

    for z in x.go_backwards():
        print(z)





