#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterate):
        self.iterator = iter(iterate)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        self.count += 1
        try:
            return next(self.iterator)
        except StopIteration:
            raise StopIteration
