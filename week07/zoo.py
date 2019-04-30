class Zoo:
    def __init__(self):
        self.index
        self.animals = []

    def add_animal(self, animal_name):
        self.animals.append(animal_name)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        index = self.index
        self.index += 1
        try:
            return self.animals[index]
        except IndexError:
            raise StopIteration


