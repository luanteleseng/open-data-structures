# Imports
from ods import SkiplistList

# Code
def absorb(self, l2):
    tam = len(self)
    index = tam
    i = 0

    while i < tam:
        self.add(index, l2.get(i))
        index += 1
        i += 1
    i = 0

    while i < tam:
        l2.remove(0)
        i += 1

    print(self, l2)


def main():
    l1 = SkiplistList(['x', 'y', 'z'])
    l2 = SkiplistList(['a', 'b', 'c'])
    setattr(SkiplistList, 'absorb', absorb)
    l1.absorb(l2)

main()
