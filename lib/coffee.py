#!/usr/bin/env python3

class Coffee:
    sizes = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        self._size = None
        self.price = price
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value not in self.sizes:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value


    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1