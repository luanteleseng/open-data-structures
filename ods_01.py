import random

from ods.binarysearchtree import BinarySearchTree

lista_p = []

class Treap(BinarySearchTree):
    class Node(BinarySearchTree.Node):
        def __init__(self, x):
            super(Treap.Node, self).__init__(x)
            self.p = random.random()
            lista_p.append(self.p)

        def __str__(self):
            return "[%r,%f]" % (self.x, self.p)

    def __init__(self, iterable=[]):
        super(Treap, self).__init__(iterable)

    def _new_node(self, x):
        return Treap.Node(x)

    def add(self, x):
        u = self._new_node(x)
        if self.add_node(u):
            self.bubble_up(u)
            return True
        return False

    def bubble_up(self, u):
        while u != self.r and u.parent.p > u.p:
            if u.parent.right == u:
                self.rotate_left(u.parent)
            else:
                self.rotate_right(u.parent)

        if u.parent == self.nil:
            self.r = u

    def remove(self, x):
        u = self._find_last(x)
        if u is not None and u.x == x:
            self.trickle_down(u)
            self.splice(u)
            return True
        return False

    def trickle_down(self, u):
        while u.left is not None or u.right is not None:
            if u.left is None:
                self.rotate_left(u)
            elif u.right is None:
                self.rotate_right(u)
            elif u.left.p < u.right.p:
                self.rotate_right(u)
            else:
                self.rotate_left(u)
            if self.r == u:
                self.r = u.parent

# Projete e implemente uma versão de uma Treap que inclua uma operação get(i) que retorna a chave de posição i na Treap.
# (Dica: Faça com que cada nó, u, mantenha o registro do tamanho da subárvore com raiz em u.):

    def get(self, i, current = None):
        if current == None:
            current = self.r
        if current.p == i:
            return current.x
        if current.left:
            left = self.get(i, current.left)
            if left:
                return left
        if current.right:
            right = self.get(i, current.right)
            if right:
                return right

    def print_tree(self, nivel = 0, current = None, label = None):
        if label == None:
            label = 'raiz:'
        if current == None:
            current = self.r
        for i in range(nivel):
            print('\t', end = ' ')
        if label:
            print(label, end=' ')

        print(current.x)

        if current.left:
            self.print_tree(nivel + 1, current.left, 'left:')
        if current.right:
            self.print_tree(nivel + 1, current.right, 'right:')

def main():
    a = Treap([1, 2, 3, 4, 5, 6])
    a.print_tree()
    for p in lista_p:
        print(f'prioridade: {p}; chave: {a.get(p)}')

main()

