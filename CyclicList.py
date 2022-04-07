from itertools import cycle
from itertools import islice


class CyclicList:

    """Infinite loop list"""

    def __init__(self, iterable):
        self.safe_list = iterable
        self.the_list = cycle(iterable)

    def __iter__(self):
        for i, item in enumerate(self.the_list):
            if item != self.safe_list[0]:
                self.the_list[i+1:]
            else:
                break
        return iter(self.the_list)

    def __next__(self):
        for item in self.the_list:
            if item.is_available:  # or however you spell it
                return item


my_list = CyclicList([1, 2, 3])
for i, n in enumerate(my_list):
    print(n)
    if i > 8:
        break
print(list(islice(my_list, 5)))