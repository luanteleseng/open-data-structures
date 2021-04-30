from ods import utils
from ods import base


class ArrayDeque(base.BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.a = utils.new_array(1)
        self.j = 0
        self.n = 0

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[(i + self.j) & (len(self.a) - 1)]

    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[(i + self.j) & (len(self.a) - 1)]
        self.a[(i + self.j) & (len(self.a) - 1)] = x
        return y

    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a): self._resize()
        if i < self.n / 2:
            self.j = (self.j - 1) & (len(self.a) - 1)
            for k in range(i):
                self.a[(self.j + k) & (len(self.a) - 1)] = self.a[(self.j + k + 1) & (len(self.a) - 1)]
        else:
            for k in range(self.n, i, -1):
                self.a[(self.j + k) & (len(self.a) - 1)] = self.a[(self.j + k - 1) & (len(self.a) - 1)]
        self.a[(self.j + i) & (len(self.a) - 1)] = x
        self.n += 1

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        x = self.a[(self.j + i) & (len(self.a) - 1)]
        if i < self.n / 2:
            for k in range(i, 0, -1):
                self.a[(self.j + k) & (len(self.a) - 1)] = self.a[(self.j + k - 1) & (len(self.a) - 1)]
            self.j = (self.j + 1) & (len(self.a) - 1)
        else:
            for k in range(i, self.n - 1):
                self.a[(self.j + k) & (len(self.a) - 1)] = self.a[(self.j + k + 1) & (len(self.a) - 1)]
        self.n -= 1
        if len(self.a) >= 3 * self.n: self._resize()
        return x

    def _resize(self):
        b = utils.new_array(max(1, 2 * self.n))
        for k in range(self.n):
            b[k] = self.a[(self.j + k) & (len(self.a) - 1)]
        self.a = b
        self.j = 0

def main():
    v = ArrayDeque()
    l = [1, 2, 3, 4]
    for i in range(0, len(l)):
        v.add(i, l[i])
    print(v)

main()
