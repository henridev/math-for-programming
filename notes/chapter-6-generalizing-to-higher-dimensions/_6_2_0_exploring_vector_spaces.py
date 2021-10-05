from datetime import datetime
from _6_1_generalizing_vectors import Vector
from pathlib import Path
from json import loads, dumps
import pprint

pp = pprint.PrettyPrinter(indent=2)

class Vec1(Vector):
    def __init__(self, x):
        self.x = x

    def add(self, other):
        return Vec1(self.x + other.x)

    def scale(self, scalar):
        return Vec1(scalar * self.x)

    @classmethod
    def zero(cls):
        return Vec1(0)

    def __eq__(self, other):
        return self.x == other.x

    def __repr__(self):
        return "Vec1({})".format(self.x)


class Vec0(Vector):
    def __init__(self):
        pass

    def add(self, other):
        return Vec0()

    def scale(self, scalar):
        return Vec0()

    @classmethod
    def zero(cls):
        return Vec0()

    def __eq__(self, other):
        return self.__class__ == other.__class__ == Vec0

    def __repr__(self):
        return "Vec0()"


class CarForSale(Vector):
    retrieved_date = datetime(2018, 11, 30, 12)  # 1 I retrieved the data set from CarGraph.com on 11/30/2018 at noon.

    def __init__(
            self, model_year, mileage, price, posted_datetime,
            model="(virtual)",  # To simplify construction of virtual cars, all of the string parameters are optional with a default value “(virtual)”.
            source="(virtual)",
            location="(virtual)",
            description="(virtual)"
    ):
        self.model_year = model_year
        self.mileage = mileage
        self.price = price
        self.posted_datetime = posted_datetime
        self.model = model
        self.source = source
        self.location = location
        self.description = description

    def add(self, other):
        # 3 Helper function that adds dates by adding the time spans from the reference date
        def add_dates(d1, d2):
            age1 = CarForSale.retrieved_date - d1
            age2 = CarForSale.retrieved_date - d2
            sum_age = age1 + age2
            return CarForSale.retrieved_date - sum_age
        return CarForSale(
            self.model_year + other.model_year,
            self.mileage + other.mileage,
            self.price + other.price,
            add_dates(self.posted_datetime, other.posted_datetime)
        )

    def scale(self, scalar):
        # 5 Helper function that scales a datetime by scaling the time span from the reference date
        def scale_date(d):
            age = CarForSale.retrieved_date - d
            return CarForSale.retrieved_date - (scalar * age)
        return CarForSale(
            scalar * self.model_year,
            scalar * self.mileage,
            scalar * self.price,
            scale_date(self.posted_datetime)
        )

    @classmethod
    def zero(cls):
        return CarForSale(0, 0, 0, CarForSale.retrieved_date)


# load cargraph data from json file
contents = Path('notes/chapter-6-generalizing-to-higher-dimensions/cargraph.json').read_text()
cg = loads(contents)
cleaned = []

def parse_date(s):
    input_format = "%m/%d - %H:%M"
    return datetime.strptime(s, input_format).replace(year=2018)

    return dt


for car in cg[1:]:
    try:
        row = CarForSale(int(car[1]), float(car[3]), float(car[4]), parse_date(car[6]), car[2], car[5], car[7], car[8])
        cleaned.append(row)
    except:
        pass

cars = cleaned
average_prius = sum(cars, CarForSale.zero()) * (1.0/len(cars))

pp.pprint((cars[0] + cars[1]).__dict__)

pp.pprint(average_prius.__dict__)


class Function(Vector):
    def __init__(self, f):
        self.f = f

    def add(self, other):
        def new_function(x):
            return self.f(x) + other.f(x)
        return Function(new_function)

    def scale(self, scalar):
        def new_function(x):
            return self.f(x) * scalar
        return Function(new_function)

    @classmethod
    def zero(cls):
        return Function(lambda x: 0)

    def __call__(self, x):
        return self.f(x)


'''
f = 3 * Function(lambda x: x * 3)
print(f(2))
g = Function(lambda x: x / 2)
combo = 2 * f - 6 * g
print(combo(2))
(f + g)(6)
'''


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

    @classmethod
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

    @classmethod
    def zero(self):
        return Matrix(
            tuple(
                tuple(0 for j in range(0, self.columns))
                for i in range(0, self.rows)
            )
        )
