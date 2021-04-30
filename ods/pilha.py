from .arraystack import ArrayStack


class Pilha(ArrayStack):
    def push(self, x):
        self.add_last(x)

    def pop(self):
        if self.size() != 0:
            return self.remove_last()
