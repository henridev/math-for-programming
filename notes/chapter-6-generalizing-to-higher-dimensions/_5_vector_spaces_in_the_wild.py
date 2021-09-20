from pathlib import Path
from json import loads, dumps
from datetime import datetime
from abc import ABCMeta, abstractmethod, abstractclassmethod, abstractproperty
import pprint

pp = pprint.PrettyPrinter(indent=2)

class Vector(metaclass=ABCMeta):
    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def add(self, other):
        pass

    @abstractclassmethod
    @abstractproperty
    def zero(self):
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

    def zero():
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


class Function(Vector):
    def __init__(
            self, f
    ):
        self.f = f

    def add(self, other):
        def new_function(x):
            return self.f(x) + other.f(x)
        return Function(new_function)

    def scale(self, scalar):
        def new_function(x):
            return self.f(x) * scalar
        return Function(new_function)

    def zero():
        return Function(lambda x: 0)

    def __call__(self, x):
        return self.f(x)


new_function = 3 * Function(lambda x: x * 3)

print(new_function(2))

new_function = 2 * Function(lambda x: x * 3) - 6 * Function(lambda x: x / 2)

print(new_function(2))
