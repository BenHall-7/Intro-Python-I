from math import floor, sqrt
import sys

class PrimeHelperIterator():
    under = True
    value = 6
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.under:
            ret = self.value - 1
            self.under = False
        else:
            ret = self.value + 1
            self.under = True
            self.value += 6
        if ret > self.limit:
            raise StopIteration
        return ret

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    
    limit = floor(sqrt(x))
    for factor in PrimeHelperIterator(limit):
        if x % factor == 0:
            return False
    
    return True

input = int(sys.argv[1]) if len(sys.argv) > 1 else exit("Needs input number")

print(is_prime(input))