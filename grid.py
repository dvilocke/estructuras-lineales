from repasoArray import *

class Grid:
    def __init__(self, rows, columns, values = None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, item):
        return self.data[item]


    def populete_date(self):
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                self.data[row][column] = random.randint(0, 100)

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                result += str(self.data[row][column]) + ' '
            result += '\n'

        return result


if __name__ == '__main__':
    x = Grid(3, 2)
    x.populete_date()

    print(x)

