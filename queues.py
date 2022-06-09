class Node:
    def __init__(self, date):
        self.date = date
        self.next = None

class Queues:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def add(self, date):
        node = Node(date)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            auxiliar = self.front
            while auxiliar.next is not None:
                auxiliar = auxiliar.next

            auxiliar.next = node
            self.rear = node

        self.size += 1

    def __str__(self):
        representation = ''
        for item in self.__iter__():
            representation += item + '-'

        return representation

    def __add__(self, other):
        new = Queues()
        for item in self.__iter__():
            new.add(item)

        for item in other:
            new.add(item)

        return new

    def __iter__(self):
        auxiliar = self.front
        while auxiliar is not None:
            yield auxiliar.date
            auxiliar = auxiliar.next

    def __contains__(self, item):
        return item in self.__iter__()

    def __len__(self):
        return self.size

    def clear(self):
        while self.front:
            self.pop()

    def peek(self):
        if self.front:
            return self.front.date
        else:
            print('Is empty')

    def pop(self):
        if self.front:
            item = self.front.date
            self.size -= 1

            if self.front.next:
                self.front = self.front.next
            else:
                self.front = None

            return item
        else:
            print('Is empty')

if __name__ == '__main__':
    queues = Queues()
    queues2 = Queues()

    queues.add('Miguel')
    queues.add('Juan')
    queues.add('Amparo')

    queues2.add('Jose')
    queues2.add('Jorge')
    queues2.add('Marcela')

    ultimate = queues + queues2

    print('contiene:', len(ultimate))

    print(ultimate)





