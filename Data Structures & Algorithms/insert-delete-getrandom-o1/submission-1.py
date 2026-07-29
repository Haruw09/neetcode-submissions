class RandomizedSet:

    def __init__(self):
        self.elements: list[int] = []
        self.indexes: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val not in self.indexes:
            self.indexes[val] = len(self.elements)
            self.elements.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indexes:
            last_elem = self.elements[-1]
            val_idx = self.indexes[val]

            self.elements[val_idx] = last_elem
            self.indexes[last_elem] = val_idx

            last_elem = self.elements.pop()
            del self.indexes[val]
            
            return True
        return False

    def getRandom(self) -> int:
        elem = random.choice(self.elements)
        return elem


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()