class Set:
    def __init__(self):
        self.elements = []

    def add(self, value):
        if value not in self.elements:
            self.elements.append(value)

    def remove(self, value):
        if value in self.elements:
            self.elements.remove(value)
        else:
            raise KeyError(f"{value} not found in set")

    def contains(self, value):
        return value in self.elements

    def __iter__(self):
        return iter(self.elements)

    def __len__(self):
        return len(self.elements)