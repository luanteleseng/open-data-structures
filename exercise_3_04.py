# Imports
from ods import SLList

# Code
def reverse(self):
    if self.n > 1:
        first = self.head
        last = self.tail
        current = self.head.next
        previous = self.head

        while current is not None:
            aux = current.next
            current.next = previous
            previous = current  
            current = aux

        first.next = None
        self.head = last
        self.tail = first


def main():
    v = SLList([1, 2, 3, 4])
    print(v)
    setattr(SLList, 'reverse', reverse)
    v.reverse()

main()
