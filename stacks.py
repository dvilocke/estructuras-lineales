class Node:
    def __init__(self, date):
        self.date = date
        self.next = None

class Stack:

    top = None
    counter = 0

    def __init__(self):
        pass

    def push(self, date):
        node = Node(date)

        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

        self.counter += 1

    def __len__(self):
        return self.counter


    def __add__(self, other):
        new_stack = Stack()
        list_1 = [item for item in self.__iter__()]
        list_2 = [item for item in other]

        for item in list_1[::-1]:
            new_stack.push(date=item)

        for item in list_2[::-1]:
            new_stack.push(date=item)

        return new_stack

    def __iter__(self):
        auxiliar = self.top
        while auxiliar is not None:
            yield auxiliar.date
            auxiliar = auxiliar.next

    def __contains__(self, item):
        for _ in self.__iter__():
            if _ == item:
                return True
        return False

    def clear(self):
        while self.top:
            self.pop()

    def is_empty(self):
        return True if self.top is None else False

    def peek(self):
        return self.top.date if self.top else 'The stack is empty'

    def pop(self):
        if self.top:
            data = self.top.date
            self.counter -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            return 'The stack is empty'


if __name__ == '__main__':
    stack1 = Stack()

    stack1.push('a')
    stack1.push('b')
    stack1.push('c')

    stack2 = Stack()

    stack2.push('d')
    stack2.push('e')
    stack2.push('f')

    stack3 = Stack()

    stack2.push('g')
    stack2.push('h')
    stack2.push('i')


    newStack = stack1 + stack2

    newStack += stack3

    for el in newStack:
        print(el)