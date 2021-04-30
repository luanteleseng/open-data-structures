# Imports
from ods import DLList

# Code
def reverse(self):
    if self.n > 1:
        first = self.dummy.next
        last = self.dummy.prev
        current = first

        while current.x is not None:
            previous = current.prev
            next = current.next
            current.prev = next
            current.next = previous
            current = next

    self.dummy.next = last
    self.dummy.prev = first


def main():
    v = DLList([1, 2, 3, 4])
    print(v)
    setattr(DLList, 'reverse', reverse)
    v.reverse()

main()
