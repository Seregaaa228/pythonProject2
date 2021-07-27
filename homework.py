class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def calculate(self):
        return self.length * self.width


rectangle = Rectangle()
print(rectangle.calculate())