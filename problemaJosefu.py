import time
import random
from node import Nodo

class CircularList:

    head = None
    end = None
    where_to_statr =  2
    number_of_players = 0

    def __init__(self):
        pass

    def add(self, data):
        nodo = Nodo(data)
        if self.head is None:
            self.end = nodo
            self.head = nodo
            nodo.siguiente = self.head
        else:

            self.end.siguiente = nodo
            self.end = nodo

            nodo.siguiente = self.head

        self.number_of_players += 1

    def generate_random_number(self):
        self.where_to_statr = random.randint(1, 100)

    def play(self):
        counter = 0
        auxiliar = self.head

        print('Numero Aleatorio Generado', self.where_to_statr)

        while True:
            if self.number_of_players == 1:
                break
            else:
                if counter == self.where_to_statr:
                    print('Eliminado el nodo:', auxiliar.dato)
                    time.sleep(4)
                    if auxiliar is self.head:
                        self.head = auxiliar.siguiente
                        previous_node.siguiente = self.head

                    elif auxiliar is self.end:
                        self.end = previous_node
                        self.end.siguiente = auxiliar.siguiente

                    else:
                        previous_node.siguiente = auxiliar.siguiente


                    counter = 0
                    self.number_of_players -= 1

                previous_node = auxiliar
                auxiliar  = auxiliar.siguiente
                counter += 1

        print('El Nodo Superviviente:', self.head.dato)

if __name__ == '__main__':
    x = CircularList()
    x.add(10)
    x.add(20)
    x.add(30)
    x.add(40)
    x.add(50)
    x.add(60)
    x.add(70)
    x.add(80)
    x.add(90)
    x.add(100)
    x.add(200)
    x.add(300)
    x.add(400)

    x.generate_random_number()

    x.play()



