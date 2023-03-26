
class Number:
    def __init__(self, start, stop):
        self.current = start
        self.end = stop
    
    def __iter__(self):
        # defines an iterator for a class
        # means you can for loop a class
        # the thing that it returns is the iterable
        # the iterable implements __next__() function which is itself in this case
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        
        self.current += 1

        return self.current
    

numbers = Number(1, 10)

for number in numbers:
    print(number)
        