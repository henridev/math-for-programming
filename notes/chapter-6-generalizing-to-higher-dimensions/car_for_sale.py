from datetime import datetime
from vector import Vector
from math import isclose

def approx_equal_time(t1, t2):
    test = datetime.now()
    return isclose((test-t1).total_seconds(), (test-t2).total_seconds())

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

    def __eq__(self, c2):
        return (
            isclose(self.model_year, c2.model_year) and
            isclose(self.mileage, c2.mileage) and
            isclose(self.price, c2.price) and
            approx_equal_time(self.posted_datetime, c2.posted_datetime)
        )

    def __repr__(self):
        return "Car({},{},{},{})".format(self.model_year, self.mileage, self.price, self.posted_datetime)
