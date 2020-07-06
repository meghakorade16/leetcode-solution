class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomized_set = {}
        self.rand_set = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.randomized_set:
            return False
        else:
            self.randomized_set[val] = len(self.rand_set)
            self.rand_set.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.randomized_set:
            return False
        else:
            pos = self.randomized_set[val]
            last_val = self.rand_set[-1]
            self.rand_set[pos] = last_val
            self.randomized_set[last_val] = pos
            self.randomized_set.pop(val)
            self.rand_set.pop()
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.rand_set)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()