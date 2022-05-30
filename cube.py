from repasoArray import *

class Cube:
    def __init__(self, x: int , y: int , z:int):
        self.items = Array(x)
        self.z = z
        for _ in range(y):
            self.items[_] = Array(y)

        for row in range(x):
            for column in range(y):
                self.items[row][column] = Array(z)

    def populete_date(self):
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                for _ in range(self.z):
                    self.items[row][column][_] = random.randint(0, 100)

    def __getitem__(self, item):
        self.items[item]

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                    result += str(self.items[row][column]) + " "

            result += "\n"

        return result

    def get_height(self):
        return len(self.items)

    def get_width(self):
        return len(self.items[0])


if __name__ == '__main__':
    x = Cube(2, 2, 2)
    x.populete_date()
    print(x.items)
    print(x.items[0][0][0])