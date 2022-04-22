from itertools import cycle, islice
from collections import UserList

''' 
# My Incomplete Solution - To Do Again

class CyclicList2:

    """Infinite Loop List"""

    def __init__(self, iterable):
        self.iterable = cycle(iterable)

    def __iter__(self):
        yield iter(self.iterable)

    def __next__(self):
        for item in self.iterable:
            return item
'''


# Trey's Solution
class CyclicList(UserList):

    """List-like data structure that loops in a cyclic manner."""

    def _slice_indices(self, obj):
        start, stop = obj.start, obj.stop
        if obj.step is not None:
            raise ValueError("Step not supported")
        if start is None:
            start = 0
        if stop is None:
            stop = len(self) if start >= 0 else 0
        return start, stop, 1

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [
                self[i]
                for i in range(*self._slice_indices(index))
            ]
        return self.data[index % len(self)]

    def __setitem__(self, index, value):
        self.data[index % len(self)] = value


# Base Problem
my_list = CyclicList([1, 2, 3])
for i, n in enumerate(my_list):
    print(n)
    if i > 8:
        break
print(list(islice(my_list, 5)))

# Bonus 1
my_list = CyclicList([1, 2, 3])
my_list.append(4)
my_list.pop()
print(len(my_list))
my_list.pop(0)
print(len(my_list))

# Bonus 2

