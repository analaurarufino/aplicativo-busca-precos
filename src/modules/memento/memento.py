class Memento:
    def __init__(self, item, id):
        self.item = item
        self.id = id

    def restore(self):
        return self.id, self.item

