class Part(object):
    def __init__(self, name, location, partNumber):
        self.name = name
        self.location = location
        self.partNumber = partNumber

    def __str__(self):
        return f'{self.name}, {self.location}, {self.partNumber}'

# aa = Part('lili','nv', 123)
# print(aa)