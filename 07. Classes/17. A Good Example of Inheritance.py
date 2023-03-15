"""
7. Classes, 17. A Good Example of Inheritance

A good example of inheritance, would be modeling how to read a stream of data
A stream of data can come from multiple sources, a file, network, memory etc.
They all have features in commom like opening or closing the stream. 
But how we read data from then chages from one to another.

The below example only has two levels of inheritance. 
"""


class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")
