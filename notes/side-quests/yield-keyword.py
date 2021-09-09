mygenerator = (x*x for x in range(3))
mylist = [x*x for x in range(3)]

for i in mygenerator:
    print('generator type iterator first => ', i)
    print('i will forget this immediatly => ', i)

for i in mygenerator:
    print('generator type iterator second => ', i)
    print('i will forget this immediatly => ', i)


for i in mylist:
    print('multiple iteration iterable in memory stored first => ', i)
    print('i will store this in memory => ', i)


for i in mylist:
    print('multiple iteration iterable in memory stored second => ', i)
    print('i will store this in memory => ', i)


def create_multiplier_generator(factor=2):
    mylist = range(3)
    for i in mylist:
        yield i*factor


multiplier_by_3_generator = create_multiplier_generator(3)
print(multiplier_by_3_generator)

for i in multiplier_by_3_generator:
    print('generator type iterator first => ', i)
    print('--- i will forget this immediatly ---')


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def testyield():
    yield "Welcome to Guru99 Python Tutorials"


gen = testyield()
gen2 = testyield()
print(next(gen))
print(gen.__class__ == gen2.__class__)


def generator():
    yield "H"
    yield "E"
    yield "L"
    yield "L"
    yield "O"


test = generator()
for i in test:
    print(i)


def function_uninterupted():
    return "H"
    return "E"
def generator_interupted():
    yield "H"
    yield "interrupt"
    yield "E"


test_gen = generator_interupted()
test_func = function_uninterupted()

print(next(test_gen), next(test_gen))
print(test_func)


def even_numbers(n):
    for x in range(n):
        if (x % 2 == 0):
            yield x


num = even_numbers(10)
print(list(num))


def getFibonnaciSeries(num):
    c1, c2 = 0, 1
    count = 0
    while count < num:
        yield c1
        c3 = c1 + c2
        c1 = c2
        c2 = c3
        count += 1


fin = getFibonnaciSeries(7)
print(fin)
for i in fin:
    print(i)
