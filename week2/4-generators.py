# generators are iterable like lists and tuple however they do not store all of the values in memory, only the last one


def generate_number(start, stop):
    for i in range(start, stop):
        yield i




generate_number = lambda start, stop: (i for i in range(start, stop))

numbers = generate_number(1, 10)

for number in numbers:
    print(number)


