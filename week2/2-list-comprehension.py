# map(function, iterable)
# list function is used to convert an iterator into a list

squares = list(map(lambda x: x**2, range(10)))

# or in list comprehension

squares = [x**2 for x in range(10)]


