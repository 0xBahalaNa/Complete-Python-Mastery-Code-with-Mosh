"""
7. Classes, 21. Extending Built-in Types

Inheritance of built-in class types.
String and list class seen below. 
Can modify methods from built-in class types. 
"""


class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called.")
        super().append(object)


list = TrackableList()
list.append(1)
