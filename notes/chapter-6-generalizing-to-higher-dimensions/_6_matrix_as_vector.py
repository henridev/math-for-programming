from abc import ABCMeta, abstractmethod, abstractclassmethod, abstractproperty


class Vector(metaclass=ABCMeta):
    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def add(self, other):
        pass

    @abstractclassmethod
    @abstractproperty
    def zero_vector(self):
        pass

    def negation_vector(self):
        return self.scale(-1)

    def subtract(self, other):
        return self.add(other.scale(-1))

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

class Matrix5_by_3(Vector):
    # 1 You need to know the number of rows and columns to be able to construct the zero matrix
    rows = 5
    columns = 3

    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        return Matrix5_by_3(tuple(
            tuple(a + b for a, b in zip(row1, row2))
            for (row1, row2) in zip(self.matrix, other.matrix)
        ))

    def scale(self, scalar):
        return Matrix5_by_3(
            tuple(
                tuple(scalar * x for x in row)
                for row in self.matrix
            )
        )

    def zero(cls):
        # 2  The zero vector for 5×3 matrices is a 5×3 matrix consisting of all zeroes. Adding this to any other 5×3 matrix M returns M.
        return Matrix5_by_3(
            tuple(
                tuple(0 for j in range(0, cls.columns))
                for i in range(0, cls.rows)
            )
        )


class Matrix(Vector):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def add(self, other):
        return Matrix(tuple(
            tuple(a + b for a, b in zip(row1, row2))
            for (row1, row2) in zip(self.matrix, other.matrix)
        ))

    def scale(self, scalar):
        return Matrix(
            tuple(
                tuple(scalar * x for x in row)
                for row in self.matrix
            )
        )

    def zero(self):
        return Matrix(
            tuple(
                tuple(0 for j in range(0, self.columns))
                for i in range(0, self.rows)
            )
        )
