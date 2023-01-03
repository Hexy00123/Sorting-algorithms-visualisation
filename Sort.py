class Sort:
    def __init__(self, array):
        self.array = array

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        return iter(self.array)

    def __repr__(self):
        return str(self.array)