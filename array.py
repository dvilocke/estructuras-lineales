import random
class Array:
    def __init__(self, capacity, fill_value = None):
        self.items = []
        for i in range(capacity):
            self.items.append(fill_value)


    def __len__(self):
        """
        Este metodo que viene desde python, nos permite obtener el tamaño de algo, en este caso como nosotros
        estamos creando un array, simplemente devolvemos su tamañan
        x = Array(10)
        print(len(x)) // 10
        """
        return len(self.items)

    def __str__(self):
        """
        Este metodo que viene desde python, nos permite hacer una representación del objeto, en este caso lo que
        nosotros queremos representar
        x = Array(10)
        print(x) // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
        return str(self.items)

    def __iter__(self):
        """
        Este metodo que viene desde python, nos permite devolver un iterador, lo que significa que yo puedo hacer esto
        x = Array(10)
        for i in x:
            print(i)
        """
        return iter(self.items)

    def __getitem__(self, item):
        """
        Este metodo que viene desde python, lo que quiere decir esto __x__ es que le da algunos comportamientos
        extras que nos pueden facilitar a nosotros muchos aspectos, por ejemplo este metodo __getitem__ nos permite
        obtener un item, como duplicar el comportamiento de las listas
        """
        return self.items[item]

    def __setitem__(self, key, value):
        """
        Este metodo que viene desde python, lo que quiere decir, nos permite hacer un comportamiento como las listas,
        en este caso nos permite cambiar un item
        """
        self.items[key] = value

    def poblar(self):
        for i in range(self.__len__()):
            self.__setitem__(i, random.randint(0, 100))

    def sumar(self):
        return sum(self.items)


x = Array(10)
x.poblar()
print(x)
print(x.sumar())




